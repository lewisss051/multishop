from django.shortcuts import render
from django.views.generic import ListView

from shop.models import *


class Index(ListView):
    model = SubCategory
    context_object_name = "subcategories"
    template_name = "shop/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subcategories = SubCategory.objects.all()
        offers = Offer.objects.all()
        products = Product.objects.all()
        categories = Category.objects.all()
        data = {}
        data["subcategories"] = subcategories
        data["offers"] = offers
        data["categories"] = categories
        data["products"] = products
        context["data"] = data
        return context
