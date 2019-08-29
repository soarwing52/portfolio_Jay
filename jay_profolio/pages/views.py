from django.shortcuts import render
from .models import Skill, Project, Section, About, Education, WorkExperience, Blog
# Create your views here.

def index(request, *args, **kwargs):
    return render(request, 'pages/index.html')

def test(request, *args, **kwargs):
    skills = Skill.objects.all()
    sections = Section.objects.all()
    projects = Project.objects.all()
    educations = Education.objects.all()
    works = WorkExperience.objects.all()
    abouts = About.objects.all()[0]
    blogs = Blog.objects.all()
    context = {'skills':skills,
               'sections':sections,
               'projects':projects,
               'about':abouts,
               'edus':educations,
               'works':works,
               'blogs':blogs,
               }
    return render(request, 'pages/test.html', context)
