from django.urls import path

# on import du dossiers courant notre fichier views
from . import views

# ici on defini nos urls
urlpatterns = [
    # ici on definit notre url janvier qui est attachee a notre vu index du dossier challenge, c'est un url static
    # path("janvier", views.index),
    # path("fevrier", views.fevrier)


    # ici on aura que les entier comme parametres acceptables NB ici il s'agit d'uune route ou d'un url non nommee no-named url
    #  path("<int:month>", views.monthly_challenges_by_month),
    # ici travaillant avec un named url
    path("<int:month>", views.monthly_challenges_by_month),
    # par defaut cette config d'url sans str pouvait revoir tout type de donnee qui pouvait etre passee en formattant avec le str cette url ne pourra plus que recevoir les string en parametre. NB ici il s'agit d'uune route ou d'un url non nommee no-named url
    path("<str:month>", views.monthly_challenge, name="month-challenges"),
    path("", views.index, name="challenges-index")



]

# nous devons rendre cette url disponible dans toute notre application on l'ajoutant au fichier urls du dossier principal de notre application(monthly_challenges)
