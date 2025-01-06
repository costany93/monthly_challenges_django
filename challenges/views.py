from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# from django.template.loader import render_to_string

monthly_challenges = {
    "janvier": "Faire du sport pendant tout le mois",
    "fevrier": "Faire beaucoup de cardion afin de perdre du poids au moins 2 kilo",
    "mars": "Preparer ses objectifs pour l'ete",
    "avril": "Boire beaucoup d'eau",
    "mai": "Visiter un musee",
    "juin": "Apprendre angular",
    "juillet": "Lire 3 livres",
    "aout": "Manger beaucoup de poisson",
    "septembre": "Beaucoup nager",
    "octobre": "Visiter de regions du pays",
    "novembre": "Apprendre une nouvelle competence",
    "decembre": None,

}

# Create your views here.

# definissons notre fonction index


# def index(request):
#     return HttpResponse("It's working")

# # ici on definit un fonction qui retourne un url static
# def fevrier(request):
#     return HttpResponse("Fevrier")

def index(request):
    list_item = ""
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge(request, month):
    # ici on teste si le moiss passer en parametre d'url est  dans notre liste de mois
    try:
        challenge_text = monthly_challenges[month]
        # ici on definit la reponse dans notre templates challenges/templates/challenge.html
        return render(request, 'challenges/challenge.html', {
            "text": challenge_text,
            "month": month
        })

        # response_data = render_to_string("challenges/challenge.html")
        return HttpResponse(response_data)
    except:
        # ici nous affichons la page 404
        raise Http404()


# ici on definit un fonction qui retourne des url dynamique, le parametre month est aussi defini comme le nom de notre url dans le fichier urls
# C'EST LA FONCTION DU HAUT MAIS SANS AVOIRR UTILISER UNE LISTE PYTHON
# def monthly_challenges(request, month):
#     # ici om va passer dynamiquement un nos objectfis en fonction des mois
#     challenge_text = None
#     if month == "janvier":
#         challenge_text = "Faire du sport pendant tout le mois"
#     elif month == "fevrier":
#         challenge_text = "Faire beaucoup de cardion afin de perdre du poids au moins 2 kilo"
#     elif month == "mars":
#         challenge_text = "Preparer ses objectifs pour l'ete"
#     else:
#         challenge_text = "Les mois n'est pas encore prit en charge"
#     return HttpResponse(challenge_text)

# ici nous definissons notre fonction qui recoit a la place du mois en lettre, le moiss en chiffre en formattant son url a ne recevoir que les chiffres


def monthly_challenges_by_month(request, month):
    # ici on recupere les cles de notre liste(janvier, fevrier, etc...)
    months = list(monthly_challenges.keys())
    # ici on teste si nous pasons un nombre qui n'est pas valide en fonction du mois
    if month > len(months):

        return HttpResponseNotFound("Le mois entrer n'existe pas")
        # ici je vais faire matcher les cles rrecuperes avec l'arguments passer dans la requette
    recup_month = months[month - 1]

    # ici on utilise un named url afin de dynamiser le site
    url_month = reverse("month-challenges", args=[recup_month])
    return HttpResponseRedirect(url_month)
    # ici je redirige l'utilisateur en fonction du mois en chiffre passer comme argument a la page qu'il faut
