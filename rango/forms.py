from django import forms 
from django.contrib.auth.models import User
from rango.models import Page, Category,UserProfile
from django.forms import extras


class CategoryForm(forms.ModelForm):

    name = forms.CharField(max_length=128,
    help_text="Please enter the category name.")
             
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)


class PageForm(forms.ModelForm):

    message = forms.CharField(max_length=1024,
                              help_text="Please enter the comment for the game.")
    evaluation = forms.IntegerField(initial=0,
                            help_text="Please enter your evaluation for the game.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Page
        exclude = ('category',)


class UserForm(forms.ModelForm): 
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User 
        fields = ('username', 'email', 'password', 'last_name', 'first_name')


class UserProfileForm(forms.ModelForm):
    age = forms.IntegerField(required=True)
    website = forms.URLField(required=False)
    picture = forms.ImageField(required=False)

    class Meta:
        model = UserProfile 
        exclude = ('user', )


