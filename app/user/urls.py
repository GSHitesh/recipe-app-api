"""
URL mapping for user app
"""

from django.urls import path
from user.views import CreateUserView

app_name='user'

url_patterns = [
    path('create/',CreateUserView.as_view(), name ='create')
]
