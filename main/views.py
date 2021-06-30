

from django.shortcuts import render
from django.views.generic import TemplateView, View, ListView
from requests import request
from django.http.response import HttpResponse
from .models import Advantages, Kurs, News, Category, Video, Tutorial, Comments
from django.core.paginator import Paginator


class MainIndex(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        kwargs["rec"] = Advantages.objects.order_by()[:4].all()
        kwargs["courses"] = Kurs.objects.order_by("-id")[:4].all()

        return super().get_context_data(**kwargs)

class Courses(View):
    # template_name = "layouts/courses.html"
    def get(self, request, pk=None):
        query = Kurs.objects.all()
        if pk is not None:
            query = query.filter(kurs_id=pk)

        paginator = Paginator(query.all(), 4)
        page = paginator.get_page(request.GET.get("page"))
        return render(request, "layouts/courses.html", {
            "courses": page.object_list,
            "page_obj": page,
            "kurs": Kurs.objects.all()

        })



class Tutoriall(TemplateView):
    template_name = "layouts/team.html"
    def get_context_data(self, **kwargs):
        kwargs["biz"] = Tutorial.objects.order_by("-id")

        return super().get_context_data(**kwargs)

# class Courses(TemplateView):
#     model = Kurs
#     template_name = "layouts/courses.html"
#     def get_context_data(self, **kwargs):
#         context = super(Courses, self).get_context_data(**kwargs)
#         context["courses"] = Kurs.objects.all()
#
#         return context



class Coursess(TemplateView):
    template_name = "layouts/video.html"
    def get_context_data(self, **kwargs):
        kwargs["cour"] = Kurs.objects.all()
        return super().get_context_data(**kwargs)




# Yangliklar

class Newss(TemplateView):
    template_name = "layouts/news.html"

    def get_context_data(self, **kwargs):
        kwargs["news"] = News.objects.all()
        return super().get_context_data(**kwargs)


class Neww(TemplateView):
    template_name = "layouts/new.html"


class Add(View):
    def get(self, request, pk):
        self_new = News.objects.get(id=pk)
        return render(request, "layouts/new.html", {
            "row": self_new
        })


# class Video(TemplateView):
#     template_name = "layouts/video.html"



def kurs(request, pk, id):
    try:
        video = Video.objects.get(id=id)
    except:
        return HttpResponse("<h1>Kirish uchun xuquqingiz cheklangan!</h1>", status=404)

    videos = Video.objects.filter(kurs=pk).order_by("id")
    context = {"videos": videos, "video": video.video, "pk": pk,  "count":  [x for x in range(1, videos.count() + 1)]}
    context["courses"] = Kurs.objects.filter(id=pk)
    for x in videos:
        print(x.id)
    return render(request, "layouts/video.html", context)


class Price(View):
    def get(self, request, id):
        price = Kurs.objects.get(price_id=id)
        return render(request, "layouts/video.html", {
            "qw": price
        })

# def video(request, pk, id):
#     video = Video.objects.get(id=id)
#     videos = Video.objects.filter(id=pk)
#     context = {"videos": videos, "video": video.video}
#     return render(request, "layouts/video.html", context)



class Comment(ListView):
    model = Comments
    paginate_by = 10

    def get_queryset(self):
        return super(self).get_queryset().filter(post_id=self.kwargs["post_id"])


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context["post"] = Comments.objects.get(id=self.kwargs["post_id"])
        return context



