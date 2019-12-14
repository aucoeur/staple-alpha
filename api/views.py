from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from staple.models import Document
from api.serializers import DocumentSerializer

class DocumentList(APIView):
    def get(self, request):
        documents = Document.objects.all()[:20]
        data = DocumentSerializer(documents, many=True).data
        return Response(data)

class DocumentDetail(APIView):
    def get(self, request, pk):
        document = get_object_or_404(Document, pk=pk)
        data = DocumentSerializer(document).data
        return Response(data)