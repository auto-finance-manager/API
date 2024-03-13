from django.db import models


class ShareModel(models.Model):
    code = models.CharField(max_length=15, primary_key=True)
    title = models.CharField(max_length=250)
    logo = models.CharField(max_length=250, default='')
    graphic = models.CharField(max_length=250)
    # offer_price = models.DecimalField(max_digits=10, decimal_places=2)
    # current_price = models.DecimalField(max_digits=10, decimal_places=2)
    current_price = models.CharField(max_length=50)
    last_updated = models.CharField(max_length=10, null=True)
    # post_offer_return = models.FloatField()


class ShareOwnershipModel(models.Model):
    share = models.ForeignKey('ShareModel', on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # piece = models.IntegerField(default=0)
    # purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    slots = models.ManyToManyField('share.SlotModel')
    # sold = models.BooleanField(default=False)
    tracking = models.BooleanField(default=True)

    def get_slots(self) -> list:
        return self.slots


class SlotModel(models.Model):
    class ProgresType(models.TextChoices):
        T_SALE = 't_sale', 't_sale'
        T_1_SALE = 't_1_sale', 't_1_sale'
        T_2_SALE = 't_2_sale', 't_2_sale'
        BUY = 'buy', 'buy'

    progres_type = models.CharField(max_length=10, choices=ProgresType.choices, default=ProgresType.BUY)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    quantity = models.IntegerField(default=0)
    action_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering: tuple = 'action_time',

    @property
    def is_buy(self):
        return self.progres_type == self.ProgresType.BUY


class PublicOfferingModel(models.Model):
    title = models.CharField(max_length=150, blank=True, null=True)
    details = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.title
