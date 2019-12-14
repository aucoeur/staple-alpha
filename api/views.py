from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView

# Create your views here.
from staple.models import Document
from api.serializers import DocumentSerializer

class DocumentList(ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class DocumentDetail(RetrieveDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer