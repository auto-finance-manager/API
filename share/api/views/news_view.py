from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from django.conf import settings


class NewsView(APIView):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.data)
        if news := data.get("news"):
            with open(settings.BASE_DIR / 'news.json', 'w', encoding='utf-8') as newsf:
                newsf.write(json.dumps(news))
        return Response()
