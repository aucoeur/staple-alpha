from django.urls import path
from api.views import DocumentList, DocumentDetail

urlpatterns = [
    path('', DocumentList.as_view(), name='documents_list'),
    path('<str:slug>/', DocumentDetail.as_view(), name='document_detail')
]