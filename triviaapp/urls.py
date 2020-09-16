from django.urls import path
from .views import home, question1, question2, question3, summary, history

urlpatterns = [
    path('',home,name='home'),
    path('question1/', question1,name='question1'),
    path('question2/',question2,name='question2'),
    path('question3/',question3,name='question3'),
    path('summary/',summary,name='summary'),
    path('history/',history,name='history')
]
