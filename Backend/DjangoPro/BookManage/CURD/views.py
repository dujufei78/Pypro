# Create your views here.
from django.http import JsonResponse
from rest_framework.generics import GenericAPIView, RetrieveAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from CURD.serializer import BookSerializer
from app01.models import Book


class Book_GenericAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BookSingle_GenericAPIView(RetrieveAPIView, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class Book_APIView(APIView):
    print('======afd======')
    def get(self):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
        # return Response({'msg': 'ok'})

    def post(self, request):
        serializer = BookSerializer(data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer.errors)


class BookDetail_APIView(APIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, pk):
        book = Book.objects.filter(nid=pk).first()
        serializer = BookSerializer(instance=book)
        return JsonResponse(serializer.data)

    def update(self, request, pk):
        book = Book.objects.filter(nid=pk).first()
        serializer = BookSerializer(instance=book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer.errors)

    def delete(self, pk):
        book = Book.objects.get(nid=pk)
        book.delete()
        return JsonResponse({'msg': 'delete success'})
