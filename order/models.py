from django.db import models
import datetime

class OrderSlip(models.Model):
    order_id = models.AutoField(primary_key=True, editable=False)
    customer_name = models.CharField(max_length=64)
    date_ordered = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f"[{self.order_id}] {self.customer_name}"

class Recipe(models.Model):
    recipe_id = models.AutoField(primary_key=True, editable=False)
    recipe_name = models.CharField(max_length=64)
    serving_size = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return f"[{self.recipe_id}] {self.recipe_name} ({self.serving_size}oz)"

class OrderItem(models.Model):
    order_item_id = models.AutoField(primary_key=True, editable=False)
    order_id = models.ForeignKey(OrderSlip, on_delete=models.CASCADE, db_column='order_id')
    recipe_id = models.ForeignKey(Recipe, on_delete=models.RESTRICT, db_column='recipe_id')
    item_price = 2

    def __str__(self):
        return f"[{self.order_item_id}] {self.order_id}-{self.recipe_id}"

class Ingredient(models.Model):
    ingredient_id = models.AutoField(primary_key=True, editable=False)
    ingredient_name = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    stock_quantity = models.IntegerField()
    price_serving = models.IntegerField()

    def __str__(self):
        return f"[{self.ingredient_id}] {self.ingredient_name}"

class ItemAddOn(models.Model):
    item_addon_id = models.AutoField(primary_key=True, editable=False)
    order_item_id = models.ForeignKey(OrderItem, on_delete=models.CASCADE, db_column='order_item_id')
    ingredient_id = models.ForeignKey(Ingredient, on_delete=models.RESTRICT, db_column='ingredient_id')
    add_on_quantity = models.IntegerField()

    def __str__(self):
        return f"[{self.item_addon_id}] {self.order_item_id}-{self.ingredient_id}"
