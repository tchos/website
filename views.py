from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime
from django.views import  View
from django.views.generic import TemplateView

from .forms import SignupForm, BlogPostForm

"""Méthode CBV"""
class HomeView(TemplateView):
    template_name = "index.html"
    title = "Default"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        return context


        
    """
    def get(self, request):
        return HttpResponse(f"<h1>{self.title}</h1><br>")
    """
def home(request):
    return HttpResponse("Accueil")

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        # On s'assure que les data du formulaire sont valides
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponse("Merci de vous être inscrit au site !!!")
    else:
        # Création du formulaire de création du compte à afficher dans la page signup.html
        form = SignupForm()
    return render(request, "accounts/signup.html", context={"formulaire": form})

def blog_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        # On s'assure que les data du formulaire sont valides
        if form.is_valid():
            # Enregistre les data du formulaire sans les sauvegarder en BD pour permettre de modifier la valeur de certains champs
            blog_post = form.save(commit=False)
            blog_post.published = True
            # Enregistre les data du formulaire en BD
            blog_post.save()

        # redirection vers la même page qui permet de créer un article
        return HttpResponseRedirect(request.path)
    else:
        init_values = {}
        if request.user.is_authenticated:
            # Par défaut c'est le user connecté qui sera l'auteur de l'article
            init_values['author'] = request.user
        # Par défaut c'est la date du jour qui sera la date à laquelle l'article a été créé
        init_values['date'] = datetime.today()
        # formulaire d'ajout d'un article
        form = BlogPostForm(initial=init_values)

    return render(request, "website/article_create.html", {"formulaire":form})