# Generated by Django 3.0.8 on 2021-04-19 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Minimaliste', '0021_auto_20210418_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='coverImg',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
