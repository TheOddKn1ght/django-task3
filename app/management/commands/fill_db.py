from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from your_app.models import Question, Answer, Tag, Like, Profile
from faker import Faker
import random

fake = Faker()

class Command(BaseCommand):
    help = 'Fill the database with test data'

    def add_arguments(self, parser):
        parser.add_argument('ratio', type=int, help='Fill ratio')

    def handle(self, *args, **kwargs):
        ratio = kwargs['ratio']

        
        users = []
        for _ in range(ratio):
            user = User.objects.create_user(username=fake.user_name(), email=fake.email(), password=fake.password())
            users.append(user)

        
        tags = [Tag.objects.create(name=fake.word()) for _ in range(ratio)]

        
        for _ in range(ratio * 10):
            question = Question.objects.create(title=fake.sentence(), content=fake.paragraph(), user=random.choice(users))
            question.tags.set(random.sample(tags, random.randint(1, ratio)))

            for _ in range(ratio * 100):
                answer = Answer.objects.create(content=fake.paragraph(), question=question, user=random.choice(users))

                for _ in range(ratio * 200):
                    Like.objects.create(user=random.choice(users), question=question, answer=answer)

        
        for user in users:
            Profile.objects.create(user=user, avatar=fake.image_url())