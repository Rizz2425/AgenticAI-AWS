from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import get_medical_advice 
class ChatbotDoctorView(APIView):
    def post(self, request):
        symptoms = request.data.get('symptoms')
        if not symptoms:
            return Response({"error": "Symptoms are required"}, status=400)
        
        answer = get_medical_advice(symptoms)
        
        return Response({"diagnosis": answer})


def home(request):
    return render(request, 'index.html')
