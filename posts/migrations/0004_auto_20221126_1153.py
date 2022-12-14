# Generated by Django 4.1.3 on 2022-11-26 19:42

from django.db import migrations


def populate_status(apps, schema_editor):
    statuses = {
        "published": "A post that has been published for all to view.",
        "draft": "A post that has not yet been published.",
    }
    Status = apps.get_model("posts", "Status")
    for name, desc in statuses.items():
        status = Status(name=name, description=desc)
        status.save()


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0003_status_post_status"),
    ]

    operations = [
        migrations.RunPython(populate_status),
    ]
