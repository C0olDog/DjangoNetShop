#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/30/030 16:14
# @Author : H
# @File : mycontextprocessors.py

def getUserInfo(request):

    return {"suser":request.session.get('user',None)}