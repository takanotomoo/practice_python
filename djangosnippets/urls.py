from django.contrib import admin
from django.urls import path, include # include関数の追加でインポート

from snippets.views import top

urlpatterns = [
    path('', top, name='top'),
    path('snippets/', include('snippets.urls')), # snippets/urls.pyの読み込み
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),
]
