from django.forms import ModelForm
from .models import Goods


class GoodsForm(ModelForm):
    class Meta:
        model = Goods
        fields = ('name', 'price',
                  'image_1', 'image_2',
                  'image_3', 'image_4',
                  'image_5', 'image_6',
                  'category', 'brand',
                  'color', 'size',
                  'quality', 'description')
