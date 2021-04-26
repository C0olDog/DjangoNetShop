#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/30/030 15:38
# @Author : H
# @File : urls.py

from django.urls import path, re_path

from userapp import views

urlpatterns = [
    path('register/',views.Register.as_view()),
    path('checkUname/',views.CheckUnameView.as_view()),
    path('center/',views.CenterView.as_view()),
    path('logout/',views.LogoutView.as_view()),
    path("login/", views.LoginView.as_view()),
    path('loadCode.jpg',views.LoadCode.as_view()),
    path('checkcode/',views.CheckCode.as_view()),
    path('address/',views.AddressView.as_view()),
    path('loadArea/',views.LoadAreaView.as_view()),
]