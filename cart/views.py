from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views import View
from .cartmanager import *

class AddCartView(View):
    def post(self, request):
        # 在多级字典数据的时候，需要手动设置modified=Trur，实时地将数据存储到session对象中
        request.session.modified = True


        # 1.获取当前操作类型是添加简史减少
        flag = request.POST.get("flag","")

        # 2.判断当前操作类型
        if flag == "add":
            # 创建cartManager对象
            carManagerObj = getCartManger(request)
            # 加入购物车
            carManagerObj.add(**request.POST.dict())

        elif flag =="plus":
            # 创建cartManager对象
            carManagerObj = getCartManger(request)
            # 修改商品的数量（添加）
            carManagerObj.update(step=1, **request.POST.dict())
        elif flag == "minus":
            # 创建cartManager对象
            carManagerObj = getCartManger(request)
            # 修改商品的数量（添加）
            carManagerObj.update(step=-1, **request.POST.dict())

        elif flag == "delete":
            # 创建cartManager对象
            carManagerObj = getCartManger(request)
            # 逻辑删除购物车选项
            carManagerObj.delete(**request.POST.dict())

        return HttpResponseRedirect('/cart/queryAll/')


class CartListView(View):
    def get(self,request):
        # 创建cartManager对象

        cartManagerOObj = getCartManger(request)

        # 查询所有购物车信息
        cartList = cartManagerOObj.queryAll()

        return render(request, 'cart.html',{"cartList":cartList})
