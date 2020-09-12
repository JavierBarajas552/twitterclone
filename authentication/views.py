from django.shortcuts import render, HttpResponseRedirect, reverse
from twitteruser.models import MyUser
from authentication.forms import LoginForm, SignupForm
from django.contrib.auth import login, logout, authenticate
# Create your views here.


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            MyUser = authenticate(request, username=data.get(
                'username'), password=data.get('password'))
            if MyUser:
                login(request, MyUser)
                return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))
    form = LoginForm()
    return render(request, "generic_form.html", {'form': form})


def logout_veiw(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))


def signup_veiw(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid:
            data = form.data
            new_user = MyUser.objects.create_user(
                username=data.get('username'),
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                password=data.get('password')
            )
            login(request, new_user)
            return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))
    form = SignupForm()
    return render(request, 'generic_form.html', {'form': form})
