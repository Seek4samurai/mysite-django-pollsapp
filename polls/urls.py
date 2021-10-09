from django.urls import path
from django.urls.conf import include
from . import views

app_name = "polls"
urlpatterns = [
    # ex: /polls
    path('', views.index, name='index'),
    # ex: /polls/10
    path('<int:question_id>/', views.details, name='details'),
    # ex: /polls/10/results
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/10/vote
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
