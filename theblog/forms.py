from django import forms
from .models import Post, Category, Profile,Comment

# choices = [('coding','coding'),('sports','sports'),('entertaiment','entertaiment')]


class PostForm(forms.ModelForm):
    class Meta:

        choices = Category.objects.all().values_list('name','name')
        choices_list = [l for l in choices]

        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body', 'header_image')
        
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'This is the Title'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control' }),
            'author': forms.TextInput(attrs={'class':'form-control' ,'id':'elder', 'type':'hidden'}),
            # 'author': forms.Select(attrs={'class':'form-control'}),
            'category': forms.Select(choices=choices_list, attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')
        
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'This is the Title'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control'}),
            # 'author': forms.Select(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }
# class EditProfile(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('user','profile_pic')