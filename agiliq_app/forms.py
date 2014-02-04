from django import forms


class CommentForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'title': 'Your Name', }))
    email = forms.EmailField(
        max_length=100,
        widget=forms.TextInput(attrs={'title': 'Your Email', }))
    description = forms.CharField(widget=forms.Textarea)
