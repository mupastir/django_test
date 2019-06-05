from django.urls import path
from .views import index, by_category, GoodsCreateView

urlpatterns = [
    path('add/', GoodsCreateView.as_view(), name='add'),
    path('<int:category_id>/', by_category, name='by_category'),
    path('', index, name='index'),
]
