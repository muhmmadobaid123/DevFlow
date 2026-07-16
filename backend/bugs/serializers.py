from rest_framework import serializers


class BugSerializer(
    serializers.Serializer
):

    id = serializers.CharField(
        required=False
    )

    task_id = serializers.CharField()

    title = serializers.CharField()

    description = serializers.CharField()

    reported_by = serializers.CharField()

    assigned_to = serializers.CharField()

    severity = serializers.CharField()

    status = serializers.CharField(
        required=False
    )