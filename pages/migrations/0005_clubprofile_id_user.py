# Generated by Django 5.0 on 2024-04-16 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_rename_phonenumber_clubprofile_phonenumber1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='clubprofile',
            name='id_user',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]