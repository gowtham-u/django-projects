from django.db import models

# Create your models here.
class Subject(models.Model):
    subject_info = models.CharField(max_length=255)

    def __str__(self):
        return self.subject_info


class Question(models.Model):
    serial_no = models.IntegerField()
    heading = models.CharField(max_length=255)
    definition = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.heading

class Answer(models.Model):
    related_text = models.CharField(max_length=255)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)

    def __str__(self):
        return self.related_text

