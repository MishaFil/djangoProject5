from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100000)])
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.title

    def get_category_hierarchy(self):
        categories = [self.category.title]
        current_category = self.category

        while current_category.parent:
            categories.append(current_category.parent.title)
            current_category = current_category.parent

        return ' · '.join(reversed(categories))
