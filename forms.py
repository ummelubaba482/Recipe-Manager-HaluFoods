# # from django import forms
# # from .models import Recipe
# # from django.contrib.auth.forms import UserCreationForm
# # from django.contrib.auth.models import User
# #
# # class RecipeForm(forms.ModelForm):
# #     class Meta:
# #         model = Recipe
# #         fields = ['title', 'description', 'ingredients', 'instructions']
# #
# # class SignUpForm(UserCreationForm):
# #     class Meta:
# #         model = User
# #         fields = ['username', 'password1', 'password2']
#
#
# from django import forms
# from .models import Recipe
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
#
# class RecipeForm(forms.ModelForm):
#     class Meta:
#         model = Recipe
#         fields = ['title', 'description', 'ingredients', 'instructions']
#
# class SignUpForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password1', 'password2']



from django import forms
from .models import Recipe
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'instructions', 'image']

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']