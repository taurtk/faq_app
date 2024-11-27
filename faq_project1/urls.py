from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/faqs/', include('faq.urls')),  # Ensure this line is correct
    path('api/query/', include('faq.urls')),  # This should be changed
]