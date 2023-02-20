from django import forms


class MessageForm(forms.Form):
    CHOICES = (
        ('q', 'Pytanie'),
        ('o', 'Inne')
    )

    name = forms.CharField(label="Imię")
    email = forms.EmailField(label="Email")
    category = forms.ChoiceField(choices=CHOICES, label="Kategoria")
    title = forms.CharField(label="Tytuł")
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'rows': 4,
                'cols': 20,
                'class': 'moja',
            }
        ), label="Treść"
    )
