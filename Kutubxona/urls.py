from django.contrib import admin
from django.urls import path
from Yangi_01.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('salom/<str:ism>/', salomlash),
    path('', bosh_sahifa),
    path('mashq/', mashq),
    path('talabalar/', talabalar),
    path('bitiruvchilar/', bitiruvchilar),
    path('talaba/<int:son>/', bitta_talaba),
    path('talaba_ochir/<int:son>/', talaba_ochir),
    path('kitob_ochir/<int:son>/', kitob_ochir),
    path('kitoblar/', kitoblar),
    path('mualliflar/', mualliflar),
    path('muallif/<int:son>/', bitta_muallif),
    path('kitob/<int:son>/', bitta_kitob),
    path('recordlar/', recordlar),
    path('tirik_mualliflar/', tirik_mualliflar),
    path('bitta_record/<int:son>/', tirik_mualliflar),
    path('muallif_ochir/<int:son>/', muallif_ochir),
    path('record_ochir/<int:son>/', record_ochir),

]
