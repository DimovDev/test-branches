from rest_framework import serializers

from user import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView."""

    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects."""

    # reci Djangu koji model zelim
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Create and return a new user."""

        user = models.UserProfile(
            email = validated_data['email'],
            name = validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """A serializer for profile feed items."""

    class Meta:
        model = models.StatusUpdate
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}

class ProfileMessage(serializers.HyperlinkedModelSerializer):
    """A serializer for profile feed items."""

    class Meta:
        model = models.Message
        fields = ( 'id','sender', 'recipient', 'message', 'date_sent')
        # extra_kwargs = {'sender': {'read_only': True}, 'date_sent': {'read_only': True}}
        read_only_fields = ['sender']

        def create(self, ):
            """Create and return a new user."""

            message = models.Message(
            #     sender=validated_data['sender'],
            #     recipient=validated_data['validated_data']
            )

            # user.set_password(validated_data['password'])
            # message.save()
            message.save(using=self._db)
            return message
# using=self._db