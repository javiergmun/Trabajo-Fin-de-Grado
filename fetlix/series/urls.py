from django.template.defaulttags import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from series import views



urlpatterns = [
    path('list/', views.ProductList.as_view(), name="productos_lista")
]
urlpatterns = format_suffix_patterns(urlpatterns)