from django.shortcuts import render, redirect
from contacts.models import Contacts


def contactList(request):
    if not request.user.is_authenticated:
        return redirect('users:login')
    return render(request, 'delivery.html', {'contact_list': Contacts.objects.all()})
