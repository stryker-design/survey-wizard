from email.policy import default
from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

import uuid


class Survey(models.Model):
    """A survey created by a user."""

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=64)
    is_active = models.BooleanField(default=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)


class Question(models.Model):

    MULTIPLE_CHOICE = 'Multiple choice'
    CHECKED_BOX = 'Checked box'
    COMMENT_BOX = 'Comment box'
    
    QUESTION_TYPE = [
    (MULTIPLE_CHOICE, 'Multiple choice'),
    (CHECKED_BOX, 'Checked box'),
    (COMMENT_BOX,'Comment box'),
    ]

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    prompt = models.CharField(max_length=128)
    type = models.CharField(max_length=15, choices=QUESTION_TYPE, default= MULTIPLE_CHOICE)

    


class Option(models.Model):
    """A multi-choice option available as a part of a survey question."""

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    

    # Change name to comment box on next migrate
    text = models.CharField(max_length=128)


    def __str__(self):
        return f'{self.text}'

    


# class CommentBox(models.Model):
    """A comment box for open ended questions"""

    # question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # comment = models.CharField(max_length=1000)


class Submission(models.Model):
    """A set of answers a survey's questions."""

    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    is_complete = models.BooleanField(default=False)


class Answer(models.Model):
    """An answer a survey's questions."""

    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)

    
    
    """
    Adding comment box -- delete if you get rid of commentbox model
    or change foreign key to option if you choose to go with option model
    for comment
     """
    
    # comment = models.ForeignKey(CommentBox, on_delete=models.CASCADE)
    
