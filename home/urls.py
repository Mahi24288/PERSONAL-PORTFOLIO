from django.contrib import admin
from django.urls import path,include
from home import views
# django admin header customization
admin.site.site_header = "Developer Mahesh"
admin.site.site_title = "welcome to DashBoard"
admin.site.index_title = "welcome to this portal"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('project', views.project, name='project')

]
