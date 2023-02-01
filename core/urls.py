from django.urls import include, path

from .views import IndexView, createProdutoView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add/', createProdutoView.as_view(), name='add/'),
]
