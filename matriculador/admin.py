from django.contrib import admin
from matriculador.models import Estudante, Curso


class EstudanteAdm(admin.ModelAdmin):
    list_display = ('id','nome', 'email', 'cpf', 'data_nascimento', 'celular',)
    list_display_links = ('id','nome',)
    list_per_page = 20
    search_fields = ('nome',)

class CursoAdm(admin.ModelAdmin):
    list_display = ('id','codigo','descricao',)
    list_display_links = ('id','codigo',)
    search_fields = ('codigo',)

admin.site.register(Estudante,EstudanteAdm)
admin.site.register(Curso,CursoAdm)
