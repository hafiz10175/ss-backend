from rest_framework import serializers

from ss_backend.apps.howto.models import Note


class HowToSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = "__all__"
