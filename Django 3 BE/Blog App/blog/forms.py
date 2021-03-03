from django import forms

from .models import Comment

class EmailPostForm(forms.Form):
    '''
        Django comes with two base classes to build forms:
        • Form : Allows you to build standard forms
        • ModelForm : Allows you to build forms tied to model instances
    '''
    name        = forms.CharField(max_length=25)
    email       = forms.EmailField()
    to          = forms.EmailField()
    comments    = forms.CharField(required=False, # comments are optional
                                  widget= forms.Textarea) # default Charfield give just <input type="text"> by widget we can change it



class CommentForm(forms.ModelForm):
    class Meta:
        model   = Comment
        fields  = ('name','email','body')
        # exclude = ('updated','active') # if you want to exclude some field use it instead of fields variable

class SearchForm(forms.Form):
    query = forms.CharField()
















