# Generated by Django 3.2.4 on 2022-03-10 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('satlab_portal', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='post',
            new_name='postfeed',
        ),
    ]
