from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone
from autoslug import AutoSlugField

sems=(("1-1","1-1"),("1-2","1-2"),("2-1","2-1"),("2-2","2-2"),("3-1","3-1"),("3-2","3-2"),("4-1","4-1"),("4-2","4-2"))

class Student(models.Model):
    HallTicketNo=models.CharField(max_length=225,unique=True)
    name=models.CharField(max_length=225)
    dob=models.DateField(("Date"))
    age=models.IntegerField()
    address=models.TextField(max_length=225)
    branchName=models.ForeignKey("Branches",on_delete=models.CASCADE,default=2)

    def __str__(self):
        return self.HallTicketNo

class Results(models.Model):
    HallTicketNo=models.ForeignKey("Student",on_delete=models.CASCADE,null=True,related_name='results')
    sem=models.CharField(max_length=225,choices=sems,default="I-I")
    branch=models.ForeignKey("Branches",on_delete=models.CASCADE)
    subjectCode=models.ForeignKey("Subjects",on_delete=models.CASCADE,null=True)
    internal=models.IntegerField(default=21)
    external=models.IntegerField(default=35)
    @property
    def total(self):
        if self.internal is not None and self.external is not None:
            return self.internal + self.external
    postingDate=models.DateField(default=date.today)

    def __str__(self):
        return self.HallTicketNo


class Branches(models.Model):
    branchName=models.CharField(max_length=225)
    branchCode=models.IntegerField()
    creationDate=models.DateField(default=date.today)

    def __str__(self):
        return self.branchName


class Subjects(models.Model):
    subjectName=models.CharField(max_length=225)
    subjectCode=models.IntegerField()
    creationDate=models.DateField(default=date.today)

    def __str__(self):
        return self.subjectName

class Notices(models.Model):
    noticeTitle=models.CharField(max_length=225)
    noticeDetails=models.TextField()
    creationDate=models.DateField(default=date.today)

    def __str__(self):
        return self.noticeTitle

sems=(("1-1","1-1"),("1-2","1-2"),("2-1","2-1"),("2-2","2-2"),("3-1","3-1"),("3-2","3-2"),("4-1","4-1"),("4-2","4-2"))

class SubjectCombination(models.Model):
    branchCode=models.ForeignKey("Branches",on_delete=models.CASCADE)
    subjectsCode=models.ForeignKey("Subjects",on_delete=models.CASCADE)
    sem=models.CharField(max_length=225,choices=sems,default="I-I")
    creationDate=models.DateField(default=date.today)

    def __str__(self):
        return self.sem




sems=(("1-1","1-1"),("1-2","1-2"),("2-1","2-1"),("2-2","2-2"),("3-1","3-1"),("3-2","3-2"),("4-1","4-1"),("4-2","4-2"))

class GetResult(models.Model):
    HallTicketNo=models.CharField(max_length=225)
    sem=models.CharField(max_length=225,choices=sems,default="I-I")

class GetResults(models.Model):
    HallTicketNo=models.CharField(max_length=225)
    sem=models.CharField(max_length=225,choices=sems,default="I-I")
    def __str__(self):
        return self.HallTicketNo
    slug=AutoSlugField(populate_from='HallTicketNo',unique=True,null=True,default=None)

class newmodel(models.Model):
    column=models.CharField(max_length=225)