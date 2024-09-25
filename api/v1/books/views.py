from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

from books.models import Book

from api.v1.books.serializers import BookSerializer


# Custom pagination class
class CustomPagination(PageNumberPagination):
    page_size = 10  # Number of items per page
    page_size_query_param = 'page_size'
    max_page_size = 100


# function to view books
@api_view(["GET"])
@permission_classes([AllowAny])
def books(request):
    instance = Book.objects.all()
    search_query = request.query_params.get('search', None)
    if search_query:
        instance = instance.filter(title__icontains=search_query) | instance.filter(author__icontains=search_query)

    paginator = CustomPagination()
    paginated_queryset = paginator.paginate_queryset(instance, request)
    context = {
        "request": request
    }
    serializer = BookSerializer(paginated_queryset, many=True, context=context)

    response_data = {
        "status_code": 200,
        "data": serializer.data,
        "pagination": {
            "count": paginator.page.paginator.count,
            "next": paginator.get_next_link(),
            "previous": paginator.get_previous_link()
        }
    }
    return paginator.get_paginated_response(response_data)


# Function to create a book
@api_view(["POST"])
@permission_classes([AllowAny])
def create_book(request):
    if request.method == "POST":
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            response_data = {
                "status_code": 201,
                "message": "Successfully added product",
                "data": serializer.data,
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        
        else:
            response_data = {
                "status_code": 400,
                "message": "validation error",
                "error": serializer.errors
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)



# Function to get a specific book
@api_view(["GET"])
@permission_classes([AllowAny])
def view_book(request,pk):
    if Book.objects.filter(pk=pk).exists():
        instance=Book.objects.get(pk=pk)
        context = {
        "request": request
        }
        serializer=BookSerializer(instance,context=context)

        response_data = {
        "status_code": 200,
        "data": serializer.data
        }
        return Response(response_data)
    else:
        response_data = {
            "status_code": 400,
            "message": "validation error",
            "error": serializer.errors
            }
        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


# Function to  update specific book
@api_view(["PUT"])
@permission_classes([AllowAny])
def update_book(request,pk):
    if Book.objects.filter(pk=pk).exists():
        instance=Book.objects.get(pk=pk)

        context = {
        "request": request
        }
        serializer=BookSerializer(instance,data=request.data,partial=True, context=context)
        if serializer.is_valid():
            serializer.save()

            response_data = {
            "status_code": 200,
            "message":"successfully edited the book"
            }
            return Response(response_data)
        
        else:
            response_data = {
                "status_code": 400,
                "message": "validation error",
                "error": serializer.errors
                }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
    else:
        response_data={
            "status_code":400,
            "message":"Book not found"
        }
        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


# Function to  delete specific book
@api_view(["DELETE"])
@permission_classes([AllowAny])
def delete_book(request, pk):
    try:
        instance = Book.objects.get(pk=pk)
        instance.delete()
        response_data = {
            "status_code": 200,
            "message": "Deleted Successfully"
        }
        return Response(response_data)
    
    except Book.DoesNotExist:
        response_data = {
            "status_code": 404,
            "message": "Book not found"
        }
        return Response(response_data, status=status.HTTP_404_NOT_FOUND)
