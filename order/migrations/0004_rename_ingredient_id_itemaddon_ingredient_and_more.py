# Generated by Django 4.0.6 on 2022-07-17 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_alter_itemaddon_ingredient_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemaddon',
            old_name='ingredient_id',
            new_name='ingredient',
        ),
        migrations.RenameField(
            model_name='itemaddon',
            old_name='order_item_id',
            new_name='order_item',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='order_id',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='recipe_id',
            new_name='recipe',
        ),
        migrations.AlterField(
            model_name='itemaddon',
            name='add_on_quantity',
            field=models.IntegerField(default=1),
        ),
    ]
