# Generated by Django 4.1.4 on 2023-10-12 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='comment',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
