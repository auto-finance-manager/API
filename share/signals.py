from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ShareModel, ShareOwnershipModel
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


@receiver(post_save, sender=ShareModel)
def stock_status_change_notification(sender, created, instance, **kwargs):
    if not created:
        old_price: float = float(1) if float(instance.previous_price) == 0 else float(instance.previous_price)
        new_price: float = float(instance.current_price)
        if changing_rate := calculate_changing_rate(old_price, new_price):
            for share_owner in ShareOwnershipModel.objects.filter(
                share=instance,
                tracking=True
            ):
                msg_context: dict = {
                    'share_owner': share_owner.owner,
                    'changing_rate': changing_rate,
                    'general_status': share_owner.get_general_status,
                    'share': share_owner.share
                }
                send_notification_to_owner(share_owner, msg_context)
            instance.previous_price = instance.current_price
            instance.save()


def calculate_changing_rate(old_price: float, new_price: float) -> float | int:
    if old_price != new_price:
        price_difference: float = new_price - old_price
        percentage_change: float = (price_difference / abs(old_price)) * 100
        if abs(percentage_change) >= 1:
            return round(percentage_change, 2)


def send_notification_to_owner(share, context):
    html_content = render_to_string('mail/share_status_update.html', context)

    html_text = strip_tags(html_content)
    msg = EmailMultiAlternatives('Share Tracker', html_text,
                                 'settings.EMAIL_HOST_USER', (share.owner.email,))
    # msg.attach(image)

    msg.attach_alternative(html_content, "text/html")
    msg.send()


