from django.contrib import admin
from django.urls import path
from flatpages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),                 # /  -> index.html
    path('hello/', views.home, name='hello'),          # /hello/ -> тоже текст/шаблон
    path('static-page/', views.static_handler, name='static_page'),  # /static-page/
]
