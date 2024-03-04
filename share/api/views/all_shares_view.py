from rest_framework.generics import ListAPIView
from share.models import ShareModel
from share.api.serializers import ShareSerializer


class AllSharesView(ListAPIView):
    queryset = ShareModel.objects
    serializer_class = ShareSerializer
