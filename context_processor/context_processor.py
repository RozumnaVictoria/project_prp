from contacts.models import Contacts


def context(request):
    contacts = Contacts.objects.all()
    return {'contacts': contacts}
