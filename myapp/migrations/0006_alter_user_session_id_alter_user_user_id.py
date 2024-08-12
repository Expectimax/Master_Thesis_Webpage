# Generated by Django 5.0.6 on 2024-08-02 16:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0005_alter_user_country"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="session_id",
            field=models.CharField(default="no_session_id", max_length=40),
        ),
        migrations.AlterField(
            model_name="user",
            name="user_id",
            field=models.CharField(default="no_user_id", max_length=200),
        ),
    ]
