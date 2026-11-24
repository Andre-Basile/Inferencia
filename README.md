# Inferencia

**Inferencia** est un petit moteur d'inférence en Python. Il charge des règles depuis un fichier JSON, vérifie si les conditions initiales sont satisfaites, puis ajoute les conclusions correspondantes à l'ensemble des faits.

Le projet illustre les bases d'un système expert simple : faits, règles et conclusions.

## Exemple

Avec les faits suivants :

```python
{
    "étudiant",
    "inscrit_L3",
    "carte_valide"
}
```

et les règles contenues dans `rules/rules.json`, le programme peut déduire :

- `niveau_L3`, lorsque le sujet est étudiant et inscrit en L3 ;
- `accès_bibliothèque`, lorsque le sujet est étudiant et possède une carte valide.

## Fonctionnement

Chaque règle possède une liste de conditions et une conclusion :

```json
{
  "conditions": ["étudiant", "inscrit_L3"],
  "conclusion": "niveau_L3"
}
```

Une règle est appliquée lorsque tous ses éléments figurent dans l'ensemble des faits initiaux. Les conclusions déduites sont ensuite affichées avec un résumé du raisonnement.

> **Important :** toutes les règles et tous les faits utilisés comme conditions doivent être chargés dans le fichier `rules/rules.json`. Si ce fichier est absent, incomplet ou mal formé, le programme ne pourra pas fonctionner correctement.

## Structure du projet

```text
Inference/
├── classes/
│   └── inferencia.py    # Moteur d'inférence
├── rules/
│   └── rules.json       # Règles du système
├── main.py              # Point d'entrée du programme
├── utils.py             # Chargement JSON et temporisation
└── requirements.txt     # Dépendances Python
```

## Installation

Python 3.14 est recommandé pour reproduire l'environnement actuel.

Depuis la racine du projet :

```powershell
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Utilisation

Lancez le programme avec :

```powershell
python main.py
```

Une sortie similaire à celle-ci est produite :

```text
Welcome to Inferencia, the inference system for every one.

(*_*):The subject has these facts : étudiant, inscrit_L3 and carte_valide
Reasoning : [étudiant,inscrit_L3,carte_valide] helps me to decide that the subject has attributes : "étudiant-inscrit_L3"
Reasoning : [étudiant,inscrit_L3,carte_valide] helps me to decide that the subject has attributes : "étudiant-carte_valide"
(*_*): All of these helps me to come to this conclusion : <<the subject has "étudiant,inscrit_L3,carte_valide,niveau_L3,accès_bibliothèque">>
```

## Ajouter des faits ou des règles

Modifiez la fonction `ask_facts()` dans `main.py` pour changer les faits initiaux :

```python
def ask_facts():
    return {
        "étudiant",
        "inscrit_L3",
        "carte_valide"
    }
```

Ajoutez ensuite une règle dans `rules/rules.json` :

```json
[
  {
    "conditions": ["étudiant", "inscrit_L3"],
    "conclusion": "niveau_L3"
  },
  {
    "conditions": ["étudiant", "carte_valide"],
    "conclusion": "accès_bibliothèque"
  }
]
```

## Informations éditoriales

**Auteur :** André B.S. KOVOHOUANDE  
**Publication :** novembre 2026