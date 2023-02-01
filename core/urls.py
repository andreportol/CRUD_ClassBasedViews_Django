from django.urls import include, path

from .views import (CreateProdutoView, DeleteProdutoView, IndexView,
                    UpDateProdutoView)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add/', CreateProdutoView.as_view(), name='add/'),
    path('<int:pk>/update/', UpDateProdutoView.as_view(), name='upd_produto'),
    path('<int:pk>/delete/', DeleteProdutoView.as_view(), name='del_produto'),
]
