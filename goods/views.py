import math

from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from django.views import View

from goods.models import *


class IndexView(View):
    def get(self, request, cid=6, num=1):
        cid = int(cid)
        num = int(num)
        # 查询所有类别信息
        categoryslist = Category.objects.all().order_by('id')

        # 查询当前类别下的所有商品信息
        goodslist = Goods.objects.filter(category_id=cid).order_by('id')

        # 分页 每页显示八条数据
        pager = Paginator(goodslist, 8)
        # 获取当前页的数据
        page_goodslist = pager.page(num)

        # 每页开始页码
        begin = (num - int(math.ceil(10.0 / 2)))
        if begin < 1:
            begin = 1

        # 每页结束页码
        end = begin + 9
        if end > pager.num_pages:
            end = pager.num_pages

        if end <= 10:
            begin = 1
        else:
            begin = end - 9

        pageList = range(begin, end + 1)
        currentPage = num

        return render(request, 'index.html',
                      {"page_goodslist": page_goodslist, "categoryslist": categoryslist, "currentCid": cid,
                       "pagelist": pageList, "currentPage": currentPage})


# 思考1：最终需要获取的推荐商品  goodsObjList=[]
# 思考2: get方法只能获取到每次访客goodsid   goodsIdList=[]
# 思考3：将每次访问的商品编号保存下来。将它保存到cookie中。
# 思考4：考虑推荐商品展示的先后顺序

def recommend_view(func):
    def wrapper(detailView, request, goodsid, *args, **kwargs):
        # 将存放在cookie中的goodId获取
        cookie_str = request.COOKIES.get('recommend', '')

        # 存放所有goodsid的列表
        goodsIdList = [gid for gid in cookie_str.split(" ") if gid.strip()]

        # 最终需要获取的推荐商品
        goodsObjList = [Goods.objects.get(id=gsid) for gsid in goodsIdList if
                        gsid != goodsid and Goods.objects.get(id=gsid).category_id == Goods.objects.get(
                            id=goodsid).category_id][:4]

        # 将goodsObjList传递给get方法
        response = func(detailView, request, goodsid, goodsObjList, *args, **kwargs)

        # 判断goodsid是否存在于goodsIdList

        if goodsid in goodsIdList:
            goodsIdList.remove(goodsid)
            goodsIdList.insert(0, goodsid)
        else:
            goodsIdList.insert(0, goodsid)

        # 将googsIdList中的数据存储到Cookies中
        response.set_cookie('recommend', ' '.join(goodsIdList), max_age=3 * 24 * 60 * 60)
        return response

    return wrapper


class DetailView(View):
    @recommend_view
    def get(self, request, goodsid=1, recommendList=[]):
        goodsid = int(goodsid)
        # 根据goodid查询商品详细信息，goods对象
        goods = Goods.objects.get(id=goodsid)
        return render(request, 'detail.html', {"goods": goods, "recommendList": recommendList})
