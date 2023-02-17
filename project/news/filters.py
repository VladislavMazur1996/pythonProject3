import django_filters
from django.forms import widgets
from django_filters import FilterSet, DateFromToRangeFilter

from .models import Post


class PostFilter(FilterSet):
    date = django_filters.DateTimeFilter(field_name='creating_dt', label='Дата:',
                                         widget=widgets.SelectDateWidget(),
                                         lookup_expr='gte', )
    name = django_filters.CharFilter(field_name='title', label='Название:',
                                     lookup_expr='icontains')
    author = django_filters.CharFilter(field_name='author__user__username', label='Автор:',
                                       lookup_expr='icontains')

    class Meta:
        model = Post
        fields = {}
