from django.shortcuts import render

# Create your views here.
# render this index template
def index(request, *args, **kwargs):
    return render(request , 'frontend/index.html')