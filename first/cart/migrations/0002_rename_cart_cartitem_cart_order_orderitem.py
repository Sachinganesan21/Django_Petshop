# Generated by Django 5.0.1 on 2024-03-12 06:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0004_alter_product_category'),
        ('cart', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='Cart',
            new_name='cart',
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.CharField(default='OrderXYZ', max_length=200, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=100)),
                ('pincode', models.IntegerField()),
                ('phoneno', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.PositiveBigIntegerField(default=1)),
                ('Total', models.IntegerField()),
                ('Products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.product')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.order')),
            ],
        ),
    ]
