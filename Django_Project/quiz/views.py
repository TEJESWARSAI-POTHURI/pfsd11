
from django.shortcuts import render
from .models import Question, Choice

from django.http import HttpResponse

def quiz_view(request):
    questions = Question.objects.all()
    return render(request, 'quiz.html', {'questions': questions})




def result_view(request):
    if request.method == 'POST':
        score = 0
        for question in Question.objects.all():
            selected_choice_id = request.POST.get(str(question.id))
            if selected_choice_id:
                selected_choice = Choice.objects.get(pk=selected_choice_id)
                if selected_choice.is_correct:
                    score += 1
        return HttpResponse(f'Your score is: {score}')
    else:
        return HttpResponse('Method not allowed')
