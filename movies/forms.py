from django import forms
from django.forms import widgets
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        numbers = (
            ('1','1 Star'),
            ('2','2 Star'),
            ('3','3 Star'),
            ('4','4 Star'),
            ('5','5 Star'),
        )
        model = Comment
        # fields = ['full_name','email','text','rating']
        exclude = ['movie','date_added',]
        labels = {
            "full_name":"Name Surname",
            "email": "E-Mail",
            "text": "Comment",
            "rating": "Rating"
        }
        widgets = {
            "full_name": widgets.TextInput(attrs={"class":"form-control"}),
            "email": widgets.EmailInput(attrs={"class":"form-control"}),
            "text": widgets.Textarea(attrs={"class":"form-control"}),
            "rating": widgets.Select(attrs={"class":"form-control custom-select"}, choices= numbers),
        }