from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "title":"Multishop",
    }
    return render(request, "shop/index.html", context)