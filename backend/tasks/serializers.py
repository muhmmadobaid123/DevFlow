from rest_framework import serializers


class TaskSerializer(
    serializers.Serializer
):

    id = serializers.CharField(
        required=False
    )

    sprint_id = serializers.CharField()

    title = serializers.CharField()

    description = serializers.CharField()

    assigned_to = serializers.CharField()

    priority = serializers.CharField()

    status = serializers.CharField(
        required=False
    )