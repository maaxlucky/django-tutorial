import datetime

from django.db.models import F
from django.db.models.functions import Now
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Question, Choice


class IndexView(generic.ListView):
    # model = Question
    # queryset = Question.objects.filter(pub_date__lte=Now())
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        # return super().get_queryset().filter(pub_date__lte=Now(), choice__isnull=False).distinct()
        return Question.objects.filter(pub_date__lte=timezone.now(), choice__isnull=False).distinct()



# clarify CBV vs FBV

# def index(request):
#     latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
#     context = {
#         'latest_question_list': latest_question_list
#     }
#
#     return render(request, 'polls/index.html', context)
#

class DetailView(generic.DetailView):
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now(), choice__isnull=False).distinct()


class ResultsView(generic.DetailView):
    template_name = 'polls/results.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now(), choice__isnull=False).distinct()


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if question.choice_set.filter(question__pub_date__lte=Now(), question__choice__isnull=False):
        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            return render(
                request,
                'polls/detail.html',
                {
                    'question': question,
                    'error_message': "You didn't select a choice.",
                },
            )
        else:
            selected_choice.votes = F('votes') + 1
            selected_choice.save()
            selected_choice.refresh_from_db()
            # CLARIFY
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
    else:
        return HttpResponse('You cant refer this question')