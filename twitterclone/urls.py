"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from authentication.views import logout_veiw, SignupVeiw, LoginView
from tweet.views import TweetView, index, veiw_notifications, follow_veiw, unfollow_veiw, TweetDetailVeiw, this_user_veiw
urlpatterns = [
    path('', index, name="homepage"),
    path('notifications/', veiw_notifications),
    path('user/<int:user_id>', this_user_veiw),
    path('tweet/<int:tweet_id>', TweetDetailVeiw.as_view()),
    path('follow/<int:user_id>', follow_veiw),
    path('unfollow/<int:user_id>', unfollow_veiw),
    path('logout/', logout_veiw),
    path('login/', LoginView.as_view()),
    path('tweet/', TweetView.as_view()),
    path('signup/', SignupVeiw.as_view()),
    path('admin/', admin.site.urls),
]
