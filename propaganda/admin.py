from django.contrib import admin
from django.utils.translation import ugettext as _
from propaganda.models import Propaganda, Subscriber, Pamphlet


class PropagandaAdmin(admin.ModelAdmin):
    list_display = ('subject', 'from_header', 'current')
    search_fields = ('subject', 'plaintext_msg', 'html_msg',)
    list_filter = ('from_header',)
    ordering = ('-id',)

    def current(self, obj):
        return obj == Propaganda.objects.latest('id')
    current.short_description = _("current")
    current.boolean = True


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'active', 'test_user')
    list_filter = ('active', 'test_user')
    search_fields = ('email',)


class PamphletAdmin(admin.ModelAdmin):
    list_display = ('subscriber', 'propaganda', 'delivery_date', 'sent')
    list_filter = ('delivery_date', 'sent')


admin.site.register(Propaganda, PropagandaAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(Pamphlet, PamphletAdmin)
