from rest_framework import serializers
from IDBM_app.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"
        # fields = ['name', 'description']
        # exclude = ['active']

    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("name and description is not be same!!!")
        return data

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("name is too short!")
        return value

#
# def name_length(value):
#     if len(value) < 3:
#         raise serializers.ValidationError("name is too short!")
#
#
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
#
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
#
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("name and description must be different!!! ")
#         else:
#             return data

# def validate_name(self, value):
#     if len(value) < 3:
#         raise serializers.ValidationError("Name is too short!")
#     else:
#         return value
