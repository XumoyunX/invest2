# Generated by Django 3.2.4 on 2021-06-25 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210625_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='soni',
            field=models.IntegerField(default=(5)),
            preserve_default=False,
        ),
    ]
