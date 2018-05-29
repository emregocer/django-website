from django import forms

class CreateTopicForm(forms.Form):
    topic_subject = forms.CharField(max_length=255)
    topic_content = forms.CharField(widget=forms.Textarea)