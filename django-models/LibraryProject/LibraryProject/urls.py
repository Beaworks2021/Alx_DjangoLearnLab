from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include the relationship_app URLs
    path('relationship/', include('relationship_app.urls')),
    # You can also include it at the root level if you prefer
    # path('', include('relationship_app.urls')),
]