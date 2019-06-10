from django.db import models

MARKS = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5)
)


class Subject(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Student(models.Model):
    mark = models.IntegerField()
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

