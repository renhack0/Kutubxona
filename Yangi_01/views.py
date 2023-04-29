from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *


def salomlash(request, ism):
    return HttpResponse(f"<h1>Salom, {ism}!</h1>")

def bosh_sahifa(request):
    return render(request, 'home.html')

def mashq(request):
    content = {
        "kitoblar": ["Ufq", "qorqma", "Otgan kunlar", "Odamiylik mulki"],
        "ism": "Izzatullo"
    }
    return render(request, 'mashq.html', content)

def talabalar(request):
    soz = request.GET.get('qidiruv')
    if soz == "" or soz is None:
       content = {
         "students": Talaba.objects.all()
       }
    else:
        content = {
            "students": Talaba.objects.filter(ism__contains=soz)
        }
    return render(request, 'talabalar.html', content)

def bitiruvchilar(request):
    content = {
        "student": Talaba.objects.filter(kusrs__gt=3)
    }
    return render(request, 'bitiruvchilar.html', content)

def bitta_talaba(request, son):
    content = {
        "talaba": Talaba.objects.get(id=son)
    }
    return render(request, 'bitta_talaba.html', content)

def talaba_ochir(request, son):
    Talaba.objects.filter(id=son).delete()
    return redirect("/talabalar/")

def kitoblar(request):
    content = {
        "books": Talaba.objects.all()
    }
    return render(request, 'Kitoblar.html', content)

def kitob_ochir(request, son):
    Kitob.objects.filter(id=son).delete()
    return redirect("/kitoblar/")

def mualliflar(request):
    soz = request.GET.get('qidiruv')
    if soz == "" or soz is None:
     content = {
         "mualliflar": Muallif.objects.all()
     }
    else:
        content = {
            "students": Talaba.objects.filter(ism__contains=soz)
        }
    return render(request, '1_Mualliflar.html', content)

def bitta_muallif(request, son):
    content = {
        "muallif": Muallif.objects.get(id=son)
    }
    return render(request, 'bitta_muallif.html', content)

def bitta_kitob(request, son):
    content = {
        "kitob": Kitob.objects.get(id=son)
    }
    return render(request, 'bitta_kitob.html', content)

def recordlar(request):
    soz = request.GET.get('qidiruv')
    if soz == "" or soz is None:
     content = {
         "recordlar": Record.objects.all()
     }
    else:
        content = {
            "students": Talaba.objects.filter(ism__contains=soz)
        }
    return render(request, 'recordlar.html', content)

def tirik_mualliflar(request):
    content = {
        "muallif": Muallif.objects.filter(tirik=True)
    }
    return render(request, 'tirik_mualliflar.html', content)

def kitoblar(request):
    content = {
        "books": Talaba.objects.filter(janr="badiiy")
    }
    return render(request, 'Kitoblar.html', content)

def bitta_record(request, son):
    content = {
        "record": Record.objects.get(id=son)
    }
    return render(request, 'bitta_record.html', content)

def muallif_ochir(request, son):
    Muallif.objects.filter(id=son).delete()
    return redirect("/mualliflar/")

def record_ochir(request, son):
    Record.objects.filter(id=son).delete()
    return redirect("/recordlar/")




