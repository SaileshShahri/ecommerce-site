# Generated by Django 3.0.6 on 2020-05-17 07:56

from django.db import migrations, models
import django.db.models.deletion
import product.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorytype', models.CharField(blank=True, max_length=300)),
                ('title', models.CharField(max_length=140)),
                ('image', models.ImageField(null=True, upload_to=product.models.upload_image_path)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('comparedprice', models.DecimalField(decimal_places=2, max_digits=20)),
                ('quantity', models.DecimalField(decimal_places=0, max_digits=20)),
                ('description', models.TextField(max_length=1000)),
                ('keyword', models.TextField(max_length=500)),
                ('slug', models.SlugField(blank=True, max_length=140, null=True, unique=True)),
                ('variants_type', models.CharField(blank=True, choices=[('Size', 'Size'), ('Colour', 'Colour'), ('Material', 'Material'), ('Style', 'Style'), ('Other', 'Other')], max_length=18)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductVariant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('comparedprice', models.DecimalField(decimal_places=2, max_digits=20)),
                ('quantity', models.IntegerField()),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
            ],
        ),
    ]