from django.contrib import admin
from django.urls import path,include

from blog import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # http://127.0.0.1:8000/blog/
    path('blog/', include('blog.urls')),

    # http://127.0.0.1:8000
    path("", views.posts_list,name="index"),

    path('user/', include('user.urls')),

    # 로그인, 로그아웃은 장고 이용
    path("accounts/", include("django.contrib.auth.urls")),    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

