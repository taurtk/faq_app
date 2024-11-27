from rest_framework import generics, status
from rest_framework.response import Response
from .models import FAQ
from .serializers import FAQSerializer
import openai  # Assuming OpenAI's library is installed

class FAQList(generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

class QueryView(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        query = request.data.get("query")
        # Check for matching FAQs based on keywords or text similarity
        faqs = FAQ.objects.filter(keywords__contains=query)  # Simple keyword match
        
        if faqs.exists():
            answer = faqs.first().answer
            return Response({"answer": answer}, status=status.HTTP_200_OK)
        
        # If no match found, query LLM (OpenAI GPT)
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": query}]
            )
            answer = response['choices'][0]['message']['content']
            return Response({"answer": answer}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "The system is temporarily unavailable. Please try again later."}, status=status.HTTP_503_SERVICE_UNAVAILABLE)