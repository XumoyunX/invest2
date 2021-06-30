from django.db import models


class LessonAdvertising(models.Model):
    subject_uz = models.CharField(max_length=150, verbose_name="Dars nomi")
    subject_ru = models.CharField(max_length=150, verbose_name="Название курса")
    content_uz = models.CharField(max_length=150, verbose_name="Dars mavzusi")
    content_ru = models.CharField(max_length=150, verbose_name="Тема курса")
    video = models.FileField(upload_to="video/")


class Tutorial(models.Model):
    subject_uz = models.CharField(max_length=150, verbose_name="Dars mavzusi")
    subject_ru = models.CharField(max_length=150, verbose_name="Тема курса")
    content_uz = models.CharField(max_length=150, verbose_name="Dars haqida malumotlar")
    content_ru = models.CharField(max_length=150, verbose_name="Информация о курсе")
    photo = models.ImageField(upload_to="images/")

    class Meta:
        verbose_name = "Biz"
        verbose_name_plural = "Bizlar"


class VideoLesson(models.Model):
    subject_uz = models.CharField(max_length=150, verbose_name="Darsnomi")
    subject_ru = models.CharField(max_length=150, verbose_name="Название курса")
    name_uz = models.CharField(max_length=150)
    name_ru = models.CharField(max_length=150)
    photo = models.ImageField(upload_to="images/")
    class Meta:
        verbose_name = "DarsReklama"
        verbose_name_plural = "DarsReklamalar"


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Darsni nomi")

    def __str__(self):
        return self.name

class Kurs(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subject_uz = models.CharField(max_length=200)
    subject_ru = models.CharField(max_length=200)
    content_uz = models.TextField()
    content_ru = models.TextField()
    photo = models.ImageField(upload_to="images/")
    price = models.PositiveBigIntegerField()

    def __str__(self):
        return self.subject_uz

    class Meta:
        verbose_name = "Kurs"
        verbose_name_plural = "Kurslar"


class Video(models.Model):
    kurs = models.ForeignKey(Kurs, on_delete=models.RESTRICT)
    content_uz = models.TextField()
    content_ru = models.TextField()
    video = models.FileField(upload_to="video/")
    soni = models.IntegerField()


class Comments(models.Model):
    video = models.ForeignKey(Video, on_delete=models.RESTRICT)
    comment = models.TextField()


# 1 Birinchi ciqadigan rasm va soʻz
class Advantages(models.Model):
    photo = models.ImageField(upload_to="images/")
    subject_uz = models.CharField(max_length=150, verbose_name="Matn sarlavhasi")
    subject_ru = models.CharField(max_length=150, verbose_name="Заголовок текста")

    class Meta:
        verbose_name = "Afzallik"
        verbose_name_plural = "Afzalliklari"

# 1 End


# News model
class News(models.Model):
    photo = models.ImageField(upload_to="images/")
    subject_uz = models.TextField()
    subject_ru = models.TextField()
    content_uz = models.TextField()
    content_ru = models.TextField()


    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"

# End


