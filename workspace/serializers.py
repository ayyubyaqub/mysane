from rest_framework import serializers
from workspace.models import work_space,work_space_tag,project,Task

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




class projectSerializer(serializers.ModelSerializer):
    class Meta:
        model=project
        fields=['id','user','title','description','project_category','open_positions','start_date','due_Date','estimated_budget',]
        extra_kwargs = {'id':{'read_only':True}}
        

    def create(self, validated_data):
        Project=project.objects.create(user=validated_data['user'], title=validated_data['title'],
        description=validated_data['description'], project_category=validated_data['project_category'], open_positions=validated_data['open_positions'], start_date=validated_data['start_date'],due_Date=validated_data['due_Date'], estimated_budget=validated_data['estimated_budget'])
        Project.save()
        return Project

    def update(self, instance, validated_data):
        instance.title=validated_data.get('title',instance.title)
        instance.description=validated_data.get('description',instance.description)       
        instance.project_category=validated_data.get('project_category',instance.project_category)
        instance.open_positions=validated_data.get('open_positions',instance.open_positions)
        instance.start_date=validated_data.get('start_date',instance.start_date)
        instance.due_Date=validated_data.get('due_Date',instance.due_Date)
        instance.estimated_budget=validated_data.get('estimated_budget',instance.estimated_budget)
        instance.save()
        return instance     




class taskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields=['id','user','name','description','start_date','due_Date','priority',]
        extra_kwargs = {'id':{'read_only':True}}
        



    def create(self, validated_data):
        task=Task.objects.create(user=validated_data['user'], name=validated_data['name'],
        description=validated_data['description'], start_date=validated_data['start_date'],due_Date=validated_data['due_Date'], priority=validated_data['priority'])
        task.save()
        return task

    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.description=validated_data.get('description',instance.description)       
        instance.start_date=validated_data.get('start_date',instance.start_date)
        instance.due_Date=validated_data.get('due_Date',instance.due_Date)
        instance.priority=validated_data.get('priority',instance.priority)
        instance.save()
        return instance    
