from .models import categories, product, Added_by
from rest_framework import serializers


class AddedBySerializer(serializers.ModelSerializer):
    class Meta:
        model = Added_by
        fields = '__all__'
        read_only_fields = ('items',)


class ProductSerializer(serializers.ModelSerializer):

    user_data = AddedBySerializer(many=True, source='user_list')
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = product
        fields = ['name','type', 'price', 'tax','total_price', 'user_data']

    def get_total_price(self, obj):
        return obj.price + (obj.price * obj.tax // 100)

    def create(self, validated_data):
        users = validated_data.pop('user_list')  # {"user": "guna", "items": 4 }
        products = product.objects.create(**validated_data)

        for i in users:
            Added_by.objects.create(items=products, **i)

        return products

# def userMethod(user, items):
#     return Added_by.objects.create(user=user,items=items)


class CategorySerializer(serializers.ModelSerializer):
    product_list = ProductSerializer(many=True)


    class Meta:
        model = categories
        fields = ['id','category', 'product_list']
    #
    # def create(self, validated_data):
    #     name = self.validated_data.get('name')
    #     type = self.validated_data.get('type')
    #     price = self.validated_data.get('price')
    #     print(price)
    #     tax = self.validated_data.get('tax')
    #     print(tax)
    #     value = price + (price * tax // 100)
    #     print(value)
    #     products = product.objects.create(name=name, price=price, tax=tax, total_price=value, type=type)





