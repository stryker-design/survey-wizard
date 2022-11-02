
import uuid
from django.shortcuts import render
from django.db import transaction
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.forms.formsets import formset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from django.views.decorators.http import require_http_methods


from ..models import Option, Survey, Question, Answer, Submission
from ..forms import SurveyForm, QuestionForm, OptionForm, AnswerForm, BaseAnswerFormSet

# Create your views here.

@login_required
def survey_list(request):
    """User can view all their surveys"""
    surveys = Survey.objects.filter(creator=request.user).order_by("-created_at").all()
    return render(request, "survey/list.html", {"surveys": surveys})


@login_required
def detail(request, uuid):
    """User can view an active survey"""
    try:
        survey = Survey.objects.prefetch_related("question_set__option_set").get(
            uuid=uuid, creator=request.user, is_active=True
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
    public_path = reverse("survey-start", args=[uuid])
    public_url = f"{request.scheme}://{host}{public_path}"
    num_submissions = survey.submission_set.filter(is_complete=True).count()
    return render(
        request,
        "survey/detail.html",
        {
            "survey": survey,
            "public_url": public_url,
            "questions": questions,
            "num_submissions": num_submissions,
        },
    )


@login_required
def create(request):
    """User can create a new survey"""
    # survey_query = Survey.objects.get(uuid=survey)
    if request.method == "POST":
        form = SurveyForm(request.POST)
        if form.is_valid():
            survey = form.save(commit=False)
            survey.creator = request.user
            survey.save()
            return redirect("survey-question-create", uuid=survey.uuid)
    else:
        form = SurveyForm()

    return render(request, "survey/create.html", {"form": form})



# DELETE SURVEYS

@login_required
def delete(request, uuid):
    """User can delete an existing survey"""
    survey = get_object_or_404(Survey, uuid=uuid, creator=request.user)
    if request.method == "POST":
        survey.delete()

    return redirect("dashboard")



@login_required
def edit(request, uuid):
    """User can add questions to a draft survey, then acitvate the survey"""
    
    try:
        survey = Survey.objects.prefetch_related("question_set__option_set").get(
            uuid=uuid, creator=request.user, is_active=False
        )
      
    except Survey.DoesNotExist:
        raise Http404()

    if request.method == "POST":
        survey.is_active = True
        
        survey.save()
        return redirect("survey-detail", uuid=uuid)
    else:
       

        questions = survey.question_set.all()
        return render(request, "survey/edit.html", {"survey": survey, "questions": questions})


@login_required
def question_create(request, uuid):
    """User can add a question to a draft survey"""
    survey = get_object_or_404(Survey, uuid=uuid, creator=request.user)
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.survey = survey
            question.save()
            return redirect("survey-option-create", survey_uuid=survey.uuid, question_uuid=question.uuid)
    else:
        form = QuestionForm()

    return render(request, "survey/question.html", {"survey": survey, "form": form})


@require_http_methods(("POST",))
def question_delete(request, uuid):
    # question = get_object_or_404(Question, uuid=uuid)    
    question = Question.objects.get(uuid=uuid)
    question.delete()

    return redirect("survey-edit", uuid=question.survey.uuid) 



@login_required
def option_create(request, survey_uuid, question_uuid):
    """User can add options to a survey question"""
    survey = get_object_or_404(Survey, uuid=survey_uuid, creator=request.user)
    question = Question.objects.get(uuid=question_uuid)

    if question.type == 'Checked box':
        form = OptionForm()
        survey = get_object_or_404(Survey, uuid=survey_uuid, creator=request.user)
        question = Question.objects.get(uuid=question_uuid)
        options = question.option_set.all()
        uuid = question_uuid
        return redirect('survey-option-create-checked', survey_uuid=survey.uuid, question_uuid=question.uuid )


    if request.method == "POST":
        form = OptionForm(request.POST)
        if form.is_valid():
            option = form.save(commit=False)
            option.question = question

            option.question_uuid = question_uuid
            option.save()
    else:
        form = OptionForm()
        
    options = question.option_set.all()
    return render(
        request,
        "survey/options.html",
        {"survey": survey, "question": question, "options": options, "form": form},
    )


@login_required
def option_create_checked(request, question_uuid, survey_uuid):
    survey = get_object_or_404(Survey, uuid=survey_uuid, creator=request.user)
    question = Question.objects.get(uuid=question_uuid)

    if request.method == "POST":
        form = OptionForm(request.POST)
        if form.is_valid():
            option = form.save(commit=False)
            option.question = question
            option.question_uuid = question_uuid
            option.save()
    else:
        form = OptionForm()
        
    options = question.option_set.all()
   
    return render(request,"survey/options-checked.html", {"survey": survey, "question": question, "options": options, "form": form})


def start(request, pk):
    """Survey-taker can start a survey"""
    survey = get_object_or_404(Survey, pk=pk, is_active=True)
    if request.method == "POST":
        sub = Submission.objects.create(survey=survey)
        return redirect("survey-submit", survey_pk=pk, sub_pk=sub.pk)

    return render(request, "survey/start.html", {"survey": survey})


def submit(request, survey_pk, sub_pk):
    """Survey-taker submit their completed survey."""

    try:
        survey = Survey.objects.prefetch_related("question_set__option_set").get(
            pk=survey_pk, is_active=True
        )
    except Survey.DoesNotExist:
        raise Http404()

    try:
        sub = survey.submission_set.get(pk=sub_pk, is_complete=False)
    except Submission.DoesNotExist:
        raise Http404()

    
    

    # if question.type == 'Checked box':
    
    #     return redirect('submit', survey_uuid=survey.uuid)


    questions = survey.question_set.all()
    options = [q.option_set.all() for q in questions]
    form_kwargs = {"empty_permitted": False, "options": options}
    AnswerFormSet = formset_factory(AnswerForm, extra=len(questions), formset=BaseAnswerFormSet)
    if request.method == "POST":
        formset = AnswerFormSet(request.POST, form_kwargs=form_kwargs)
        if formset.is_valid():
            with transaction.atomic():
                for form in formset:
                    Answer.objects.create(
                        option_id=form.cleaned_data["option"], submission_id=sub_pk,
                    )

                sub.is_complete = True
                sub.save()
            return redirect("survey-thanks", pk=survey_pk)

    else:
        formset = AnswerFormSet(form_kwargs=form_kwargs)

    question_forms = zip(questions, formset)
    return render(
        request,
        "survey/submit.html",
        {"survey": survey, "question_forms": question_forms, "formset": formset},
    )


def thanks(request, pk):
    """Survey-taker receives a thank-you message."""
    survey = get_object_or_404(Survey, pk=pk, is_active=True)
    return render(request, "survey/thanks.html", {"survey": survey})






