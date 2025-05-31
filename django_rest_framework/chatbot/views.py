from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .domain.CONAI_CHATBOT_GPT_PARAMETERS_MST import ConaiChatbotGptParametersMst
from .serializers.conai_chatbot_gpt_parameters_mst_restful_serializer import ConaiChatbotGptParametersMstPostSerializer


class GPTParameterViewSet(viewsets.ModelViewSet):
    queryset = ConaiChatbotGptParametersMst.objects.all()
    serializer_class = ConaiChatbotGptParametersMstPostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.query_params.get("user_id")  # Use query_params to access query parameters
        if user_id:
            # Fetch parameters specific to the user or global parameters
            return ConaiChatbotGptParametersMst.objects.filter(
                user_id=user_id) | ConaiChatbotGptParametersMst.objects.filter(user_id__isnull=True)
        return ConaiChatbotGptParametersMst.objects.filter(
            user_id__isnull=True)  # Fallback to global parameters if no user_id
