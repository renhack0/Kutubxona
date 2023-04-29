from django.db import models

class Profil(models.Model):
    ism_fam = models.CharField(max_length=20)
    yosh = models.IntegerField(null=True)
    sana = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.ism_fam

class Kurs(models.Model):
    d = [
        ("Boshlang'ich", "Boshlang'ich"),
        ("O'rta", "O'rta"),
        ("Yuqori", "Yuqori")
         ]
    nom = models.CharField(max_length=10)
    daraja = models.CharField(max_length=12, choices=d)
    ustoz = models.CharField(max_length=20)
    narx = models.IntegerField()
    chegirma = models.IntegerField(default=0)
    def __str__(self):
        return self.nom
class Izoh(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    matn = models.CharField(max_length=100)
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE)
    sana = models.DateField()
    baho = models.IntegerField()
    # def __str__(self):
        # return f''

class Talangan(models.Model):
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE)
    prifile = models.ForeignKey(Profil, on_delete=models.CASCADE)
    # def __str__(self):
    #     return

class Xarid(models.Model):
    h = [
        ("Boshlandi", "Boshlandi"),
        ("Ko'rilyapti", "Ko'rilyapti"),
        ("Tugadi", "Tugadi")
         ]
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE)
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    sana = models.DateField()
    holat = models.CharField(max_length=11, choices=h)
    # def __str__(self):
    #     return
