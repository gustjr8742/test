from django import forms
from .models import Blog, Comment

class BlogForm(forms.Form):
    # 내가 입력받고자 하는 값들
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)

class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        # 블로그 클래스 안에 있는 title, body, date가 전부다 form의 대상이 되게 하는것 ==> # fields = '__all__'
        #fields = ['title', 'body'] #블로그 클래스 안에있는 특정 데이터 넣는것
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']