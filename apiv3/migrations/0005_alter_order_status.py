# Generated by Django 4.2.3 on 2023-08-05 23:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("apiv3", "0004_mono"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(max_length=50),
        ),
    ]
