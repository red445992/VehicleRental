# Generated by Django 5.1.4 on 2025-01-13 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='customer_password',
        ),
        migrations.AddField(
            model_name='customer',
            name='order_return_day',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='customer',
            name='order_take_day',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_mobileno',
            field=models.CharField(max_length=15),
        ),
    ]
