from django.db import models
import datetime

class OrderSlip(models.Model):
    order_id = models.AutoField(primary_key=True, editable=False)
    customer_name = models.CharField(max_length=64)
    date_ordered = models.DateField(default=datetime.date.today)
 
    @property
    def order_price(self):
        order_price = 0
        OrderItems = OrderItem.objects.filter(order=self)
        for oi in OrderItems:
            order_price += oi.item_price
        return order_price

    def __str__(self):
        return f"[O{self.order_id}] {self.customer_name}"

class Recipe(models.Model):
    recipe_id = models.AutoField(primary_key=True, editable=False)
    recipe_name = models.CharField(max_length=64)
    serving_size = models.IntegerField()
    price = models.DecimalField(max_digits=8,decimal_places=2)

    def __str__(self):
        return f"[R{self.recipe_id}] {self.recipe_name} ({self.serving_size}oz)"

class OrderItem(models.Model):
    order_item_id = models.AutoField(primary_key=True, editable=False)
    order = models.ForeignKey(OrderSlip, on_delete=models.CASCADE, db_column='order_id')
    recipe = models.ForeignKey(Recipe, on_delete=models.RESTRICT, db_column='recipe_id')
    
    @property
    def item_price(self):
        item_price = 0
        item_price += self.recipe.price
        AddOns = ItemAddOn.objects.filter(order_item=self)
        for AddOn in AddOns:
            item_price += AddOn.ingredient.price_serving * AddOn.add_on_quantity
        return item_price
    
    def __str__(self):
        return f"[OI{self.order_item_id}] {self.order.customer_name}-{self.recipe.recipe_name}"

class Ingredient(models.Model):
    ingredient_id = models.AutoField(primary_key=True, editable=False)
    ingredient_name = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    stock_quantity = models.IntegerField()
    price_serving = models.DecimalField(max_digits=8,decimal_places=2)

    def __str__(self):
        return f"[I{self.ingredient_id}] {self.ingredient_name}"

class ItemAddOn(models.Model):
    item_addon_id = models.AutoField(primary_key=True, editable=False)
    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE, db_column='order_item_id')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.RESTRICT, db_column='ingredient_id')
    add_on_quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"[IA{self.item_addon_id}] {self.order_item.recipe.recipe_name}-{self.ingredient.ingredient_name}"
