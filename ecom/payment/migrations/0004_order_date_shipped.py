# Generated by Django 5.1 on 2024-08-17 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_order_shipped'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_shipped',
            field=models.DateField(blank=True, null=True),
        ),
    ]
