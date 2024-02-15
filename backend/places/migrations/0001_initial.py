# Generated by Django 3.2.15 on 2023-10-16 13:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geocode_date', models.DateField(default=django.utils.timezone.now, verbose_name='Дата запроса')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Широта')),
                ('lon', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Долгота')),
            ],
            options={
                'unique_together': {('lat', 'lon', 'address')},
            },
        ),
    ]