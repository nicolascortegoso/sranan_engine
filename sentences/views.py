from django.shortcuts import render

# Create your views here.
def sentences(request):
    return render(request, 'sentences.html')
