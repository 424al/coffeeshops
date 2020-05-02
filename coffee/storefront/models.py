from django.db import models

# Create your models here.


# List that determines whether or not shop get's approved to be displayed

ACTIVE =(
	(0, "NOT APPROVED"),
	(1, "APPROVED"),
    )


class StoreFront(models.Model):
    name = models.CharField(max_length=250, blank=False)
    street_address = models.CharField(max_length=100, blank=True)
    additional_address_field = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    instagram_username =models.CharField(max_length=100, blank=True)
    status = models.IntegerField(choices=ACTIVE, default=0)
    """
    Fix items below in future branch
    """
    # created_by =
    # lattitude =
    # longitude =
    # uuid =
    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name
