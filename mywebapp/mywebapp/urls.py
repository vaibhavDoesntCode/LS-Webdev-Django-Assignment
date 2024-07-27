from django.contrib import admin
from django.urls import path
from authen.views import login_page, register_page, logout_view, home, post_list, post_edit, post_delete, post_create  # Import post-related views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
    path('home/', home, name='home_page'),
    path('admin/', admin.site.urls),
    path('login/', login_page, name='login_page'),
    path('register/', register_page, name='register_page'),
    path('logout/', logout_view, name='logout'),
    path('posts/', post_list, name='post_list'),
    path('posts/create/', post_create, name='create_post'),  # URL for creating a post
    path('posts/edit/<int:post_id>/', post_edit, name='edit_post'),
    path('posts/delete/<int:post_id>/', post_delete, name='delete_post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
