
from rest_framework import serializers
from snippets.models import Snippet
from django.contrib.auth.models import User


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(lookup_field="pk", view_name='snippets:snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('url', 'id', 'highlight', 'owner', 'title', 'code', 'linenos', 'language', 'style')
        extra_kwargs = {
            'url': {'view_name': 'snippets:snippet-detail', 'lookup_field': 'pk'},
        }


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(lookup_field="pk", many=True, view_name='snippets:snippet-detail', read_only=True)
    # snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippets:snippet-detail',
    #                                                lookup_field="",
    #                                                lookup_url_kwarg="", read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='snippets:user-detail', lookup_field='pk')

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets')
        # extra_kwargs = {
        #     'url': {'view_name': 'snippet:user-detail', 'lookup_field': 'pk'},
        # }

# from rest_framework import serializers
# from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

# from django.contrib.auth.models import User

# # Using Hyperlink Serializer

# class SnippetSerializer(serializers.HyperlinkedModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.username')
#     highlight = serializers.HyperlinkedIdentityField(view_name='snippets:snippet-highlight', format='html', lookup_field='id')

#     class Meta:
#         model = Snippet
#         fields = ['url', 'id', 'highlight', 'owner',
#                   'title', 'code', 'linenos', 'language', 'style']


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippets:snippet-detail', read_only=True, lookup_field='id')

#     class Meta:
#         model = User
#         fields = ['url', 'id', 'username', 'snippets']

# Using Model Serializer
# class UserSerializer(serializers.ModelSerializer):
#     snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

#     class Meta:
#         model = User
#         fields = ['id', 'username', 'snippets']


# class SnippetSerializer(serializers.ModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.username')
#
#     class Meta:
#         model = Snippet
#         fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner']


# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Snippet.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance