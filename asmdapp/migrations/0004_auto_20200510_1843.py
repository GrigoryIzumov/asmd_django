# Generated by Django 3.0.6 on 2020-05-10 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asmdapp', '0003_learningmodel_name2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='learningmodel',
            name='name',
        ),
        migrations.RemoveField(
            model_name='learningmodel',
            name='name2',
        ),
        migrations.RemoveField(
            model_name='learningmodel',
            name='title',
        ),
    ]