from django.contrib import admin

from .models import Skill, Project, Section, About, Education, WorkExperience
# Register your models here.
admin.site.register(Section)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(About)
admin.site.register(Education)
admin.site.register(WorkExperience)