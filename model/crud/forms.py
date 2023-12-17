from django import forms


class AddForm(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    age = forms.IntegerField()
    # gender = forms.BooleanField()
    birthday = forms.DateField()




class NewsForm(forms.Form):
    title = forms.CharField(max_length=100, label='Название', widget=forms.TextInput(attrs={'class': 'main__input'}))
    content = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'class': 'main__textarea'}))
    is_published = forms.BooleanField(label="Опубликовано", initial=True)
    category = forms.ChoiceField(choices=((1, 'Cпорт'), (2, 'Красота')), label='Категория')