from rest_framework import serializers


class ProjectSerializer(
    serializers.Serializer
):

    id = serializers.CharField(
        required=False
    )

    name = serializers.CharField()

    description = serializers.CharField()

    manager_id = serializers.CharField()

    status = serializers.CharField(
        required=False
    )