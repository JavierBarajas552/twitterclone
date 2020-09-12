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
from authentication.views import signup_veiw, login_view, logout_veiw
from tweet.views import tweet_veiw, index, veiw_notifications, follow_veiw, unfollow_veiw, this_tweet_veiw, this_user_veiw
urlpatterns = [
    path('', index, name="homepage"),
    path('notifications/', veiw_notifications),
    path('user/<int:user_id>', this_user_veiw),
    path('tweet/<int:tweet_id>', this_tweet_veiw),
    path('follow/<int:user_id>', follow_veiw),
    path('unfollow/<int:user_id>', unfollow_veiw),
    path('logout/', logout_veiw),
    path('login/', login_view),
    path('tweet/', tweet_veiw),
    path('signup/', signup_veiw),
    path('admin/', admin.site.urls),
]
