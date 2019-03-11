from rest_framework import serializers
from .models import Story, Author

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ("__all__")


class AuthorSerializer(serializers.ModelSerializer):
    #user = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Author
        fields = ("__all__")
