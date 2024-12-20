# Generated by Django 4.2 on 2024-12-17 14:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("parking_spot", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="booking",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name="parkingspot",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
