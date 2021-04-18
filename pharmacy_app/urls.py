from django.urls import path
from . import views,urls
from django.conf import settings

urlpatterns = [
    path('', views.index,name="index"),
    path('login', views.login ,name="login"),
    path('signup', views.signup ,name="signup"),
    path('schedule1', views.schedule1 ,name="schedule1"),
    path('schedule2', views.schedule2 ,name="schedule2"),
    path('schedule3', views.schedule3 ,name="schedule3"),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   