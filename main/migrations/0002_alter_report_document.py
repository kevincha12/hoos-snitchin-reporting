# Generated by Django 5.0.2 on 2024-03-17 18:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="report",
            name="document",
            field=models.ManyToManyField(blank=True, to="main.document"),
        ),
    ]
