from django.shortcuts import render

def home(request):
    skills = [
        {'name': 'Python', 'color': 'blue'},
        {'name': 'Django', 'color': 'indigo'},
        {'name': 'Flask', 'color': 'green'},
        {'name': 'HTML', 'color': 'red'},
        {'name': 'CSS', 'color': 'cyan'},
        {'name': 'Tailwind', 'color': 'yellow'},
    ]

    projects = [
        {'title':'Weather App', 'desc':'A web app built with Django', 'link':'https://github.com/pranishs999/Weather-app.git'},
        {'title':'Library LMS', 'desc':'Library Management System', 'link':'https://github.com/pranishs999/Library_Management_system-LMS.git'},
        {'title':'Gradebook CLI', 'desc':'Command-line Gradebook system', 'link':'https://github.com/pranishs999/GradeBook-CLI.git'},
    ]

    education = [
        'Shree Rastriya Ma. Vi. - SEE - 2020',
        'New Capital College Tandi - SLC - 2022',
        'Hetauda City College - BSc. CSIT - Present'
    ]

    experience = [
        {'role':'Secondary Teacher','company':'Zenith International Secondary School','duration':'May 2025 - Present','details':'Teaching computer science.'}
    ]

    achievements = [
        'UTech Hackathon Alpha',
        'BIC Hackathon v1.0',
        'OSM Hack Fest 2023 Chitwan'
    ]

    context = {
        'skills': skills,
        'projects': projects,
        'education': education,
        'experience': experience,
        'achievements': achievements
    }

    return render(request, 'main/home.html', context)
