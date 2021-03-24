
from django.contrib import admin
from django.urls import path
from blogapp import views
from account import views as account_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    
    # html form을 이용해 블로그 객체 만들기
    path('new/', views.new, name = 'new'),
    path('create/', views.create, name = 'create'),

    # django form을 이용해 블로그 객체 만들기
    path('formcreate/', views.formcreate, name = 'formcreate'),
    
    # django modelform을 이용해 블로그 객체 만들기
    path('modelformcreate/', views.modelformcreate, name = 'modelformcreate'),

    # 127.0.0.1:8000/detail/1 디테일 페이지 첫번째
    # 127.0.0.1:8000/detail/2 두 번째
    # 127.0.0.1:8000/detail/3 세 번째
    path('detail/<int:blog_id>', views.detail, name = 'detail'), 
    # <(정수형) : blog_id라는 변수는 detail 함수에 넘길 값을 담는다는 뜻.> 


    # 댓글 부분
    path('create_comment/<int:blog_id>', views.create_comment, name = 'create_comment'),

    #로그인 부분
    path('login/', account_views.login, name = 'login'),

    #로그아웃 부분
    path('logout/', account_views.logout, name = 'logout'),
]
# media 파일에 접근할 수 있는 url을 추가해야함
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)



