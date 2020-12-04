# Generated by Django 3.1.4 on 2020-12-04 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0002_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('contact', models.CharField(max_length=15)),
                ('gender', models.CharField(max_length=1)),
            ],
        ),
    ]
