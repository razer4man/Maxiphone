from django.shortcuts import render
from .models import Benefit
from .models import Benefit_add
from .models import Connection_step

def mainpage(request):
    benefits = Benefit.objects.filter().order_by()
    benefit_adds = Benefit_add.objects.filter().order_by()
    connection_steps = Connection_step.objects.filter().order_by()
    return render(request, 'mainpage/mainpage.html', {'benefits': benefits, 'benefit_adds': benefit_adds, 'connection_steps': connection_steps})
