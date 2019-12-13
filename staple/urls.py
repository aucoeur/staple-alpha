from django.urls import path
# from staple.views import IndexView
from staple import views
from staple.views import DocumentDetailView, DocumentNewView, DocumentListView, DocumentUpdateView, DocumentDeleteView

urlpatterns = [
    # path('', IndexView.as_view(), name = 'staple-index'),
    path('', views.index, name = 'staple-index'),
    path('new/', DocumentNewView.as_view(), name = 'new-packet'),
    path('documents/', DocumentListView.as_view(), name = "documents-list-page"),
    path('documents/<str:slug>/', DocumentDetailView.as_view(), name='document-details-page'),
    path('documents/<str:slug>/update', DocumentUpdateView.as_view(), name = 'document-update-page'),
    path('documents/<str:slug>/delete', DocumentDeleteView.as_view(), name = 'document-delete'),

]