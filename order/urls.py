#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/2/002 22:54
# @Author : H
# @File : urls.py

from django.urls import path

from order import views

urlpatterns = [
    path('', views.ToOrderView.as_view()),
    path('order.html', views.OrderListView.as_view()),
]