from rest_framework.views import APIView
from rest_framework.response import Response
from decimal import Decimal

from share.api.serializers import ShareSerializer
from share.models import ShareModel


class ShareUpdateView(APIView):
    # queryset = ShareModel.objects
    # serializer_class = ShareSerializer

    def update_or_create_share(self, data):
        share_code = data.get('code')
        if share := ShareModel.objects.filter(code=share_code).first():
            print(f'updated {share}')
            share.graphic = data.get('graphic')
            share.current_price = data.get('current_price')
            share.last_updated = data.get('last_updated')
        else:
            share_model = ShareModel()
            share_model.code = share_code
            print(f'create {share_model.code}')
            share_model.graphic = data.get('graphic')
            share_model.current_price = data.get('current_price')
            share_model.last_updated = data.get('last_updated')
            share_model.save()

    def post(self, request, *args, **kwargs):
        if sync_list := request.data.get('sync_list'):
            for sync_code in sync_list:
                self.update_or_create_share(sync_code)
        else:
            self.update_or_create_share(request.data)
        return Response({'message': 'success'})

