from datetime import date

from django.db import IntegrityError
from propaganda.models import Propaganda, Subscriber, Pamphlet


def generate_pamphlets(propaganda=None, subscribers=None, delivery_date=None):
    """Returns a list of pamphlets with propaganda to be sent to subscribers"""
    pamphlets= []

    # Defaults are latest added propaganda, all active users, deliver today
    email = propaganda or Propaganda.objects.latest('id')
    subscribers = subscribers or Subscriber.objects.filter(active=True)
    delivery_date = delivery_date or date.today()

    # Create pamphlets
    for subscriber in subscribers:
        try:
            pamphlet = Pamphlet.objects.create(propaganda=email,
                    subscriber=subscriber, delivery_date=delivery_date)
        except IntegrityError:
            pass  # Subscriber already has email set for the given date
        else:
            pamphlets.append(pamphlet)

    return pamphlets
