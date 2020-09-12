from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import TweetModel
from .forms import TweetForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from notification.models import NoteModle
from twitteruser.models import MyUser
from copy import deepcopy
# Create your views here.


@login_required
def index(request):
    tweets = TweetModel.objects.filter(Q(
        who_tweeted__in=request.user.following.all()) | Q(who_tweeted=request.user))
    return render(request, 'index.html', {'tweets': tweets})


@ login_required
def tweet_veiw(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid:
            data = form.data
            this_tweet = TweetModel.objects.create(
                body=data.get('body'),
                who_tweeted=request.user
            )
            the_note = NoteModle.objects.create(
                the_tweet=this_tweet
            )
            the_note.the_users.set(
                MyUser.objects.filter(following=request.user))
            return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))
    form = TweetForm()
    return render(request, 'generic_form.html', {'form': form})


def this_tweet_veiw(request, tweet_id):
    this_tweet = TweetModel.objects.get(id=tweet_id)
    return render(request, "tweet_view.html", {'tweet': this_tweet})


def this_user_veiw(request, user_id):

    this_user = MyUser.objects.get(id=user_id)
    following_count = this_user.following.count()
    users_tweets = TweetModel.objects.filter(who_tweeted=this_user)
    tweet_count = users_tweets.count()
    return render(request, "user_view.html", {'user': this_user, 'tweets': users_tweets, 'follow_count': following_count, "tweet_count": tweet_count})


@login_required
def follow_veiw(request, user_id):
    request.user.following.add(user_id)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def unfollow_veiw(request, user_id):
    request.user.following.remove(user_id)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def veiw_notifications(request):
    tweets = TweetModel.objects.filter(
        Q(notemodle__in=request.user.notemodle_set.all()))
    return render(request, 'notification.html', {'tweets': tweets})
