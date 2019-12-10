from django.urls import path
# from staple.views import IndexView
from staple import views

urlpatterns = [
    # path('', IndexView.as_view(), name = 'staple-index'),
    path('', views.index, name = 'staple-index'),
    path('new', views.new_packet, name = 'new-packet'),
    # path('<str:slug>/', PageDetailView.as_view(), name='document-details-page'),
]