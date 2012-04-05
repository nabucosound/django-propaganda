from django.db import models
from django.utils.translation import ugettext as _


class Propaganda(models.Model):
    """Each different email to be sent"""
    plaintext_msg = models.TextField(_("plain text message"))
    html_msg = models.TextField(_("html message"))
    subject = models.CharField(_("subject"), max_length=255)
    from_header = models.CharField(_("sender name"), max_length=255, blank=True)

    def __unicode__(self):
        return self.subject

    class Meta:
        verbose_name = _("propaganda")
        verbose_name_plural = _("propagandas")


class Subscriber(models.Model):
    """A subscriber of your emails"""
    email = models.EmailField(_("email"), unique=True)
    active = models.BooleanField(_("active user"), default=True)
    test_user = models.BooleanField(_("test user"), default=False)

    def __unicode__(self):
        return self.email

    class Meta:
        verbose_name = _("subscriber")
        verbose_name_plural = _("subscribers")


class Pamphlet(models.Model):
    """
    Email assigned to a subscriber to be sent.
    The ``delivery_date``, combined on the ``unique_together``, restricts the
    creation of only one Pamphlet assigned to a user per day.
    """
    propaganda = models.ForeignKey(Propaganda, verbose_name=_("propaganda"))
    subscriber = models.ForeignKey(Subscriber, verbose_name=_("subscriber"))
    delivery_date = models.DateField(_("delivery date"))
    sent = models.BooleanField(_("sent pamphlet"), default=False)

    class Meta:
        # This makes sure we will not send the same email
        # more than one time per day to our subcribers
        unique_together = ('subscriber', 'propaganda', 'delivery_date')
        verbose_name = _("pamphlet")
        verbose_name_plural = _("pamphlets")

    def __unicode__(self):
        return u"%s - %s" % (self.subscriber, self.propaganda.subject)

