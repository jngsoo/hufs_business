from django.contrib import admin
from django.urls import path

import account.views
import main.views

urlpatterns = [
    path('admin/', admin.site.urls),

    ## locker include
    path('locker/', account.views.locker, name="locker"),

    # include 전
    path('signup/', account.views.Login, name="login"),
    path('', account.views.UserSignupView.as_view(), name="signup"),


]
