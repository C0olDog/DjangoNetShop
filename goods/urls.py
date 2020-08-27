#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/27/027 23:21
# @Author : H
# @File : urls.py
from django.urls import path, re_path, include

from goods import views

urlpatterns = [
    path('',views.IndexView.as_view())
]