

from unicodedata import name
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.db import transaction
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.forms.formsets import formset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from django.conf import settings

from requests import options

from ..models import Survey, Question, Answer, Submission
from ..forms import SurveyForm, QuestionForm, OptionForm, AnswerForm, BaseAnswerFormSet

@login_required(redirect_field_name='login')
def dashboard_view(request):
    # Build an error you must be logged in page to redirect to
    # if not request.user.is_authenticated:
    #     return redirect('login')

    surveys = Survey.objects.filter(creator=request.user).order_by("-created_at").all()


    def delete(request, pk):
        survey = get_object_or_404(Survey, pk=pk, creator=request.user)
        if request.method == "POST":
            survey.delete()
            return redirect('dashboard')
        
    context = {'surveys': surveys}
    return render(request, 'dashboard_templates/dashboard.html', context)


@login_required
def results(request, pk):
    try:
        survey = Survey.objects.prefetch_related("question_set__option_set").get(
            pk=pk, creator=request.user, is_active=True
        )
    except Survey.DoesNotExist:
        raise Http404()

    questions = survey.question_set.all()

    # Calculate the results.
    # This is a naive implementation and it could be optimised to hit the database less.
    # See here for more info on how you might improve this code: https://docs.djangoproject.com/en/3.1/topics/db/aggregation/
    for question in questions:
        option_pks = question.option_set.values_list("pk", flat=True)
        total_answers = Answer.objects.filter(option_id__in=option_pks).count()
        for option in question.option_set.all():
            num_answers = Answer.objects.filter(option=option).count()
            option.percent = 100.0 * num_answers / total_answers if total_answers else 0

    host = request.get_host()
    public_path = reverse("survey-start", args=[pk])
    public_url = f"{request.scheme}://{host}{public_path}"
    num_submissions = survey.submission_set.filter(is_complete=True).count()
    return render(
        request,
        "dashboard_templates/results.html",
        {
            "survey": survey,
            "public_url": public_url,
            "questions": questions,
            "num_submissions": num_submissions,
        },
    )

    # return render(request, 'dashboar_templates/results.html')

