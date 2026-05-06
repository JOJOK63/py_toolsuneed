from rest_framework import serializers

from budget.models import Category


class CategorySerializer(serializers.ModelSerializer[Category]):
    class Meta:
        icon = serializers.ImageField(
            required=False,
            allow_null=True,
            use_url=True  # retourne l'URL en lecture
        )
        model = Category
        fields = '__all__'
        read_only_fields = ('id',)
