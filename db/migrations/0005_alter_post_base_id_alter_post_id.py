# Generated by Django 4.2.6 on 2023-10-27 19:41

import uuid

from django.db import migrations, models


def up(apps, schema_apps):
    post_model = apps.get_model('db', 'Post')
    posts = post_model.objects.all()
    for post in posts:
        post.id = post.base_id
        post.save()

def down(apps, schema_apps):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0004_post_base_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.CharField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='base_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.RunPython(up, down, True)
    ]