# Generated by Django 3.0.5 on 2020-04-25 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20200425_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='my_pdf',
            name='pdf',
            field=models.FileField(upload_to='books/pdfs/'),
        ),
    ]
