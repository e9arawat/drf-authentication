"""
Urls module
"""
from django.urls import path, include
from myAPIapp import views

# from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("book/", views.BookList.as_view(), name="book"),
    path("book-detail/<int:pk>/", views.BookDetail.as_view(), name="book-detail"),
    path("car/", views.CarList.as_view(), name="car"),
    path("car-detail/<int:pk>/", views.CarDetail.as_view(), name="car-detail"),
    path("song/", views.SongList.as_view(), name="song"),
    path("song-detail/<int:pk>/", views.SongDetail.as_view(), name="song-detail"),
    path("movie/", views.MovieList.as_view(), name="movie"),
    path("movie-detail/<int:pk>/", views.MovieDetail.as_view(), name="movie-detail"),
    path("job-posting/", views.JobPostingList.as_view(), name="job-posting"),
    path(
        "job-posting-detail/<int:pk>/",
        views.JobPostingDetail.as_view(),
        name="job-posting-detail",
    ),
    path("product/", views.ProductList.as_view(), name="product"),
    path(
        "product-detail/<int:pk>/", views.ProductDetail.as_view(), name="product-detail"
    ),
    path("task/", views.TaskList.as_view(), name="task"),
    path("task-detail/<int:pk>/", views.TaskDetail.as_view(), name="task-detail"),
    path("post/", views.PostList.as_view(), name="post"),
    path("post-detail/<int:pk>/", views.PostDetail.as_view(), name="post-detail"),
    path("enrollment/", views.EnrollmentList.as_view(), name="enrollment"),
    path(
        "enrollment-detail/<int:pk>/",
        views.EnrollmentDetail.as_view(),
        name="enrollment-detail",
    ),
    path("student/", views.StudentList.as_view(), name="student"),
    path(
        "student-detail/<int:pk>/", views.StudentDetail.as_view(), name="student-detail"
    ),
    path("course/", views.CourseList.as_view(), name="course"),
    path("course-detail/<int:pk>/", views.CourseDetail.as_view(), name="course-detail"),
    path("post-category/", views.CourseList.as_view(), name="post-category"),
    path(
        "post-category-detail/<int:pk>/",
        views.CourseDetail.as_view(),
        name="post-category-detail",
    ),
    path("project/", views.ProjectList.as_view(), name="project"),
    path(
        "project-detail/<int:pk>/", views.ProjectDetail.as_view(), name="project-detail"
    ),
    path("category/", views.CategoryList.as_view(), name="category"),
    path(
        "category-detail/<int:pk>/",
        views.CategoryDetail.as_view(),
        name="category-detail",
    ),
]


# urlpatterns = format_suffix_patterns(urlpatterns)
