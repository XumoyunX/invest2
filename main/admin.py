from django.contrib import admin
from .models import  Category, Kurs, Video, Advantages, News, Tutorial


class AdvantagesAdmin(admin.ModelAdmin):
    list_display = [
        "photo",
        "subject_uz",
        "subject_ru",
    ]

    class Meta:
        model = Advantages

admin.site.register(Advantages, AdvantagesAdmin)

# 1 hammasi bitta maliyot saqledi
class CategoryAdmin(admin.ModelAdmin):

    list_display = [
        "name"
    ]

    class Meta:
        model = Category


admin.site.register(Category, CategoryAdmin)

class KursAdmin(admin.ModelAdmin):

    list_display = [
        "category",
        "subject_uz",
        "subject_ru",
        "content_uz",
        "content_ru",
        "photo",
        "price",
    ]

    class Meta:
        model = Kurs


admin.site.register(Kurs, KursAdmin)


class NewsAdmin(admin.ModelAdmin):

    list_display = [
        "content_uz",
        "content_ru",
        "subject_uz",
        "subject_ru",
        "photo",

    ]
    class Meta:
        model = News

admin.site.register(News, NewsAdmin)



class VideoAdmin(admin.ModelAdmin):

    list_display = [
        "kurs",
        "video",
        "soni"
    ]
    class Meta:
        model = Video

admin.site.register(Video, VideoAdmin)


# class VideoLessonAdmin(admin.ModelAdmin):
#
#     list_display = [
#         "subject_uz",
#         "subject_ru",
#         'name_uz',
#         'name_ru',
#         "photo",
#     ]
#
#     class Meta:
#         model = VideoLesson
#
# admin.site.register(VideoLesson, VideoLessonAdmin)



# class LessonAdvertisingAdmin(admin.ModelAdmin):
#     list_display = [
#         "subject_uz",
#         "subject_ru",
#         "content_uz",
#         "content_ru",
#         "video",
#     ]
#
#     class Meta:
#         model = LessonAdvertising
#
#
# admin.site.register(LessonAdvertising, LessonAdvertisingAdmin)




class TutorialAdmin(admin.ModelAdmin):
    list_display = [
        "subject_uz",
        "subject_ru",
        "content_uz",
        "content_ru",
        "photo",
    ]

    class Meta:
        model = Tutorial


admin.site.register(Tutorial, TutorialAdmin)

#
#
#
#
# class AdvantagesAdmin(admin.ModelAdmin):
#
#     list_display = [
#         "subject_uz",
#         "subject_ru",
#         "photo",
#     ]
#
#     class Meta:
#         model = Advantages
#
#
# admin.site.register(Advantages, AdvantagesAdmin)





#
#
# class NewAdmin(admin.ModelAdmin):
#
#     list_display = [
#         "news",
#         "name_uz",
#         "name_ru",
#         "subject_uz",
#         "subject_ru",
#         "photo",
#
#     ]
#
#     class Meta:
#         model = New
#
#
# admin.site.register(New, NewAdmin)




