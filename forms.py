from django import forms
from blog.models import BlogPost

JOBS = (
    ("Python", "Développeur Python"),
    ("JavaScript", "Développeur JavaScript"),
    ("Csharp", "Développeur Csharp")
)

class SignupForm(forms.Form):
    pseudo = forms.CharField(max_length=8, required=False)
    email = forms.EmailField()
    password = forms.CharField(min_length=6, widget=forms.PasswordInput())
    job = forms.ChoiceField(choices=JOBS)
    cgu_accept = forms.BooleanField(initial=True)

    # Control côté server des data saisies dans un champ du formulaire
    def clean_pseudo(self):
        pseudo = self.cleaned_data.get("pseudo")
        # on ne veut pas qu'il y '$' dans le pseudo
        if "$" in pseudo:
            raise forms.ValidationError("Le pseudo ne doit pas contenir $ !!!")
        return pseudo

# Cas du formulaire lié au modèle BlogPost
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        # Si l'on veut que notre formulaire contient tous les champs du modèle, on fera fields = "__all__"
        # Liste des champs du modèle à afficher dans le formulaire
        fields = [
            "title",
            "date",
            "category",
            "content",
            "description",
        ]

        # Personnalisation des champs du formulaire
        labels = {
            "title": "Titre",
            "category": "Catégorie"
        }

        widgets = {
            "date": forms.SelectDateWidget(years=range(2000,2050))
        }