import django_filters
from .models import Article, Comment

class ArticleFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.NumberFilter(field_name='author__id')

    class Meta:
        model = Article
        fields = ['title', 'author']

class CommentFilter(django_filters.FilterSet):
    content = django_filters.CharFilter(lookup_expr='icontains')
    article = django_filters.NumberFilter(field_name='article__id')

    class Meta:
        model = Comment
        fields = ['content', 'article']
