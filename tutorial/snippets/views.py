from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer
from rest_framework import generics, renderers
from django.contrib.auth.models import User
from rest_framework import permissions, viewsets
from .permission import IsOwnerOrReadOnly
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse
# Create your views here.
"""
DefaultRouter를 사용하면 자동으로 API root view를 생성하므로 밑에 코드는 삭제가 가능하다.

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })
"""

class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, *kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)
        
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer