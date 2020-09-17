from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import Game
import datetime

def home(request):
    context = {
        'title': 'home'
    }
    return render(request, 'home.html', context)

def question1(request):
    context = {
        'title':'question1'
    }
    if request.method == 'POST':
        name = request.POST['name']
        game = Game(player=name)
        game.save()
        request.session['game_id'] = game.id
        return HttpResponseRedirect(reverse('question2'))
    else:
        return render(request,'question1.html',context)

def question2(request):
    context = {
        'title':'question2'
    }
    if request.method == 'POST':
        game_id = request.session['game_id']
        answer1 = request.POST['answer1']
        game = Game.objects.get(pk=game_id)
        game.answer1 = answer1
        game.save()
        return HttpResponseRedirect(reverse('question3'))
    else:
        return render(request,'question2.html',context)

def question3(request):
    context = {
        'title':'question3'
    }
    if request.method == 'POST':
        game_id = request.session['game_id']
        answers2 = request.POST.getlist('answers2')
        game = Game.objects.get(pk=game_id)
        game.answers2 = str(answers2)
        print("Answers2:",answers2)
        game.timestamp = datetime.datetime.now()
        game.save()
        return HttpResponseRedirect(reverse('summary'))
    else:
        return render(request,'question3.html',context)

def summary(request):
    game_id = request.session['game_id']
    del request.session['game_id']
    game = Game.objects.get(pk=game_id)
    context = {
        'title' : 'summary',
        'game' : game
    }
    return render(request,'summary.html',context)

def history(request):
    games = Game.objects.all()
    context = {
        'title' : 'history',
        'games' : games
    }
    return render(request,'history.html',context)