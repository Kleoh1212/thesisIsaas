# Generated by Django 4.1.5 on 2023-01-06 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_rename_user_yrandsec_studentprof_yrandsec'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentprof',
            old_name='yrandsec',
            new_name='user_yrandsec',
        ),
    ]
