# Generated by Django 4.2 on 2024-12-13 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_useraccountverification"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="auth_provider",
            field=models.CharField(
                blank=True,
                choices=[("GOOGLE", "Google"), ("BY-CREDENTIALS", "By_credentials")],
                default="BY-CREDENTIALS",
                max_length=30,
            ),
        ),
    ]
