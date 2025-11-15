from django.shortcuts import render

# простая главная страница index.html
def home(request):
    return render(request, 'index.html')

# страница, на которой подключен CSS: static_handler.html
def static_handler(request):
    return render(request, 'static_handler.html')
