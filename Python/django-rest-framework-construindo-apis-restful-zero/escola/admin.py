from django.contrib import admin
from escola.models import Estudante, Curso, Matricula

class EstudanteAdmin(admin.ModelAdmin):
    # listando campos que iram aparecer no django admin
    list_display = ('id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular')
    # campos clicaveis no django admin
    list_display_links = ('id', 'nome')
    # campos habeis para busca no django admin
    search_fields = ('nome', 'email', 'cpf')
    # quantos itens por pagina
    list_per_page = 20
    # filtros disponiveis no django admin
    list_filter = ('data_nascimento',)
    # ordenação do django admin
    ordering = ('id', 'nome',)
    
admin.site.register(Estudante, EstudanteAdmin)

class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'descricao', 'nivel')
    list_display_links = ('id', 'codigo')
    search_fields = ('codigo', 'id')
    list_filter = ('nivel',)
    ordering = ('id',)
    
admin.site.register(Curso, CursoAdmin)

class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('id', 'estudante', 'curso', 'periodo')
    list_display_links = ('id', )

admin.site.register(Matricula, MatriculaAdmin)

