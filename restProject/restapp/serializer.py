from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    age = serializers.IntegerField()
    enrollment_date = serializers.DateField()


