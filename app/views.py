from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator


QUESTIONS = [
        {
            'id':i,
            'title': f'Question {i}',
            'content': f'long ipsum {i}'
        } for i in range(100)

    ]

def paginate(objects, page, per_page=10):
    paginator = Paginator(objects, per_page)
    return paginator.get_page(page)

# Create your views here.
def index(request):
    page = request.GET.get('page', 1)
    questions = paginate(QUESTIONS, page)
    return render(request, 'index.html', {'questions': questions})

def question(request, question_id):
    item = QUESTIONS[question_id]
    return render(request, "question.html", {'question': item})


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