from django import forms
from .models import Recipe, Memo

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        labels = {'title': '料理名', 'image': '写真','content': '説明', 'zairyou': '材料'}
    
class MemoForm(forms.ModelForm):
    class Meta:
        model = Memo
        fields = '__all__'