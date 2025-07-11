from rest_framework.serializers import CharField, ModelSerializer, SerializerMethodField

from core.models import Compra, ItensCompra


class ItensCompraSerializer(ModelSerializer):
    total = SerializerMethodField()

    def get_total(self, instance):
        return instance.livro.preco * instance.quantidade

    class Meta:
        model = ItensCompra
        fields = ('id', 'quantidade', 'livro', 'total')
        depth = 2


class CompraSerializer(ModelSerializer):
    usuario_email = CharField(source='usuario.email', read_only=True)
    usuario_name = CharField(source='usuario.name', read_only=True)
    status = CharField(source='get_status_display', read_only=True)
    itens = ItensCompraSerializer(many=True, read_only=True)

    class Meta:
        model = Compra
        fields = ('id', 'usuario_name', 'usuario_email', 'status', 'total', 'itens')
