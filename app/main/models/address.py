from django.db import models


class Address(models.Model):
    address = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    state = models.CharField(max_length=64)
    zipcode = models.CharField(max_length=8)

    class Meta:
        ordering = ['pk']
        verbose_name_plural = 'addresses'
        db_table = 'address'
