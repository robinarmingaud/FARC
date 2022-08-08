# FARC - Flow-R Airborn Risk Calculator

Le FARC est un projet combinant 2 outils : tout d'abord un calculateur d'évaluation des risques développé pour modéliser la concentration des virus dans les espaces fermés, afin d'éclairer les décisions de gestion de l'espace. Il est basé sur le modèle CARA du CERN. Le second outil est une version étendue du premier calculateur permettant de réaliser des simulations sur tout un bâtiment à partir des informations concernant les pièces, les personnes et leur emploi du temps.

## Modifications du FARC par rapport au projet d'origine CARA
### Changements principaux
- Ajout d'un ratio de port du masque
- Ajout de nouvelles activités
- Séparation des activités des personnes infectées et des personnes saines
- Rapport plus détaillé avec des graphiques en plus : comparaison de l'évolution de la probabilité d'infection et de la dose cumulée absorbée
- Fenêtres maintenant ouvertes pendant les pauses quand l'option est sélectionnée
- Gestion d'accès des pages via une base de données et des cookies
- FARC Expert : Outil de simulation multi-évènementiel créé de 0

### Internationalisation
- Toute l'application est maintenant traduisible grâce à un balisage des chaînes de caractères via Babel
- Choix du langage basé sur les préférences du navigateur de l'utilisateur ou via un cookie 

### Code
- Séparation plus claire entre HTML/CSS/JS
- Factorisation de tous les paramètres par défaut dans un seul fichier
- Suppression des templates inutilisés et rassemblement des fichiers semblables dans les mêmes dossiers au maximum
- Réduction des tirages de Monte-Carlo de 250 000 à 60 000 
- Correction de bugs

### Interface
- Correction de bugs
- Changements dans le style

### CI
- Upload automatique vers le registre Flow-R d'une nouvelle image Docker à chaque push

## Auteurs
Le FARC a été developpé à partir du modèle du CERN CARA développé par les membres suivants :

Andre Henriques<sup>1</sup>, Luis Aleixo<sup>1</sup>, Marco Andreini<sup>1</sup>, Gabriella Azzopardi<sup>2</sup>, James Devine<sup>3</sup>, Philip Elson<sup>4</sup>, Nicolas Mounet<sup>2</sup>, Markus Kongstein Rognlien<sup>2,6</sup>, Nicola Tarocco<sup>5</sup>

<sup>1</sup>HSE Unit, Occupational Health & Safety Group, CERN<br>
<sup>2</sup>Beams Department, Accelerators and Beam Physics Group, CERN<br>
<sup>3</sup>Experimental Physics Department, Safety Office, CERN<br>
<sup>4</sup>Beams Department, Controls Group, CERN<br>
<sup>5</sup>Information Technology Department, Collaboration, Devices & Applications Group, CERN<br>
<sup>6</sup>Norwegian University of Science and Technology (NTNU)<br>

Au sein de Flow-R et Ingenica les personnes ayant contribué au projet sont : 

Olivier Perraud <sup>1</sup>, Serge Lebrun <sup>2</sup>, Vincent Kozlik <sup>3</sup>, Dr. Valérie Héquet <sup>4</sup>, Fatima Afilal <sup>5</sup>, Simon Moro <sup>6</sup>, Robin Armingaud <sup>7</sup>

<sup>1</sup>PDG d'Ingenica<br>
<sup>2</sup>Directeur de l'ingénierie, Ingenica-LLI<br>
<sup>3</sup>Flow-R Products manager, Ingenica<br>
<sup>4</sup>Enseignant et chercheur (HDR) IMT Atlantique<br>
<sup>5</sup>Étudiant IMT atlantique<br>
<sup>6</sup>Étudiant IMT atlantique<br>
<sup>7</sup>Étudiant IMT atlantique et stagiaire Flow-R <br>

### Reference and Citation

**For the use of the CARA web app**
CARA – COVID Airborne Risk Assessment tool
© Copyright 2020-2021 CERN. All rights not expressly granted are reserved.

**For use of the model**
Henriques A, Mounet N, Aleixo L, Elson P, Devine J, Azzopardi G, Andreini M, Rognlien M, Tarocco N, Tang J. (2022). Modelling airborne transmission of SARS-CoV-2 using CARA: risk assessment for enclosed spaces. _Interface Focus 20210076_. https://doi.org/10.1098/rsfs.2021.0076

## Applications

### Disclaimer


Cet outil est conçu pour être informatif, permettant à l'utilisateur d'adapter différents paramètres et de modéliser l'impact relatif sur les probabilités d'infection estimées.
L'objectif est de faciliter la prise de décision et l'investissement ciblé par des comparaisons, plutôt qu'une détermination singulière du risque absolu.
Bien que le virus SARS-CoV-2 soit en circulation parmi la population, la notion de «risque zéro» ou de «scénario complètement sûr» n'existe pas.
Chaque événement modélisé est unique, et les résultats qui y sont générés ne sont que justes qu'en fonction des données d'entrées et des hypothèses du modèle.
Le FARC n'a pas subi d'examen, d'approbation ou de certification par les autorités compétentes et, par conséquent, il ne peut pas être considéré en tant qu'outil entièrement approuvé et fiable.


### Lancer le FARC localement dans un Docker

La manière la plus rapide de déployer le FARC localement est d'utiliser Docker. Cloner le répertoire :

    $ git clone https://git.flow-r.fr/CI/FARC

Se rendre dans le répertoire principal

    $ cd FARC

Télécharger les fichiers lourds avec git-lfs :

    $ git lfs pull

Créer une image Docker en remplaçant 1.0.1 par la version actuelle : 

    $ docker build -t farc:latest -t farc:1.0.1 .

Enfin, lancer le conteneur Docker à l'adresse http://localhost:8080/ :
    
    $ docker run -d -p 8080:8080 farc:latest

Ou tout autre port en remplaçant 8080:8080 (par 9000:8080 par exemple pour le port 9000).

Cependant, il va falloir par la suite configurer les cookies manuellement pour autoriser l'accès aux applications. Pour contourner cette limitation, il est possible de lancer le FARC en mode développement en désactivant l'authentification.


### Lancer le FARC en mode de développement

Cloner le répertoire :

    $ git clone https://git.flow-r.fr/CI/FARC

Se rendre dans le répertoire principal

    $ cd FARC

Installer les librairies nécessaires :

    $ pip install -r farc/requirements.txt

Télécharger les fichiers lourds avec git-lfs :

    $ git lfs pull

Lancer le FARC en local en désactivant l'authentification : 

    $ python3 -m farc.apps.calculator --no-auth=True 


## Internationalisation

Pybabel est nécessaire pour extraire le texte du code. 

```console
$ pip install Babel
```

Ajouter "pybabel.py au PATH.
Si des champs de texte ont été modifiés dans le code, utiliser la fonction _ si on souhaite les traduire. 
Extraire le texte : 

```console
$ cd farc-master/farc/apps
```

```console
$ pybabel extract -F babel-mapping.ini -o locale/base.pot ./
```

- Cette commande crée un fichier de template de traduction dans le dossier locale
- Update les traductions dans les différentes langues :

```console
$ pybabel update -i locale/base.pot -d locale
```

- Les fichiers pot sont des dictionnaires comprenant les champs de textes venant du template de traduction et leur traduction. Un éditeur en ligne efficace pour renseigner ces traductions : https://pofile.net/
- Ensuite, compiler les fichiers pot en fichier mo :

```console
$ pybabel compile -d locale    
```
