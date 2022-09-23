from rest_framework import serializers
from workspace.models import work_space,work_space_tag

# class work_spaceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=work_space
#         fields='__all__'





class work_spaceSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(many=True, slug_field='tag_name', read_only=True)
    update_tags = serializers.ListField(
        child=serializers.CharField(max_length=30), write_only=True)

    class Meta:
        model = work_space
        exclude = ()

    def create(self, validated_data):
        tag_names = validated_data.pop('update_tags')
        instance = super().create(validated_data)
        tags = []
        for name in tag_names:
            tag, created = work_space_tag.objects.get_or_create(tag_name=name)
            tags.append(tag)
        instance.tags.set(tags)
        return instance

    # def update(self, instance, validated_data):
    #     tag_names = validated_data.pop('update_tags')
    #     instance = super().update(instance, validated_data)
    #     tags = []
    #     for name in tag_names:
    #         tag, created = work_space_tag.objects.get_or_create(name=name, defaults={'created_by': user})
    #         tags.append(tag)
    #     instance.tags.set(tags)
    #     return instance        