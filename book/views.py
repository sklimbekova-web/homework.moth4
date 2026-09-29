from django.shortcuts import render
from django.http import HttpResponse

def my_favourite_writer_view(request):
        return HttpResponse('<h1>Мой любимый писатель<h1><p>Мой любимый писатель - Лев Толстой.<p>')


def facts_about_writer_view(request):
        return HttpResponse('<h1>Факты о писателе<h1><p>28 августа 1828 года, а его литературное наследие составляет огромное собрание сочинений объемом около 90 томов.<p>')


def my_opinion_about_writer_view(request):
        return HttpResponse('<h1>Мое мнение<h1>Я думаю он реальный русский лев как его имя<p>')