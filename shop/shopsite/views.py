from django.shortcuts import render
from .models import Goods, Category
from django.views.generic.edit import CreateView
from .forms import GoodsForm
from django.urls import reverse_lazy


class GoodsCreateView(CreateView):
    template_name = 'shopsite/create.html'
    form_class = GoodsForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


def index(request):
    gds = Goods.objects.all()
    categories = Category.objects.all()
    context = {'gds': gds, 'categories': categories}
    return render(request, 'shopsite/index.html', context)


def by_category(request, category_id):
    gds = Goods.objects.filter(category=category_id)
    categories = Category.objects.all()
    current_category = Category.objects.get(pk=category_id)
    context = {'gds': gds, 'categories': categories, 'current_category': current_category}
    return render(request, 'shopsite/by_category.html', context)

