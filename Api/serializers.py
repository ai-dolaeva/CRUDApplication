from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ModelSerializer
from Api.models import User
import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class UserSerializer(ModelSerializer):
    """
    Serializer for conversion data of the User table
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'password',
                  'is_active', 'last_login', 'is_superuser',)
        read_only_fields = ('id', 'last_login', 'is_superuser',)
        extra_kwargs = {
            'password': {'write_only': True},
            'is_active': {'default': True},
        }

    def validate_username(self, value):
        """
        Validation of the username field
        """
        if not re.findall(r'^[\w.@+-]+$', value):
            raise ValidationError(
                _('Letters, digits and characters @.+-_ only'),
                code='invalid username',
            )
        return value

    def validate_password(self, value):
        """
        Validation of the password field
        """
        if not re.findall(r'^(?=.*[A-Z])(?=.*\d).{8,}$', value):
            raise ValidationError(
                    _('8 or more symbols including an uppercase letter and'
                      'a digit'),
                    code='invalid password',
                )
        return value

    def create(self, validated_data):
        """
        Create user in the User model
        """
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        """
        Update user in the User model
        """
        instance.username = validated_data.get('username', instance.username)
        instance.password = make_password(validated_data.get('password',
                                                             instance.password)
                                          )
        instance.first_name = validated_data.get('first_name',
                                                 instance.first_name)
        instance.last_name = validated_data.get('last_name',
                                                instance.last_name)
        instance.is_active = validated_data.get('is_active',
                                                instance.is_active)
        instance.save()
        return instance
