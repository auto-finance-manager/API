from rest_framework.views import APIView
from rest_framework.response import Response
from share.models import ShareModel


class ShareUpdateView(APIView):
    @staticmethod
    def update_or_create_share(data):
        share_code = data.get('code')
        print(f'share_code: {share_code}')
        if share := ShareModel.objects.filter(code=share_code).first():
            share.graphic = data.get('graphic')
            share.title = data.get('title')
            share.logo = data.get('logo')
            share.current_price = data.get('current_price')
            share.last_updated = data.get('last_updated')
            share.save()
        else:
            share_model = ShareModel()
            share_model.code = share_code
            share_model.title = data.get('title')
            share_model.logo = data.get('logo')
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

