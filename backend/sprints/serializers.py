from rest_framework import serializers


class SprintSerializer(
    serializers.Serializer
):

    id = serializers.CharField(
        required=False
    )

    project_id = serializers.CharField()

    name = serializers.CharField()

    goal = serializers.CharField()

    start_date = serializers.DateTimeField()

    end_date = serializers.DateTimeField()

    status = serializers.CharField(
        required=False
    )