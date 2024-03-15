from django.db import models
from datetime import timedelta, datetime
import pytz  # Import pytz module for timezone handling


class ShareModel(models.Model):
    code = models.CharField(max_length=15, primary_key=True)
    title = models.CharField(max_length=250)
    logo = models.CharField(max_length=250, default='')
    graphic = models.CharField(max_length=250)
    # offer_price = models.DecimalField(max_digits=10, decimal_places=2)
    # current_price = models.DecimalField(max_digits=10, decimal_places=2)
    current_price = models.CharField(max_length=50)
    previous_price = models.CharField(max_length=50, default='0')
    last_updated = models.CharField(max_length=10, null=True)
    # post_offer_return = models.FloatField()

    class Meta:
        ordering: tuple = 'code',

    def __str__(self):
        return f'{self.code}-{self.title}'


class ShareOwnershipModel(models.Model):
    share = models.ForeignKey('ShareModel', on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # piece = models.IntegerField(default=0)
    # purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    slots = models.ManyToManyField('share.SlotModel')
    # sold = models.BooleanField(default=False)
    tracking = models.BooleanField(default=True)

    @property
    def get_general_status(self):
        remaining_lots = 0
        total_profit = 0
        if slots := self.slots.all():
            for transaction in slots:
                if transaction.progres_type == transaction.ProgresType.BUY:
                    remaining_lots += transaction.quantity
                    # total_profit += float(transaction.price) * transaction.quantity
                    total_profit += transaction.quantity * float(self.share.current_price)
                else:
                    sold_lots = transaction.quantity
                    sale_price = float(transaction.price)
                    profit = sold_lots * (sale_price - float(self.share.current_price))
                    total_profit += profit
                    remaining_lots -= sold_lots
        return {
            'total_profit': f'{total_profit:.2f}',
            'remaining_lots': remaining_lots
        }

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

    @property
    def is_sale_cooldown(self):
        # now = datetime.now()  # Get current datetime
        # now = now.replace(tzinfo=None)  # Make it offset-naive
        now = datetime.now(pytz.utc)  # Get current datetime with UTC timezone

        match self.progres_type:
            case self.ProgresType.BUY:
                return True
            case self.ProgresType.T_SALE:
                return self.action_time < now
            case self.ProgresType.T_1_SALE:
                return (self.action_time + timedelta(days=1)) < now
            case self.ProgresType.T_2_SALE:
                return (self.action_time + timedelta(days=2)) < now


class PublicOfferingModel(models.Model):
    title = models.CharField(max_length=150, blank=True, null=True)
    details = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.title
