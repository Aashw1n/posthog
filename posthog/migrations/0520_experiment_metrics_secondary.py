# Generated by Django 4.2.15 on 2024-11-18 12:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posthog", "0519_errortrackingissue_description_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="experiment",
            name="metrics_secondary",
            field=models.JSONField(blank=True, default=list, null=True),
        ),
    ]
