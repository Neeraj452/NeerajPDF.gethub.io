# Generated by Django 3.0.5 on 2020-04-25 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='My_pdf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(max_length=50)),
                ('subject', models.CharField(default='', max_length=50)),
                ('pdf', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
