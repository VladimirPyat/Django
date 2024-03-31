from django.shortcuts import render
from django.http import HttpResponse
import logging

logger=logging.getLogger(__name__)


def index(request):
    html_head = 'Главная страница'
    html_text = f' <h2>  {html_head} </h2>' \
                f'<p>Это главная страница учебного проекта</p>' \
                f'<p>Пока тут ничего нет</p>'

    logger.info(f'new visit -  {html_head}')
    return HttpResponse(html_text)


def about(request):
    html_head='Обо мне'
    html_text = f' <h2> {html_head} </h2>' \
                f'<p>Я изучаю язык программирования Python, фреймворк  Django</p>' \

    logger.info(f'new visit -  {html_head}')
    return HttpResponse(html_text)


