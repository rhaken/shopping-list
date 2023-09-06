from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'name': 'Rhaken Shaquille Akbar Yanuanda',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)