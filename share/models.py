from django.db import models


class ShareModel(models.Model):
    code = models.CharField(max_length=15, primary_key=True)
    title = models.CharField(max_length=250)
    graphic = models.CharField(max_length=250)
    # offer_price = models.DecimalField(max_digits=10, decimal_places=2)
    # current_price = models.DecimalField(max_digits=10, decimal_places=2)
    current_price = models.CharField(max_length=50)
    last_updated = models.CharField(max_length=10, null=True)
    # post_offer_return = models.FloatField()


class ShareOwnershipModel(models.Model):
    share = models.ForeignKey('ShareModel', on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    piece = models.IntegerField(default=0)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)

    sold = models.BooleanField(default=False)
    tracking = models.BooleanField(default=True)


