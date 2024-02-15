# Generated by Django 3.2.15 on 2023-10-15 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0041_orderitem_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.PositiveIntegerField(choices=[(1, 'Необработанный'), (2, 'Обрабатывается'), (3, 'Доставляет курьер'), (4, 'Выполнен')], default=1, verbose_name='статус'),
        ),
    ]