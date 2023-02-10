from todolist_api.views import TodoViewSet
from rest_framework.routers import DefaultRouter
from todolist_api import views
router = DefaultRouter()
router.register(r'Todo',views.TodoViewSet, basename='Todo')
urlpatterns = router.urls