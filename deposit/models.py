from django.db import models


class Deposit(models.Model):
    deposit = models.DecimalField(decimal_places=1, max_digits=10, null=True, blank=True)
    term = models.DecimalField(decimal_places=1, max_digits=10, null=True, blank=True)
    rate = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    interest = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
