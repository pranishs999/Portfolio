import logging
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from .forms import ContactForm, ExperienceForm, TrainingForm, AchievementForm
from .models import Experience, Training, Achievement

logger = logging.getLogger(__name__)


def home(request):
    context = {
        "skills": [
            {"name": "Python", "level": 90},
            {"name": "Django", "level": 85},
            {"name": "Flask", "level": 80},
            {"name": "HTML & CSS", "level": 90},
            {"name": "Tailwind CSS", "level": 85},
            {"name": "SQL / Database", "level": 75},
            {"name": "C / C++", "level": 70},
            {"name": "Graphics Design", "level": 60},
        ],
        "projects": [
            {"title": "Portfolio", "desc": "Personal portfolio website showcasing projects, skills, and experience.", "tags": ["Web", "Frontend"], "link": "https://github.com/pranishs999/Portfolio"},
            {"title": "Library Management System", "desc": "Comprehensive LMS allowing management of books, users, and borrow records.", "tags": ["Django", "LMS"], "link": "https://github.com/pranishs999/Library_Management_system-LMS"},
            {"title": "Weather App", "desc": "Web-based weather application built with Django. Fetches real-time data and displays accurate forecasts.", "tags": ["Django"], "link": "https://github.com/pranishs999/Weather-app"},
            {"title": "Simple Calculator CLI", "desc": "A clean command-line calculator handling core arithmetic operations with input validation.", "tags": ["Python CLI"], "link": "https://github.com/pranishs999/Simple-Calculator-CLI"},
            {"title": "To-Do App CLI", "desc": "Command-line task manager for adding, listing, and completing daily tasks with persistent storage.", "tags": ["Python CLI"], "link": "https://github.com/pranishs999/To-Do-App-CLI"},
            {"title": "GradeBook CLI", "desc": "A robust CLI based gradebook system to manage student records, grades, and data using file handling.", "tags": ["Python CLI"], "link": "https://github.com/pranishs999/GradeBook-CLI"},
            {"title": "Ollama Dashboard", "desc": "Dashboard interface for interacting with locally-hosted Ollama LLM models.", "tags": ["LLM", "Dashboard"], "link": "https://github.com/pranishs999/ollama_dashboard"},
            {"title": "AVA", "desc": "An AI virtual assistant experiment exploring conversational interaction and task automation.", "tags": ["AI", "Python"], "link": "https://github.com/pranishs999/AVA"},
            {"title": "Copy Submission Recorder", "desc": "A utility for tracking and recording student copy/assignment submissions.", "tags": ["Python", "Education"], "link": "https://github.com/pranishs999/Copy_sumibtion_recorder"},
            {"title": "Voice Python", "desc": "Voice-enabled Python project exploring speech recognition and audio-driven control.", "tags": ["Python", "Voice"], "link": "https://github.com/pranishs999/voic-epython"},
            {"title": "Plan Manager", "desc": "A planning and scheduling tool for organizing tasks, goals, and personal workflows.", "tags": ["Python", "Productivity"], "link": "https://github.com/pranishs999/plan-manager"},
            {"title": "Voice", "desc": "Experiment exploring voice input, audio processing, and speech-driven interfaces.", "tags": ["Python", "Voice"], "link": "https://github.com/pranishs999/voice"},
        ],
        "experience": Experience.objects.all(),
        "education": [
            {"degree": "BSc. CSIT", "school": "Hetauda City College", "period": "Dec 2024 - Present"},
            {"degree": "SLC (+2) Science", "school": "New Capital College, Tandi", "period": "2020 - 2022"},
        ],
        "hackathons": Achievement.objects.all(),
        "certifications": Training.objects.all(),
    }
    return render(request, "main/home.html", context)


@login_required
def dashboard(request):
    if request.method == "POST":
        form_type = request.POST.get("form_type")

        if form_type == "experience":
            form = ExperienceForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Experience added successfully!")
                return redirect("main:dashboard")

        elif form_type == "training":
            form = TrainingForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Training added successfully!")
                return redirect("main:dashboard")

        elif form_type == "achievement":
            form = AchievementForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Achievement added successfully!")
                return redirect("main:dashboard")

        elif form_type == "delete_experience":
            item_id = request.POST.get("item_id")
            Experience.objects.filter(id=item_id).delete()
            messages.success(request, "Experience deleted.")
            return redirect("main:dashboard")

        elif form_type == "delete_training":
            item_id = request.POST.get("item_id")
            Training.objects.filter(id=item_id).delete()
            messages.success(request, "Training deleted.")
            return redirect("main:dashboard")

        elif form_type == "delete_achievement":
            item_id = request.POST.get("item_id")
            Achievement.objects.filter(id=item_id).delete()
            messages.success(request, "Achievement deleted.")
            return redirect("main:dashboard")

    context = {
        "experience_form": ExperienceForm(),
        "training_form": TrainingForm(),
        "achievement_form": AchievementForm(),
        "experiences": Experience.objects.all(),
        "trainings": Training.objects.all(),
        "achievements": Achievement.objects.all(),
    }
    return render(request, "main/dashboard.html", context)


def logout_view(request):
    logout(request)
    return redirect("main:home")


@require_POST
def contact_submit(request):
    form = ContactForm(request.POST)
    if not form.is_valid():
        return JsonResponse({"ok": False, "errors": form.errors}, status=400)

    data = form.cleaned_data
    try:
        send_mail(
            subject=f"Portfolio Contact: {data['subject']}",
            message=f"From: {data['name']} <{data['email']}>\n\n{data['message']}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=["pranishs999@gmail.com"],
            fail_silently=False,
        )
        return JsonResponse({"ok": True, "message": "Thanks! Your message has been sent."})
    except Exception as exc:
        logger.exception("Email send failed")
        return JsonResponse(
            {"ok": False, "message": f"Message received, but email notification failed: {exc}"},
            status=500,
        )
