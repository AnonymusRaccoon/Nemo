import os

TOKEN = os.environ["NEMO_TOKEN"] 

CATEGORY_NAME = "EVENTS"
ORGANIZATION_NAME = "organisation"



HELP_MSG = """Blop... Blop... Bonjour, je suis Nemo, le poisson qui a plus de mémoire que toi. Voici les actions que je peut faire :

__**Actions pour les utilisateurs:**__

Je peux aussi créer des votes aux réponse Oui ou Non pour vos message. Pour cela, ajouter a la fin de vos message```:vote:```
Ca fonctionne aussi pour des votes a 4 choix. Pour cela, ajouter a la fin de vos message```:vote-4:```

__**Actions pour tous les events:**__

Ouvrir l'event a tous le monde```!open [message]```
Rendre l'event privé et inviter les personnes individuellement```!private```
Renomer le channel de l'event```!name [nom-sans-espace]```
Stopper l'event```!stop```

__**Actions pour les events privée:**__

Ajouter quelqu'un sur la liste des participants ```!invite @username [@username ...]```
Enlever un joueur de la liste des participants```!kick @username [@username ...]``` 
Ajouter un organisateur : ```!colab @username [@username ...]```

@username correspond a un utilisateur, par exemple @Me et ce qui se trouve entre crochets est optionel.
 """



EVENT_LIST = """**Liste des events ouverts:**

**Aucun event ouvert.**
"""
LIST_KEY = "Liste des events ouverts"
EMPTY_KEY = "Aucun event ouvert"
EMPTY_SLOT = "Aucun event sur ce slot."

CREATE_MSG = """**Créer un event: ** 
Pour créer un event, click sur ✅
"""
CREATE_KEY = "Créer un event"

CONFIGURING_EVENT = "@User configure l'event."
EVENT_CONFIGURING_KEY = "configure l'event."

PRIVATE_EVENT = "L'event est privé, vous ne pouvez pas le rejoindre."


EVENT_SUFFIX = "-event"
ORGANIZER_PREFIX = "Organisateur-"
PARTICIPANT_PREFIX = "Event-"


SETUP_MSG = """**Pour finaliser la création de l'event, faite l'une des commandes si dessous:**

Ouvrir l'event a tous le monde:
```!open [message]```
Faire un event privé et inviter les personnes individuellement:
```!private```
"""

STOP_MSG = """Pour confirmer la fermeture de l'event, cliquez sur ✅."""

SET_EVENT_MSG = """@User a changé la description de l'event pour "@Status"."""

NEW_EVENT = """@everyone Nouvel event (@id)"""
NEW_EVENT_KEY = """Nouvel event ("""


EVENT_JOIN = """@User vient de rejoindre l'event.
Vous pouvez le quitter en tappant !leave.
"""