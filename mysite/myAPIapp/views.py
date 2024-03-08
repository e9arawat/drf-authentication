"""
App views
"""
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from myAPIapp import serializers
from .models import (
    Book,
    Car,
    Song,
    Movie,
    JobPosting,
    Category,
    Task,
    Product,
    Project,
    PostCategory,
    Post,
    Student,
    Course,
    Enrollment,
)

# Create your views here.


class BookList(ListCreateAPIView):
    """
    view to display book details
    """

    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer


class BookDetail(RetrieveUpdateDestroyAPIView):
    """
    view to update or delete the data
    """

    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer


class CarList(ListCreateAPIView):
    """
    view to display car details
    """

    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Car.objects.all()
    serializer_class = serializers.CarSerializer


class CarDetail(RetrieveUpdateDestroyAPIView):
    """
    view to update or delete the data
    """

    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Car.objects.all()
    serializer_class = serializers.CarSerializer


class SongList(ListCreateAPIView):
    """
    view to display song details
    """

    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Song.objects.all()
    serializer_class = serializers.SongSerializer


class SongDetail(RetrieveUpdateDestroyAPIView):
    """
    view to update or delete the data
    """

    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Song.objects.all()
    serializer_class = serializers.SongSerializer


class MovieList(ListCreateAPIView):
    """
    view to display movie details
    """

    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Movie.objects.all()
    serializer_class = serializers.MovieSerializer


class MovieDetail(RetrieveUpdateDestroyAPIView):
    """
    view to update or delete the data
    """

    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Movie.objects.all()
    serializer_class = serializers.MovieSerializer


class JobPostingList(ListCreateAPIView):
    """
    view to display job details
    """

    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = JobPosting.objects.all()
    serializer_class = serializers.JobPostingSerializer


class JobPostingDetail(RetrieveUpdateDestroyAPIView):
    """
    view to update or delete the data
    """

    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = JobPosting.objects.all()
    serializer_class = serializers.JobPostingSerializer


class CategoryList(ListCreateAPIView):
    """
    view to display category details
    """

    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer


class CategoryDetail(RetrieveUpdateDestroyAPIView):
    """
    view to update and delete the data
    """

    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer


class ProductList(ListCreateAPIView):
    """
    view to display job details
    """

    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductDetail(RetrieveUpdateDestroyAPIView):
    """
    view to update and delete the data
    """

    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProjectList(ListCreateAPIView):
    """
    view to display project details
    """

    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = serializers.ProjectSerializer


class ProjectDetail(RetrieveUpdateDestroyAPIView):
    """
    view to update and delete the data
    """

    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Project.objects.all()
    serializer_class = serializers.ProjectSerializer


class TaskList(ListCreateAPIView):
    """
    view to display task details
    """

    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = serializers.TaskSerializer


class TaskDetail(RetrieveUpdateDestroyAPIView):
    """
    view to update and delete the data
    """

    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Task.objects.all()
    serializer_class = serializers.TaskSerializer


class PostCategoryList(ListCreateAPIView):
    """
    view to display and create post
    """

    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = PostCategory.objects.all()
    serializer_class = serializers.PostCategorySerializer


class PostCategoryDetail(RetrieveUpdateDestroyAPIView):
    """
    view to retrieve the data
    """

    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = PostCategory.objects.all()
    serializer_class = serializers.PostCategorySerializer


class PostList(ListCreateAPIView):
    """
    view to display and create post
    """

    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer


class PostDetail(RetrieveUpdateDestroyAPIView):
    """
    view to retrieve the data
    """

    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer


class StudentList(ListCreateAPIView):
    """
    view to display and create student
    """

    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = serializers.StudentSerializer


class StudentDetail(RetrieveUpdateDestroyAPIView):
    """
    view to retrieve, update or delete the data
    """

    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Student.objects.all()
    serializer_class = serializers.StudentSerializer


class CourseList(ListCreateAPIView):
    """
    view to display and create course
    """

    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Course.objects.all()
    serializer_class = serializers.CourseSerializer


class CourseDetail(RetrieveUpdateDestroyAPIView):
    """
    view to retrieve, update or delete the data
    """

    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Course.objects.all()
    serializer_class = serializers.CourseSerializer


class EnrollmentList(ListCreateAPIView):
    """
    view to display and create enrollment
    """

    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Enrollment.objects.all()
    serializer_class = serializers.EnrollmentSerializer


class EnrollmentDetail(RetrieveUpdateDestroyAPIView):
    """
    view to retrieve the data
    """

    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Enrollment.objects.all()
    serializer_class = serializers.EnrollmentSerializer
