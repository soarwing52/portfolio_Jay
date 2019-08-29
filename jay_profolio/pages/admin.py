from django.contrib import admin

from .models import Skill, Project, Section, About, Education, WorkExperience,Blog
# Register your models here.
admin.site.register(Section)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(About)
admin.site.register(Education)

class WorkAdmin(admin.ModelAdmin):
    list_display= ('name', 'time', 'position')

    def get_queryset(self, request):
        queryset = super(WorkAdmin,self).get_queryset(request)
        queryset = queryset.order_by('name')
        return queryset

admin.site.register(WorkExperience, WorkAdmin)

admin.site.register(Blog)