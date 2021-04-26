#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/31/031 23:38
# @Author : H
# @File : urls.py


from django.urls import path

from cart import views

urlpatterns = [
    path('', views.AddCartView.as_view()),
    path('queryAll/', views.CartListView.as_view()),
]

