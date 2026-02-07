from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Greeting

def birthday_view(request, id):
    greeting = get_object_or_404(Greeting, id=id)

    # 🔴 Track click
    greeting.viewed = True
    greeting.view_count += 1
    greeting.last_viewed_at = timezone.now()
    greeting.save()

    return render(request, 'greeting.html', {'greeting': greeting})

def home_view(request):
    greeting = Greeting.objects.first()  # get first greeting
    return render(request, 'home.html', {'greeting': greeting})

def love(request):
    greeting = Greeting.objects.first()
    return render(request, 'love.html',{'greetin': greeting})