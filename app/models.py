from django.db import models
# Create your models here.
class Report(models.Model):
    REPORT_TYPES=[
        ("report","Report Page"),
        ("scam","Scam Page"),
        ("somethingelse","SomethingElse Page"),
        ("aboutus","About Us Page")
    ]
    name=models.TextField(default="Unknown")
    email=models.EmailField( max_length=254,default="@gmail.com")
    message=models.TextField(default="Nothing")
    select=models.CharField(default="Bug")
    date1= models.DateTimeField(auto_now=True)
    date2=models.DateField (null=True,blank=True)
    source=models.CharField(max_length=100,choices=REPORT_TYPES,default="Unknown Page")
    platform=models.CharField(max_length=50,default="Whatsapp")
    amount=models.IntegerField(default=12344)



    