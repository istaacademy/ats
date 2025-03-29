from rest_framework import serializers
from course.models import Course, CourseUserModel


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')




class CourseRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseUserModel
        fields = ["course", "relation"]
        read_only_fields = ('created_at', 'updated_at')


    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)



