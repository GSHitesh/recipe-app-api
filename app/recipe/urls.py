""""
URL Mapping for the recipe app
"""

from django.urls import (
    path, include
)

from rest_framework.routers import DefaultRouter

from recipe import views

router = DefaultRouter()
router.register('recipes', views.RecipeViewSet)

"""
Default router creates a api/recipe/<custom> endpoint for api calls
RecipeViewSet will have all the generated urls depending upon the functionality that's enabled on viewset
will support all the HTTP Method get post patch put and delete
"""

app_name = 'recipe'
""" 
for reverse method used in testcases """

urlpatterns = [
    path('',include(router.urls))
]

"""
urlpatterns gives the url options and then you can use that to retrive the URLs by revealing all
"""