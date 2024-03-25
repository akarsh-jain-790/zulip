# Generated by Django 4.2.10 on 2024-03-23 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("zerver", "0501_mark_introduce_zulip_view_modals_as_read"),
    ]

    operations = [
        migrations.AddField(
            model_name="realm",
            name="custom_welcome_message_enabled",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="realm",
            name="custom_welcome_message_text",
            field=models.TextField(default=""),
        ),
    ]
