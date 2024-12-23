from django.shortcuts import render

def inscrevase_view(request):
    return render(request, 'inscrevase/inscrevase.html')
