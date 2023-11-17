# Generated by Django 4.2.6 on 2023-10-13 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('slug', models.SlugField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
    ]
