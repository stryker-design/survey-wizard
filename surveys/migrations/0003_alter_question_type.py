# Generated by Django 4.1.2 on 2022-10-06 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0002_question_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[(1, 'Multiple choice'), (2, 'Checked box'), (3, 'Comment box')], default='--------', max_length=15),
        ),
    ]
