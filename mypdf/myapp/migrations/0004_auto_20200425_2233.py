# Generated by Django 3.0.5 on 2020-04-25 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20200425_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='my_pdf',
            name='pdf',
            field=models.ImageField(default='', upload_to='myapp/pdf'),
        ),
    ]
