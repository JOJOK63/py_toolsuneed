from rest_framework import serializers

from budget.models import Category, Budget
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

    # EN LECTURE SEULEMENT → on renvoie l'objet Category complet
    # source='category' dit à DRF d'aller chercher le champ 'category' du model
    category_detail = CategorySerializer(source='category', read_only=True)

    class Meta:
        model = Subcategory
        fields = ['id', 'name', 'icon', 'category', 'category_detail']
        read_only_fields = ('id',)


class BudgetSerializer(serializers.ModelSerializer[Budget]):
    class Meta:
        model = Budget
        fields = '__all__'
        read_only_fields = ('id', 'user')
