from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Question



def paginate(objects, page, per_page=10):
    paginator = Paginator(objects, per_page)
    return paginator.get_page(page)

# Create your views here.
def index(request):
    questions = Question.objects.get_newest_questions()
    paginator = Paginator(questions, 10)
    page = request.GET.get('page')
    questions = paginator.get_page(page)
    return render(request, 'index.html', {'questions': questions})


def list_best_questions(request):
    questions = Question.objects.get_best_questions()
    paginator = Paginator(questions, 10)  
    page = request.GET.get('page')
    questions = paginator.get_page(page)
    return render(request, 'best_questions.html', {'questions': questions})


def list_questions_by_tag(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    questions = Question.objects.filter(tags=tag)
    paginator = Paginator(questions, 10)
    page = request.GET.get('page')
    questions = paginator.get_page(page)
    return render(request, 'questions_by_tag.html', {'questions': questions, 'tag': tag})


def question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    answers = question.answer_set.all()
    return render(request, 'question.html', {'question': question, 'answers': answers})


def ask(request):
    return render(request, "ask.html")

def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')

def settings(request):
    return render(request, 'settings.html')

def handler404(request, exception):
    return render(request, '404.html', status=404)