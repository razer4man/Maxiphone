from django.shortcuts import render
from .models import Benefit

# Create your views here.
def mainpage(request):
    benefits = Benefit.objects.filter().order_by()
    Benefit_adds = Benefit.objects.filter().order_by()
    return render(request, 'mainpage/mainpage.html', {'benefits': benefits, 'benefit_adds': benefit_adds})
