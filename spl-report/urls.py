from django.urls import path
from . import views
urlpatterns=[
    path('',views.html,name='html'),
    path('home',views.html,name='html'),
    path('graphs',views.graphs,name='graphs')
    ##path('',views.Viewpdf.as_view(),name="pdf_view")
]