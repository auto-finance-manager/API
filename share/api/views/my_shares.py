from share.models import ShareOwnershipModel
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from share.models import ShareOwnershipModel
from share.api.serializers import ShareOwnershipSerializer


class MyShare(ListAPIView):
    serializer_class = ShareOwnershipSerializer
    queryset = ShareOwnershipModel.objects.all()

    # def get(self, request):
    #     share_owner = ShareOwnershipModel.objects.all()

