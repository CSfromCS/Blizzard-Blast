# Generated by Django 4.0.6 on 2022-07-21 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_rename_ingredient_id_itemaddon_ingredient_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='price_serving',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
