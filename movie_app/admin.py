from django.contrib import admin, messages

from .models import Movie
from django.db.models import QuerySet


# Register your models here.

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'currency', 'budget', 'rating_status']
    list_editable = ['rating', 'currency', 'budget']
    ordering = ['-rating', '-name']
    list_per_page = 10
    actions = ['set_dollars', 'set_euro']
    search_fields = ['name__startswith', 'rating']

    @admin.display(ordering='rating', description='Статус')
    def rating_status(self, movie: Movie):
        if movie.rating < 50:
            return 'Зачем это смотреть?!'
        elif movie.rating < 70:
            return 'Разок можно глянуть'
        elif movie.rating < 85:
            return 'Зачет'
        return 'Топчик'

    @admin.action(description='Установить валюту в доллары')
    def set_dollars(self, request, queryset: QuerySet):
        queryset.update(currency=Movie.USD)

    @admin.action(description='Установить валюту в евро')
    def set_euro(self, request, queryset: QuerySet):
        count_updated = queryset.update(currency=Movie.EUR)
        self.message_user(
            request,
            f'Было обновлено {count_updated} записей.',
            messages.ERROR
        )

# admin.site.register(Movie, MovieAdmin)
