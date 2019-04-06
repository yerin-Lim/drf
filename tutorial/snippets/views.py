from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework import generics

# Create your views here.

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class SnippetDetail(generics.RetrieveDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


"""
class SnippetList(mixins.ListModelMixin),
                  mixins.CreateModelMixin),
                  generics.GenricAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self,request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    
class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
"""