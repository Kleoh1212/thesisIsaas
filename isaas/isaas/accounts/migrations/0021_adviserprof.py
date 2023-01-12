# Generated by Django 4.1.5 on 2023-01-11 20:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0020_fy2ndsem_nstp2'),
    ]

    operations = [
        migrations.CreateModel(
            name='adviserprof',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adviser_fname', models.CharField(max_length=200, verbose_name='First Name')),
                ('adviser_mname', models.CharField(max_length=200, verbose_name='Middle Name')),
                ('adviser_lname', models.CharField(max_length=200, verbose_name='Last Name')),
                ('adviser_course', models.CharField(max_length=200, verbose_name='Course')),
                ('adviser_yrandsec', models.CharField(max_length=200, verbose_name='Year')),
                ('adviser_section', models.CharField(max_length=200, null=True, verbose_name='Section')),
                ('adviser_address', models.CharField(max_length=200, verbose_name='Address')),
                ('adviser_cnumber', models.CharField(max_length=200, verbose_name='Contact Number')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
