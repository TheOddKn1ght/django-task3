from django.db import models

class QuestionManager(models.Manager):
    def get_newest_questions(self):
        return self.order_by('-created_at')

    def get_best_questions(self):
        # TODO
        pass