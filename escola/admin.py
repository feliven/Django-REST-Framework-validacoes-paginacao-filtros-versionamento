from django.contrib import admin
from django.db.models.functions import Lower
from escola.models import Estudante, Curso, Matricula


# Register your models here.
class ListandoEstudantes(admin.ModelAdmin):
    list_display = ("id", "nome", "email")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    ordering = ("nome",)
    list_editable = ("email",)
    list_per_page = 10

    def get_ordering(self, request):  # type: ignore[override]
        return [Lower("nome")]


class ListandoCursos(admin.ModelAdmin):
    list_display = ("codigo", "descricao", "nivel")
    list_display_links = ("codigo",)
    search_fields = ("codigo", "descricao")
    list_filter = ("nivel",)
    list_editable = ("nivel",)
    list_per_page = 10

    def get_ordering(self, request):  # type: ignore[override]
        return [Lower("codigo"), Lower("descricao")]


class ListandoMatriculas(admin.ModelAdmin):
    list_display = ("estudante", "curso", "periodo")
    list_display_links = ("estudante", "curso")
    search_fields = ("codigo",)
    list_filter = ("periodo",)
    list_editable = ("periodo",)
    list_per_page = 10


admin.site.register(Estudante, ListandoEstudantes)
admin.site.register(Curso, ListandoCursos)
admin.site.register(Matricula, ListandoMatriculas)
