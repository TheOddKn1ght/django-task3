from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class QuestionManager(models.Manager):
    def get_newest_questions(self):
        return self.order_by('-created_at')

    def get_best_questions(self):
        return self.annotate(num_likes=models.Count('like')).order_by('-num_likes')
        




class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Question(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = QuestionManager()

class Answer(models.Model):
    content = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Like(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)