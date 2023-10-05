from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, permissions
from .models import Post, User
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly
from .utils import SendMailTo

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)


# curl -X POST http://localhost:8000/api/v1/send_email -d "email=someemail@gmail.com"
@csrf_exempt
def send_email(request):
    
    email = request.POST.get('email')
    if email:
        if user := User.objects.get(email=email):
            print(user)
            SendMailTo(user).authentication_email()
            SendMailTo(user).wellcome_email()
            
            return HttpResponse(status=204)
    return HttpResponse(status=400)
