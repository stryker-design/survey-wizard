# Generated by Django 4.1 on 2022-11-02 13:42

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_id_post_uuid'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('date_created', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
