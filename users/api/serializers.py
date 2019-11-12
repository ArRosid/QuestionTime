from rest_framework import serializers
from users import models as um

class UserDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = um.CustomUser
        fields = ["username"]