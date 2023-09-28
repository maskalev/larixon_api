from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name="Title")

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=30, verbose_name="City")

    class Meta:
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.name


class Advert(models.Model):
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Created", db_index=True
    )
    title = models.CharField(max_length=50, verbose_name="Title", db_index=True)
    description = models.TextField(verbose_name="Description", db_index=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="City")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Category"
    )
    views = models.PositiveIntegerField(default=0, verbose_name="Views")

    def __str__(self):
        return self.title
