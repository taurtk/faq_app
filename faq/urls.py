from django.urls import path
from .views import FAQList, QueryView

urlpatterns = [
    path('', FAQList.as_view(), name='faq-list'),  # This matches /api/faqs/
    path('query/', QueryView.as_view(), name='query-faq'),  # This matches /api/query/
]