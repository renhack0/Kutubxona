from django.db import models

class Talaba(models.Model):
    ism = models.CharField(max_length=20)
    kitoblar_soni = models.IntegerField()
    kusrs = models.SmallIntegerField()
    def __str__(self):
        return self.ism

class Muallif(models.Model):
    j = [
        ('Ayol', 'Ayol',),
        ('Ekak', 'Erkak',),
        ('Berilmagan', 'Berilmagan')
    ]
    ism = models.CharField(max_length=20)
    kitoblar_soni = models.SmallIntegerField()
    jins = models.CharField(max_length=10, choices=j)
    tirik = models.BooleanField()
    tugilgan_yili = models.DateField()
    def __str__(self):
        return self.ism
class Kitob(models.Model):
    nom = models.CharField(max_length=20)
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)
    sahifa = models.IntegerField()
    janr = models.CharField(max_length=10)
    def __str__(self):
        return self.nom
class Admin(models.Model):
    ism = models.CharField(max_length=10)
    ish_vaqti = models.TimeField()
    def __str__(self):
        return self.ism
class Record(models.Model):
    talaba = models.ForeignKey(Talaba, on_delete=models.CASCADE)
    kitob = models.ForeignKey(Kitob, on_delete=models.CASCADE)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    olingan_sana = models.DateField()
    qaytarilish_sana = models.DateField()
    qaytarildi = models.BooleanField()

class Foydalanuvchi(models.Model):
    username = models.CharField(max_length=10)
    login = models.CharField(max_length=20)
    parol = models.CharField(max_length=8)
    email = models.EmailField(max_length=20)
    talaba = models.BooleanField()
    rasm = models.ImageField()
    def __str__(self):
        return self.username

class Mahsulot(models.Model):
    nom = models.CharField(max_length=10)
    brend = models.CharField(max_length=10)
    narx = models.IntegerField()
    davlat = models.CharField(max_length=10)
    mavjud = models.BooleanField()
    def __str__(self):
        return self.nom

class Kurs(models.Model):
    nom = models.CharField(max_length=10)
    daraja = models.IntegerField()
    yonalish = models.CharField(max_length=10)
    davomiylik = models.IntegerField()

# class Nashriyot(models.Model):
#     nom = models.CharField(max_length=10)
#     manzil = models.CharField(max_length=20)
#     def __str__(self):
#         return self.nom
# class Kitob(models.Model):
#     nom = models.CharField(max_length=10)
#     narx = models.IntegerField()
#     kelgan_sana = models.DateField()
#     nashriyot = models.ForeignKey(Nashriyot, on_delete=models.CASCADE)
#     def __str__(self):
#         return self.nom
# class Sotuvchi(models.Model):
#     ism = models.CharField(max_length=20)
#     tel = models.IntegerField()
#     def __str__(self):
#         return self.ism
# class Sotuv(models.Model):
#     kitob = models.ForeignKey(Kitob, on_delete=models.CASCADE)
#     sotuvchi = models.ForeignKey(Sotuvchi, on_delete=models.CASCADE)
#     sana = models.DateField()

