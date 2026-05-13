from typing import Any

from drf_spectacular.extensions import OpenApiSerializerFieldExtension
from drf_spectacular.plumbing import build_basic_type
from drf_spectacular.types import OpenApiTypes
from rest_framework.fields import ImageField


class ImageFieldFix(OpenApiSerializerFieldExtension):
    target_class = 'rest_framework.fields.ImageField'

    def map_serializer_field(self, auto_schema: Any, direction: str) -> dict[str, Any]:
        if direction == 'request':
            return {'type': 'string', 'format': 'binary'}  # ← file upload
        return build_basic_type(OpenApiTypes.URI)  # type: ignore[return-value]
