from rest_framework import serializers

from budget.models import Category, Budget, FinancialTransaction
from budget.models import Subcategory


class CategorySerializer(serializers.ModelSerializer[Category]):
    # For DRF Spectacular files add
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
    # For DRF Spectacular files add
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


class FinancialTransactionSerializer(serializers.ModelSerializer[FinancialTransaction]):
    # For DRF Spectacular dropdown
    subcategory_detail: SubcategorySerializer = SubcategorySerializer(
        source='subcategory',
        read_only=True
    )

    class Meta:
        model = FinancialTransaction
        fields = [
            'id', 'name', 'amount', 'detail', 'transaction_type',
            'created_at', 'updated_at', 'budget', 'subcategory',
            'subcategory_detail'
        ]
        read_only_fields = ('id', 'created_at', 'updated_at')
