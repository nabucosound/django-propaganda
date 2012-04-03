from django.db import models


class Propaganda(models.Model):
    """Each different email to be sent"""
    plaintext_msg = models.TextField()
    html_msg = models.TextField()
    subject = models.CharField(max_length=255)
    from_header = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return self.subject


class Subscriber(models.Model):
    """A subscriber of your emails"""
    email = models.EmailField(unique=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.email


class Pamphlet(models.Model):
    """
    Email assigned to a subscriber to be sent.
    The ``delivery_date``, combined on the ``unique_together``, restricts the
    creation of only one Pamphlet assigned to a user per day.
    """
    propaganda = models.ForeignKey(Propaganda)
    subscriber = models.ForeignKey(Subscriber)
    delivery_date = models.DateField()
    sent = models.BooleanField(default=False)

    class Meta:
        # This makes sure we will not send the same email
        # more than one time per day to our subcribers
        unique_together = ('subscriber', 'propaganda', 'delivery_date')

    def __unicode__(self):
        return u"%s - %s" % (self.subscriber, self.propaganda.subject)

