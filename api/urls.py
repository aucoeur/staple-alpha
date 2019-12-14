from django.urls import path
from api.views import DocumentList, DocumentDetail

urlpatterns = [
    path('documents/', DocumentList.as_view(), name='documents_list'),
    path('document/<str:slug>/', DocumentDetail.as_view(), name='document_detail')
]