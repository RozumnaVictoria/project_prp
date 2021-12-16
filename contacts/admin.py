from django.contrib import admin
from contacts.models import Contacts


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    fields = ['address', 'number_tel', 'email', 'schedule']

    def has_add_permission(self, request):
        if not self.model.objects.count():
            return True
        return False
