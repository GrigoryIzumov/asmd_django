# Generated by Django 3.0.6 on 2020-05-12 04:36

import asmdapp.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asmdapp', '0006_learningmodel_date_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=asmdapp.models.user_directory_path)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asmdapp.LearningModel')),
            ],
        ),
    ]
