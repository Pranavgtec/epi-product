from django.db import models

class ProductScheme(models.Model):
    product_id = models.CharField(max_length=100, unique=True)
    investment = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    days = models.IntegerField()
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()

    def __str__(self):
        return f"Scheme for {self.product_id} - {self.investment} Investment"

    def calculate_end_date(self):
        from datetime import timedelta
        return self.start_date + timedelta(days=self.days)
