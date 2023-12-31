# Generated by Django 5.0 on 2023-12-17 11:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("crud", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="News",
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
                ("title", models.CharField(max_length=50)),
                ("content", models.TextField()),
                ("is_published", models.BooleanField(default=True)),
                (
                    "category",
                    models.CharField(
                        choices=[(1, "Cпорт"), (2, "Красота")], max_length=20
                    ),
                ),
            ],
        ),
    ]
