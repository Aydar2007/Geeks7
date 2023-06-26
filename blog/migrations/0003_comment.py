# Generated by Django 4.2.2 on 2023-06-22 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_alter_post_options_alter_post_content_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=16, verbose_name="Имя пользователя"),
                ),
                (
                    "comment",
                    models.CharField(max_length=300, verbose_name="Текст комментария"),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now=True, verbose_name="Дата публикации"),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="post_comment",
                        to="blog.post",
                        verbose_name="Запись",
                    ),
                ),
            ],
            options={
                "verbose_name": "Комментарий",
                "verbose_name_plural": "Комментарии",
            },
        ),
    ]