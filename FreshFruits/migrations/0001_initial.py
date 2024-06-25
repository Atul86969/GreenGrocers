# Generated by Django 5.0.2 on 2024-03-16 18:16

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
                ('name', models.CharField(max_length=50, verbose_name='Product Name')),
                ('price', models.IntegerField()),
                ('catg', models.CharField(default='', max_length=50)),
                ('product_details', models.CharField(max_length=500, verbose_name='Product Details')),
                ('is_active', models.BooleanField(default=True, verbose_name='Available')),
                ('img', models.ImageField(upload_to='image')),
            ],
        ),
    ]
