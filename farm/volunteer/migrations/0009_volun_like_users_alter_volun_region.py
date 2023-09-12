# Generated by Django 4.2.4 on 2023-08-17 16:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("volunteer", "0008_alter_volun_region"),
    ]

    operations = [
        migrations.AddField(
            model_name="volun",
            name="like_users",
            field=models.ManyToManyField(
                blank=True, related_name="like_users", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="volun",
            name="region",
            field=models.CharField(
                choices=[
                    ("jeolla", "전라도"),
                    ("gyeongsong", "경상도"),
                    ("gangwon", "강원도"),
                    ("metropolitan", "광역시"),
                    ("chungcheong", "충청도"),
                    ("jeju", "제주도"),
                    ("gyeonggi", "경기도"),
                    ("seoul", "서울"),
                ],
                max_length=400,
                null=True,
            ),
        ),
    ]