from django.http import Http404
from django.views import generic
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Book, Order
from main.serializers import BookSerializer, OrderSerializer


@api_view(['GET'])
def books_list(request):
    """получите список книг из БД
    отсериализуйте и верните ответ
    """
    books = Book.objects.all()
    print(books)
    serializer_class = BookSerializer(books, many=True)
    return Response(serializer_class.data)


class CreateBookView(APIView):
    def post(self, request):
        # получите данные из запроса

        serializer = BookSerializer(data=request.data) #передайте данные из запроса в сериализатор
        serializer.is_valid()
        serializer.validated_data
        serializer.save()
        if serializer.is_valid(raise_exception=True): #если данные валидны
            return Response('Книга успешно создана') # возвращаем ответ об этом


class BookDetailsView(RetrieveAPIView):
    # реализуйте логику получения деталей одного объявления
    def get(self, request, book_id):
        try:
            book = Book.objects.filter(id=book_id)
            print(book)
            ser = BookSerializer(book, many=True)
            return Response(ser.data)
        except Book.DoesNotExists:
            raise Http404("Book not found")
        pass


class BookUpdateView(UpdateAPIView):
    # реализуйте логику обновления Книги
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDeleteView(DestroyAPIView):
    # реализуйте логику удаления объявления
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class OrderViewSet(viewsets.ModelViewSet):
    # реализуйте CRUD для заказов
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
