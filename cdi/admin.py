from django.contrib import admin

# Register your models here.
from .models import Formation,Matiere,Course,Apply
admin.site.site_header = "Center Innovation Informatoque"


class FormationAdminConfig(admin.ModelAdmin):
    model = Formation
    search_fields = ('title', 'matiere1', 'matiere2',)
    list_filter = ('title', 'matiere1', 'matiere2', 'matiere3', 'matiere4', 'matiere5')
    # ordering = ('-start_date',)
    list_display = ('title', 'matiere1', 'matiere2', 'matiere3', 'matiere4', 'matiere5',
                    'nbrmatier', 'description')
    fieldsets = (
        (None, {'fields': ('title', 'matiere1', 'matiere2',)}),
    )


    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('title', 'matiere1', 'matiere2', 'matiere3', 'matiere4', 'matiere5', 'nbrmatier', 'description')
            }
         ),
    )

class MatiereAdminConfig(admin.ModelAdmin):
    model = Matiere
    search_fields = ('title', 'description', 'time',)
    list_filter = ('title', 'description', 'time')
    # ordering = ('-start_date',)
    list_display = ('title', 'description', 'time',)
    fieldsets = (
        (None, {'fields': ('title', 'description', 'time')}),
    )


    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('title', 'description', 'time')
            }
         ),
    )   

class CommentaireAdminConfig(admin.ModelAdmin):
    model = Apply
    search_fields = ('course', 'comment', 'created_at',)
    list_filter = ('course', 'comment', 'created_at')
    # ordering = ('-start_date',)
    list_display = ('course', 'comment', 'created_at')
    fieldsets = (
        (None, {'fields': ('course', 'comment', 'created_at')}),
    )


    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('course', 'comment', 'created_at')
            }
         ),
    )        
admin.site.register(Formation,FormationAdminConfig)
admin.site.register(Matiere,MatiereAdminConfig)
admin.site.register(Course)
admin.site.register(Apply,CommentaireAdminConfig)

