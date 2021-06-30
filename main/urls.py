from django.urls import path
from django.views.generic import TemplateView
from .views import MainIndex,  Newss, Add, Neww, Video, kurs, Coursess, Courses, Tutoriall, Price, Comment

app_name = "main"

urlpatterns = [
    path("", MainIndex.as_view(), name="index"),
    path("courses/", Courses.as_view(), name="courses"),
    path("cat/<int:pk>/", Courses.as_view(), name="cat"),
    path("course/", Coursess.as_view(), name="course"),
    path("news/", Newss.as_view(), name="news"),
    path("new/<int:id>/", Neww.as_view(), name="new"),
    path("add/<int:pk>/", Add.as_view(), name="add"),
    # path("video/", Video.as_view(), name="video"),
    path("kurs/<int:pk>/<int:id>/", kurs, name="kurs_video"),
    # path("module/<int:id>/", kurs, name="kurs"),
    path("team/", Tutoriall.as_view(), name="team"),
    path("price/<int:id>/", Price.as_view(), name="price"),
    path("comments/<int:post_id>/", Comment.as_view(), name="comments" )
]
