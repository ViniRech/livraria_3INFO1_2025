from rest_framework.serializers import CharField, ModelSerializer

from core.models import Compra


class CompraSerializer(ModelSerializer):
    usuario_email = CharField(source='usuario.email', read_only=True)
    usuario_name = CharField(source='usuario.name', read_only=True)
    status = CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Compra
        fields = ('id', 'usuario_name', 'usuario_email', 'status')
