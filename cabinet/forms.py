from django import forms
from cabinet.models import Image, Author

# class AuthorForm(forms.Form):
#     sur_name = forms.CharField(max_length=200)
#     name = forms.CharField(max_length=200)
#     username = forms.CharField(max_length=200)

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = "__all__"