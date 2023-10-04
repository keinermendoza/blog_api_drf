from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly
from .utils import MailSender

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)

# curl -X POST http://localhost:8000/api/v1/send_email -H "Content-Type: application/json"
#    -d '{"username": "boby", "mail": "holamundo@gmail.com"}'

@csrf_exempt
def send_email(request):
    username = request.POST.get('username')
    mail = request.POST.get('mail')
    MailSender.wellcome(user_data={'username':username, 'mail':mail})
    return HttpResponse(status=204)