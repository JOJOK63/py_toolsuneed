from rest_framework import serializers

from budget.models import Category


class CategorySerializer(serializers.ModelSerializer[Category]):
    class Meta:
        model = Category
        fields = '__all__'
        exclude = ['']
        read_only_fields = ('id',)
