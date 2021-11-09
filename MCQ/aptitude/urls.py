from django.urls import path
from aptitude.views import index, get_question_info

urlpatterns = [

    path('index/',index),
    path('<int:subject_id>',get_question_info)

]