# Generated by Django 3.0.4 on 2020-05-31 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200531_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='', max_length=225),
            preserve_default=False,
        ),
    ]
