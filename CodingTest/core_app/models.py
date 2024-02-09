from django.db import models
from django.utils.text import slugify
import os
from uuid import uuid4


def unique_slug(mdl, target_name):
    slug = slugify(target_name)

    check_slug = mdl.objects.filter(slug=slug).exists()
    count = 1
    while check_slug:
        count += 1
        slug = slugify(target_name) + '-' + str(count)
        check_slug = mdl.objects.filter(slug=slug).exists()
    return slug


def image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid4()}.{ext}'

    return os.path.join('uploads/images/', filename)


class QuestionTopic(models.Model):
    """Create specific topics (like Rhyming or Syllables)"""
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = unique_slug(QuestionTopic, self.name)
        super(QuestionTopic, self).save(*args, **kwargs)


class Question(models.Model):
    """For creating question"""
    ques_topic = models.ForeignKey(QuestionTopic, on_delete=models.SET_NULL, null=True, blank=True)
    ques = models.CharField(max_length=255)
    is_solved = models.BooleanField(default=False)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.ques

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = unique_slug(Question, self.ques)
        super(Question, self).save(*args, **kwargs)


class QuestionOptions(models.Model):
    """Creates question options. If every options contain an image, use image field, otherwise leave blank"""
    ques = models.ForeignKey(QuestionTopic, on_delete=models.CASCADE)
    option = models.CharField(max_length=255)
    image = models.ImageField(upload_to=image_path, null=True, blank=True)

    def __str__(self):
        return f'{self.ques} - {self.option}'


class QuestionImage(models.Model):
    """If the question contains a single image"""
    ques = models.ForeignKey(QuestionTopic, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_path, null=True, blank=True)

    def __str__(self):
        return f'{self.ques}'


class CorrectAnswer(models.Model):
    """Correct answer of a question"""
    ques = models.ForeignKey(QuestionTopic, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.ques} - {self.answer}'
