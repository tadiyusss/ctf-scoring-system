from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from .forms import *
from .models import *
import json

CONFIG = json.load(open("config.json"))

def register(request):
    if CONFIG['ALLOW_REGISTRATION'] == False:
        return HttpResponse("Registration is disabled")
    
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            team_name = form.cleaned_data["team_name"]
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            if User.objects.filter(username=username).exists():
                messages.error(request, "Username is already taken")
                return redirect("register")
            
            user = User.objects.create_user(username=username, password=password, first_name=team_name)
            user.save()
            log = Log(user=user, action=f"{team_name} joined the party.", ip_address=request.META.get("REMOTE_ADDR"))
            log.save()
            messages.success(request, "Account created successfully")
            return redirect("login")
        else:
            messages.error(request, "Unable to create account")
            return redirect("register")

    context = {
        "form": form,
    }
    return render(request, "authentication/register.html", context)

def user_login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("dashboard")
            else:
                messages.error(request, "Invalid username or password")
                return redirect("login")
        else:
            messages.error(request, "Invalid username or password")
            return redirect("login")
    
    context = {
        "form": form,
        "CONFIG": CONFIG,
    }
    return render(request, "authentication/login.html", context)


@login_required(login_url="login")
def dashboard(request):

    users = User.objects.all()
    for user in users:
        user.score = 0
        user.flags = 0
        last_solved = Solved.objects.filter(user=user).order_by("-timestamp").first()
        if last_solved:
            user.last_solved_time = last_solved.timestamp.strftime("%I:%M %p")
        else:
            user.last_solved_time = "N/A"
        solved = Solved.objects.filter(user=user)
        for s in solved:
            user.score += s.question.level.points
            user.flags += 1
    users = sorted(users, key=lambda x: x.score, reverse=True)
    [setattr(user, "rank", i+1) for i, user in enumerate(users)]
    answered = Solved.objects.filter(user=request.user)
    questions = Question.objects.all()
    context = { 
        "answered": answered,
        "questions": questions,
        "progress": int((len(answered) / len(questions)) * 100),
        "users" : users,
    }
    return render(request, "dashboard/home.html", context)

@login_required(login_url="login")
def flags(request):
    levels = Level.objects.all()
    submit_form = SubmitFlagForm()
    selected_level = request.GET.get("level")

    if request.method == "POST":
        submit_form = SubmitFlagForm(request.POST)
        if submit_form.is_valid():
            flag = submit_form.cleaned_data["flag"]
            question_id = request.POST.get("question_id")
            question = get_object_or_404(Question, pk=question_id)
            if question.answer == flag:
                if not Solved.objects.filter(user=request.user, question=question).exists():
                    solved = Solved(user=request.user, question=question, ip_address=request.META.get("REMOTE_ADDR"))
                    solved.save()
                    log = Log(user=request.user, action=f"{request.user.first_name} solved a flag.", ip_address=request.META.get("REMOTE_ADDR"))
                    log.save()
                    messages.success(request, "Correct flag")
                else:    
                    messages.error(request, "Flag already submitted")
            else:
                submission = Submission(user=request.user, flag=flag, ip_address=request.META.get("REMOTE_ADDR"))
                submission.save()
                messages.error(request, "Incorrect flag")
        submit_form = SubmitFlagForm()
    if selected_level:
        selected_level = get_object_or_404(Level, name=selected_level)
        questions = Question.objects.filter(level__name=selected_level)
    else:
        questions = Question.objects.all().order_by('level')
        selected_level = Level.objects.all()

    for question in questions:
        question.answered = Solved.objects.filter(user=request.user, question=question).exists()
    

    context = {
        "levels": levels,
        "selected_level": selected_level,
        "questions": questions,
        "submit_form": submit_form,
    }
    return render(request, "dashboard/flags.html", context)

def leaderboard_data(request):
    users = User.objects.all()
    logs = Log.objects.all()
    for user in users:
        user.score = 0
        user.flags = 0
        last_solved = Solved.objects.filter(user=user).order_by("-timestamp").first()
        if last_solved:
            user.last_solved_time = last_solved.timestamp.strftime("%I:%M %p")
        else:
            user.last_solved_time = "N/A"
        solved = Solved.objects.filter(user=user)
        for s in solved:
            user.score += s.question.level.points
            user.flags += 1
    users = sorted(users, key=lambda x: x.score, reverse=True)
    [setattr(user, "rank", i+1) for i, user in enumerate(users)]

    data = {
        "users": [{"first_name": user.first_name, "score": user.score, "flags": user.flags, "rank": user.rank, "last_solved_time": user.last_solved_time} for user in users],
        "logs": [{"user": log.user.username, "action": log.action, "timestamp": log.timestamp.strftime("%I:%M %p")} for log in logs],
    }

    return JsonResponse(data)

def leaderboard(request):
    users = User.objects.all()
    logs = Log.objects.all()
    for user in users:
        user.score = 0
        user.flags = 0
        last_solved = Solved.objects.filter(user=user).order_by("-timestamp").first()
        if last_solved:
            user.last_solved_time = last_solved.timestamp.strftime("%I:%M %p")
        else:
            user.last_solved_time = "N/A"
        solved = Solved.objects.filter(user=user)
        for s in solved:
            user.score += s.question.level.points
            user.flags += 1
    users = sorted(users, key=lambda x: x.score, reverse=True)
    [setattr(user, "rank", i+1) for i, user in enumerate(users)]
    context = {
        "users": users,
    }
    return render(request, "leaderboard.html", context)

def logout_user(request):
    logout(request)
    return redirect("login")
