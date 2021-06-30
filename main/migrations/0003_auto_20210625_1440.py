# Generated by Django 3.2.4 on 2021-06-25 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_news_button'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Kurs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_uz', models.CharField(max_length=200)),
                ('subject_ru', models.CharField(max_length=200)),
                ('content_uz', models.TextField()),
                ('content_ru', models.TextField()),
                ('photo', models.ImageField(upload_to='images/')),
                ('price', models.PositiveBigIntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
            ],
            options={
                'verbose_name': 'Kurs',
                'verbose_name_plural': 'Kurslar',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('content_uz', models.TextField()),
                ('content_ru', models.TextField()),
                ('price', models.PositiveBigIntegerField()),
                ('video', models.FileField(upload_to='video/')),
                ('kurs', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.kurs')),
            ],
        ),
        migrations.RemoveField(
            model_name='vidotitle',
            name='category',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='name_ru',
            new_name='content_ru',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='name_uz',
            new_name='content_uz',
        ),
        migrations.DeleteModel(
            name='Dars',
        ),
        migrations.DeleteModel(
            name='VidoTitle',
        ),
        migrations.AddField(
            model_name='comments',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.video'),
        ),
    ]
