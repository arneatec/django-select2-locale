from django import forms
from .models import Post
from django_select2 import forms as s2forms


class TopicWidget(s2forms.ModelSelect2Widget):

    search_fields = [
        "name__icontains",
        "description__icontains",
    ]


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author',
                  'topic',
                  'title',
                  'text',
                  )
        widgets = {
            "topic": TopicWidget,
        }
