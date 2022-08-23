from rest_framework import serializers
from watch_list_app.models import WatchList, StreamPlatform, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = ('watchlist',)
        # fields = "__all__"

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("your rating is not valid!!!")
        return value


class WatchListSerializer(serializers.ModelSerializer):
    review = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = WatchList
        fields = "__all__"

    def validate(self, data):
        if data['title'] == data['storyline']:
            raise serializers.ValidationError("Your title and storyline must be different!")
        return data

    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("your title is too short!!!")
        return value


class StreamPlatformSerializer(serializers.ModelSerializer):
    # watchlist = WatchListSerializer(many=True, read_only=True)
    # watchlist = serializers.StringRelatedField(many=True)
    # watchlist = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='watch-list-details')

    class Meta:
        model = StreamPlatform
        fields = "__all__"

    def validate(self, data):
        if data['name'] == data['about']:
            raise serializers.ValidationError("Your name and about must be different!")
        return data

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("your name is too short!!!")
        return value

# from watch_list_app.models import Movie

#
# class MovieSerializer(serializers.ModelSerializer):
#     len_name = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Movie
#         fields = "__all__"
#         # fields = ['name', 'description']
#         # exclude = ['active']
#
#     def get_len_name(self, object):
#         length = len(object.name)
#         return length
#
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("name and description is not be same!!!")
#         return data
#
#     def validate_name(self, value):
#         if len(value) < 3:
#             raise serializers.ValidationError("name is too short!")
#         return value

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
