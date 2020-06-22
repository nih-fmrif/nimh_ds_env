from django.urls import include
from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'projectpapers', views.ProjectPaperViewSet)
router.register(r'people', views.PersonViewSet)
router.register(r'orgs', views.OrgViewSet)
router.register(r'orgArticles', views.OrgArticleViewSet)
router.register(r'personArticles', views.PersonArticleViewSet)
router.register(r'personGraph', views.PersonGraphViewSet)
router.register(r'orgGraph', views.OrgGraphViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('uniquejournals/', views.unique_journals, name='unique-journals'),
    path('uniquepis/', views.unique_pis, name='unique-pis'),
]