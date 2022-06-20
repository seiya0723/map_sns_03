from django.shortcuts import render,redirect
from django.views import View

from .models import Park,Category,Tag
from .forms import ParkForm,TagSearchForm

from django.db.models import Q

class IndexView(View):

    def get(self, request, *args, **kwargs):

        context = {}
        context["categories"]   = Category.objects.all()
        context["tags"]         = Tag.objects.all()

        #TODO:ここで公園を検索するバリデーションを行う。

        #TODO:公園名の検索

        query   = Q()

        if "search" in request.GET:
            search      = request.GET["search"]

            raw_words   = search.replace("　"," ").split(" ")
            words       = [ w for w in raw_words if w != "" ]

            for w in words:
                query &= Q(name__contains=w)


        #TODO:カテゴリの検索










        #TODO:多対多の検索
        """
        form    = TagSearchForm(request.GET)

        if form.is_valid():
            cleaned = form.clean()
            for tag in cleaned["tag"]:
                print(tag.id)
        """

        #多対多の取得
        #(下記と、カスタムテンプレートタグを使用してチェックする必要がある。)
        #print(request.GET.getlist("tag"))


        context["parks"]        = Park.objects.order_by("-dt")

        return render(request, "sns/index.html", context)

    def post(self, request, *args, **kwargs):

        form    = ParkForm(request.POST)

        if form.is_valid():
            print("バリデーションOK")
            form.save()
        else:
            print("バリデーションNG")
            print(form.errors)

        return redirect("sns:index")

index   = IndexView.as_view()
