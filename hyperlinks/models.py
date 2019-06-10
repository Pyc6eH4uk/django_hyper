from django.db import models


class Subject(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-title']


class Student(models.Model):
    mark = models.IntegerField()
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.surname} {self.subject.title}'


    class Meta:
        ordering = ['-id']
