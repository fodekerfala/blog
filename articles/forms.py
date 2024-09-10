from django import forms
from .models import Articles,Categories,Comment


class FormArticle(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ['title','sumary','content','categorie','date_pub','imagearticle','publiche']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'sumary':forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control'}),
            'categorie':forms.Select,
            'date_pub':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'publishe':forms.RadioSelect(choices=[(True,'Oui'),(False,'Non')])
        }


class FormCategories(forms.ModelForm):
    class meta:
        model = Categories
        fields = ['title']
        widgets= {
            'title':forms.TextInput(attrs={'class':'form-control'})
        }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields= ('comment', )
        widgets = {
            'comment':forms.Textarea(attrs={'class':'form-control'})
        }
