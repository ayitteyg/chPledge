from django.db import models
from django.contrib.auth.models import User
from import_export import resources
from django.db.models import Sum, F



# Create your models here.


class Register(models.Model):
     name = models.CharField(max_length=250, unique=True)
     contact = models.CharField(max_length=10)
     def __str__(self):
        return self.name

     def get_pledge(self):
        s = [k for k in Pledges.objects.filter(name_id=self.id).distinct()]
        sm = sum([i.pamount for i in s])
        return sm
     
     def get_total_rct(self):
        s = [k for k in Receipts.objects.filter(rname_id=self.id)]
        sm = sum([i.ramount for i in s])
        return sm

     def get_bal(self):
        return self.get_total_rct() -  self.get_pledge() 
     

     def get_payable(self):
        for k in Pledges.objects.filter(name_id=self.id):       
            return k.option


payable = (('weekly', 'weekly'),('monthly', 'monthly'),('periodic','periodic'))
class Pledges(models.Model):
    name = models.ForeignKey(Register, on_delete=models.CASCADE)
    pamount = models.FloatField (null=False)
    option = models.CharField(choices=payable, default='Weekly', max_length=10)
    pdate = models.DateField(null=False)
    fdate= models.DateField(null=False)
    
    def __int__(self):
        return self.pamount

    
    def getYear(self):
        yr = self.date.strftime('%Y')
        return yr



class Receipts(models.Model):
    user = models.CharField(max_length=100)
    rdate = models.DateField(null=False)
    rname = models.ForeignKey(Register, on_delete=models.CASCADE)
    ramount = models.FloatField (null=False)
    #def __str__(self):
     #   print(self.name)
       # return self.rname_id__name




