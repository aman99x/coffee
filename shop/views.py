from django.shortcuts import render
from datetime import datetime
from shop.models import Contact
from django.core.mail import send_mail

def index(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == "POST":

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()

        send_mail(
            name,
            desc,
            'aman88sh@gmail.com',
            ['aman88sh@gmail.com'],
            fail_silently=False,
        )

    return render(request, 'index.html')