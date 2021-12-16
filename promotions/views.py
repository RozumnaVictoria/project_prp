from django.shortcuts import render, redirect
from promotions.models import Promotions


def promotionsList(request):
    if not request.user.is_authenticated:
        return redirect('users:login')
    return render(request, 'promotions.html', {'prom_list': Promotions.objects.all()})
