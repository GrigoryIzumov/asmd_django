# Generated by Django 3.0.6 on 2020-05-10 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asmdapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='learningmodel',
            name='name',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]