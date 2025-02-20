from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer

class PostListView(generics.ListAPIView):
    queryset = Post.objects.filter(status='published')
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.query_params.get('status', None)
        if status in ['draft', 'published']:
            queryset = Post.objects.filter(status=status)
        return queryset

class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.filter(status='published')
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'slug'

class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, status='published')

class PostDeleteView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'slug'

class PostUpdateView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'slug'