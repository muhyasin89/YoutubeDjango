
from django.urls import path, include
from rest_framework import routers
from api.views.users import UserViewSet
from api.views.register import RegisterUserAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from api.views.books import BooksListCreate, BookUpdateDelete
from api.views.author import AuthorsListCreate, AuthorUpdateDelete
from api.views.rent_history import RentHistoriesListCreate, RentHistoryUpdateDelete
from api.views.task_librarian import TaskLibrariansListCreate, TaskLibrarianUpdateDelete
from api.views.task_librarian_detail import TaskLibrarianDetailsListCreate, TaskLibrarianDetailUpdateDelete
from api.views.task_report import TaskReportsListCreate, TaskReportUpdateDelete

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('register/',RegisterUserAPIView.as_view(), name="register"),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('books/', BooksListCreate.as_view(), name='books'),
    path('book/<int:pk>/update/', BookUpdateDelete.as_view(), name='book_update'),
    path('author/', AuthorsListCreate.as_view(), name='authors'),
    path('author/<int:pk>/update/', AuthorUpdateDelete.as_view(), name='author_update'),
    path('rent/history/', RentHistoriesListCreate.as_view(), name='rent_history'),
    path('rent/history/<int:pk>/update/', RentHistoryUpdateDelete.as_view(), name='rent_history_update'),
    path('task/librarian/', TaskLibrariansListCreate.as_view(), name='task_librarian'),
    path('task/librarian/<int:pk>/update/', TaskLibrarianUpdateDelete.as_view(), name='task_librarian_update'),
    path('task/librarian/details/', TaskLibrarianDetailsListCreate.as_view(), name='task_librarian_details'),
    path('task/librarian/detail/<int:pk>/update/', AuthorUpdateDelete.as_view(), name='task_librarian_details_update'),
    path('task/report/', TaskReportsListCreate.as_view(), name='task_report'),
    path('task/report/<int:pk>/update/', TaskReportUpdateDelete.as_view(), name='task_report_update'),
]