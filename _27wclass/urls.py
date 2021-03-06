"""_27wclass URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import home.views
import accounts.views
import community.views
import contact.views
import issue.views
import lecture.views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.views.index, name='index'),

    path('accounts/',include('accounts.urls')),
    #path('accounts/login', accounts.views.login, name = 'login'),
    #path('accounts/signup', accounts.views.signup, name = 'signup'),
    #path('accounts/logout', accounts.views.logout, name = 'logout'),

    #path('community/community_board', community.views.community_board, name = 'community_board'),
    
    path('community/', include('community.urls')),
    path('lecture/', include('lecture.urls')),
    
    #path('contact/contact_board', contact.views.contact_board, name = 'contact_board'),
    #path('contact/create', contact.views.create, name = 'create'),
    path('contact/',include('contact.urls')),
    path('issue/',include('issue.urls')),
    path('payment/', include('payment.urls')),
    #path('issue/issue_board', issue.views.issue_board, name = 'issue_board'),
    
    # path('lecture/lecture_board', lecture.views.lecture_board, name = 'lecture_board'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)