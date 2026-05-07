from rest_framework import serializers

from budget.models import Category
from budget.models import Subcategory


class CategorySerializer(serializers.ModelSerializer[Category]):
    icon = serializers.ImageField(
        required=True,
        allow_null=False,
        use_url=True  # retourne l'URL en lecture
    )
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ('id',)


class SubcategorySerializer(serializers.ModelSerializer[Subcategory]):
    icon = serializers.ImageField(
        required=True,
        allow_null=False,
        use_url=True
    )
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Subcategory
        fields = '__all__'
        read_only_fields = ('id',)
