# --- subscriber verification --- start ---------------------------------------
from django.contrib import admin

from emencia.models \
    import SubscriberVerification

class SubscriberVerificationAdmin(admin.ModelAdmin):
    fields = ['link_id', 'contact']

admin.site.register(SubscriberVerification, SubscriberVerificationAdmin)
# --- subscriber verification --- end -----------------------------------------
