"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('workspace/',include('workspace.urls')),
    path('', TemplateView.as_view(template_name='index.html')),
    path('home', TemplateView.as_view(template_name='index.html')),
    path('profile', TemplateView.as_view(template_name='index.html')),
    path('basic-details', TemplateView.as_view(template_name='index.html')),
    path('college-education', TemplateView.as_view(template_name='index.html')),
    path('professional', TemplateView.as_view(template_name='index.html')),
    path('preference', TemplateView.as_view(template_name='index.html')),
    path('preference-modal', TemplateView.as_view(template_name='index.html')),
    path('skills', TemplateView.as_view(template_name='index.html')),
    path('projects', TemplateView.as_view(template_name='index.html')),
    path('social', TemplateView.as_view(template_name='index.html')),
    path('leadership', TemplateView.as_view(template_name='index.html')),
    path('volunteer', TemplateView.as_view(template_name='index.html')),
    path('fellowship', TemplateView.as_view(template_name='index.html')),
    path('industry_affiliation', TemplateView.as_view(template_name='index.html')),
    path('career', TemplateView.as_view(template_name='index.html')),
    path('basic', TemplateView.as_view(template_name='index.html')),
    path('workspace', TemplateView.as_view(template_name='index.html')),
    path('my_workspace', TemplateView.as_view(template_name='index.html')),
    path('workspace-details', TemplateView.as_view(template_name='index.html')),
    path('job_application', TemplateView.as_view(template_name='index.html')),
    path('create_task', TemplateView.as_view(template_name='index.html')),
    path('assign-task', TemplateView.as_view(template_name='index.html')),
    path('view-task', TemplateView.as_view(template_name='index.html')),
    path('add-member', TemplateView.as_view(template_name='index.html')),
    path('create-project', TemplateView.as_view(template_name='index.html')),
    path('my-project', TemplateView.as_view(template_name='index.html')),
    path('job-preference', TemplateView.as_view(template_name='index.html')),
    path('certification', TemplateView.as_view(template_name='index.html')),
    path('', TemplateView.as_view(template_name='index.html')),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
