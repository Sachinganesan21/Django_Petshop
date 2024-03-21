# Generated by Django 5.0.1 on 2024-02-05 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Product_brand',
            field=models.CharField(default='Paws', max_length=75),
        ),
        migrations.AddField(
            model_name='product',
            name='Product_picture',
            field=models.ImageField(default='', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='Product_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='Product_description',
            field=models.TextField(default='Product_description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Product_name',
            field=models.CharField(default='Product_name', max_length=100),
        ),
    ]
