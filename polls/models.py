from django.db import models

# Create your models here.

class Ip(models.Model):
    ip = models.IPAddressField()
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.ip

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    #...
    def __str__(self):
        return self.question

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    ip = models.ManyToManyField(Ip, blank=True)

    #...
    def __str__(self):
        return self.choice_text
