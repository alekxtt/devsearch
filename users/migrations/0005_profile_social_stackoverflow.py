# Generated by Django 3.2.4 on 2021-10-16 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20211016_1120'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='social_Stackoverflow',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]