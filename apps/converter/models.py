from django.db import models

from apps.converter.services import Currency

class Converter(models.Model):
    CURRENCY_CHOICES = [
        ("RUB", "RUB"),
        ("USD", "USD"),
    ]
    from_currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)
    to_currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)
    value = models.IntegerField()
    
    def __str__(self):
        return f"{self.from_currency} > {self.to_currency}: {self.value}"
    
    def get_value_currency(self):
        currency = Currency()
        if self.from_currency == "RUB":
            return int(self.value) / float(currency.get_price())
        if self.from_currency == "USD":
            return int(self.value) * float(currency.get_price())
