from rest_framework import serializers
from comment.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user

        # تنظیم is_reply در صورت وجود پاسخ
        if validated_data.get('reply'):
            validated_data['is_reply'] = True

        return super().create(validated_data)
