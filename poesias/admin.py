from django.utils.html import mark_safe
import poesias.models as models
from django.contrib import admin


admin.site.register(models.Categoria)
admin.site.register(models.Autor)
admin.site.register(models.Poesia)
admin.site.register(models.Venda)


@admin.register(models.Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor',)
    list_filter = ('titulo', 'autor',)
    search_fields = ('titulo', 'autor__name', 'categoria__name',)
    readonly_fields = ('imagem_preview',)

    def imagem_preview(self, obj):
        return mark_safe(f'<img src="{obj.imagem.url}" width="100" />')
