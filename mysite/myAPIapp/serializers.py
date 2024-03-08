"""
serializer class
"""
from rest_framework import serializers
from .models import (
    Book,
    Car,
    Song,
    Movie,
    JobPosting,
    Product,
    Project,
    Task,
    PostCategory,
    Post,
    Category,
    Student,
    Enrollment,
    Course,
)


class BookSerializer(serializers.ModelSerializer):
    """
    Book serializer class
    """

    id = serializers.IntegerField(read_only=True)

    class Meta:
        """
        Meta class
        """

        model = Book
        fields = "__all__"


class CarSerializer(serializers.ModelSerializer):
    """
    Car serializer class
    """

    id = serializers.IntegerField(read_only=True)

    class Meta:
        """
        meta class
        """

        model = Car
        fields = "__all__"


class SongSerializer(serializers.ModelSerializer):
    """
    Song serializer class
    """

    id = serializers.IntegerField(read_only=True)

    class Meta:
        """
        meta class
        """

        model = Song
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    """
    movie serializer class
    """

    id = serializers.IntegerField(read_only=True)

    class Meta:
        """
        Meta class
        """

        model = Movie
        fields = "__all__"


class JobPostingSerializer(serializers.ModelSerializer):
    """
    job posting serializer class
    """

    id = serializers.IntegerField(read_only=True)

    class Meta:
        """
        Meta class
        """

        model = JobPosting
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    """
    category serializer class
    """

    id = serializers.IntegerField(read_only=True)

    class Meta:
        """
        Meta class
        """

        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    """
    product serializer class
    """

    id = serializers.IntegerField(read_only=True)
    category_info = serializers.SerializerMethodField()
    url = serializers.HyperlinkedIdentityField(view_name="category-detail")

    class Meta:
        """
        Meta class
        """

        model = Product
        fields = "__all__"

    def get_category_info(self, obj):
        """
        return the category details
        """
        return CategorySerializer(obj.category).data


class ProjectSerializer(serializers.ModelSerializer):
    """
    project serializer class
    """

    id = serializers.IntegerField(read_only=True)

    class Meta:
        """
        Meta class
        """

        model = Project
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    """
    task serializer class
    """

    id = serializers.IntegerField(read_only=True)
    project_info = serializers.SerializerMethodField()

    class Meta:
        """
        Meta class
        """

        model = Task
        fields = "__all__"

    def get_project_info(self, obj):
        """
        return the project details
        """
        return ProjectSerializer(obj.project).data


class PostCategorySerializer(serializers.ModelSerializer):
    """
    post category serializer
    """

    id = serializers.IntegerField(read_only=True)

    class Meta:
        """
        Meta class
        """

        model = PostCategory
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    """
    post serializer class
    """

    id = serializers.IntegerField(read_only=True)
    postcategory_info = serializers.SerializerMethodField()

    class Meta:
        """
        Meta class
        """

        model = Post
        fields = "__all__"

    def get_postcategory_info(self, obj):
        """
        return the post category details
        """
        return PostCategorySerializer(obj.category).data


class StudentSerializer(serializers.ModelSerializer):
    """
    student serializer class
    """

    id = serializers.IntegerField(read_only=True)

    class Meta:
        """
        Meta class
        """

        model = Student
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    """
    course serializer class
    """

    id = serializers.IntegerField(read_only=True)

    class Meta:
        """
        Meta class
        """

        model = Course
        fields = "__all__"


class EnrollmentSerializer(serializers.ModelSerializer):
    """
    enrollment serializer class
    """

    student_info = serializers.SerializerMethodField()
    course_info = serializers.SerializerMethodField()
    # url = serializers.HyperlinkedIdentityField(view_name="student-detail")

    class Meta:
        """
        Meta class
        """

        model = Enrollment
        fields = "__all__"

    def get_student_info(self, obj):
        """
        return the student details
        """
        return StudentSerializer(obj.student).data

    def get_course_info(self, obj):
        """
        return the student details
        """
        return CourseSerializer(obj.course).data
