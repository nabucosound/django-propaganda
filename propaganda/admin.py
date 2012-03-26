from django.contrib import admin
from propaganda.models import Propaganda, Subscriber, Pamphlet


class PropagandaAdmin(admin.ModelAdmin):
    list_display = ('subject', 'from_header')


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'active')


class PamphletAdmin(admin.ModelAdmin):
    list_display = ('subscriber', 'propaganda', 'creation_date', 'sent')
    list_filter = ('creation_date', 'sent')


admin.site.register(Propaganda, PropagandaAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(Pamphlet, PamphletAdmin)
