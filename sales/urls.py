from django.urls.conf import path
from .views import 세일_지우기, 세일_업데이트, 세일_입력, 세일목록, 세일상세

app_name = '세일목록1' # namespace과 이름 지정이 달라도 상관 없음

urlpatterns = [
    path('', 세일목록, name='목록'),
    path('<int:pk>/', 세일상세, name='상세'),
    path('make/', 세일_입력, name='생성'),
    path('<int:pk>/update/', 세일_업데이트, name='업뎃'),
    path('<int:pk>/delete/', 세일_지우기, name='지우기'),
]