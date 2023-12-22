from django.db import models

# Create your models here.
class tag(models.Model):
    tag_name = models.CharField(unique=True,max_length=100)

    def __str__(self):
        return self.tag_name

class TodoDetails(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100,null=False)
    description = models.CharField(max_length=1000,null=False)
    due_date=models.DateField(null=True)
    tag = models.ManyToManyField(tag,blank=True)
    status = models.CharField(max_length=10,choices=(('OPEN','Open'),('WORKING','Working'),('DONE','Done'),('OVERDUE','Overdue')),default='OPEN',null=False)

    def __str__(self):
        return self.title