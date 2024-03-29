# Generated by Django 4.2.9 on 2024-03-05 08:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("title", models.CharField(max_length=100)),
                ("author", models.CharField(max_length=50)),
                ("publication_date", models.DateField()),
                (
                    "isbn",
                    models.CharField(
                        max_length=13,
                        validators=[django.core.validators.MinLengthValidator(13)],
                    ),
                ),
            ],
        ),
    ]
