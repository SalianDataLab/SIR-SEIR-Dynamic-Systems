# Projet Mathématiques pour l'IA : Étape 1 --- Analyse des Systèmes Dynamiques

Ce dépôt contient les travaux de l' **Étape 1** du projet, consacrée à la modélisation et à la simulation des épidémies via les modèles compartimentaux **SIR** et **SEIR**.

## Contexte Scientifique

L'objectif est d'étudier comment une population évolue au cours d'une épidémie en utilisant le formalisme des **systèmes dynamiques** (systèmes d'équations différentielles ordinaires).

### Modèles implémentés :

- **SIR (Kermack & McKendrick, 1927)** : Modèle de référence répartissant la population en Sains (S), Infectés (I) et Rétablis (R).
- **SEIR** : Extension incluant une phase de latence (Exposés - E) pour représenter l'incubation des maladies modernes.

## Structure du Projet

- `app.py` : Simulateur interactif **Epidemix PRO** (Streamlit) avec design Ultra-Premium.
- `notebook_etape_1_sir_seir.md` : Rapport complet et rigoureux des fondations mathématiques.
- `etape_1_sir_seir.ipynb` : Version Jupyter Notebook pour l'exécution directe des démonstrations.
- `assets/` : Ressources graphiques et images de référence du dashboard.

## Installation et Utilisation

### Prérequis

- Environnement Conda
- Python 3.8+

### Installation des dépendances

```bash
pip install streamlit numpy scipy plotly
```

### Lancer le simulateur interactif

```bash
streamlit run app.py
```

### Consulter le Notebook

Le notebook peut être ouvert avec Jupyter Lab ou VS Code pour explorer les équations et les simulations matplotlib.

## Caractéristiques de l'Application

- **Dashboard R0** : Visualisation en temps réel du nombre de reproduction de base.
- **Paramètres Dynamiques** : Ajustement de la transmission ($\beta$), de la guérison ($\gamma$) et de l'incubation ($\sigma$).
- **Interface Premium** : Design "Nanotechnique" haute-fidélité, sans emojis, pour un rendu professionnel et scientifique.

## Références

- Kermack, W. O., & McKendrick, A. G. (1927). *A Contribution to the Mathematical Theory of Epidemics*.
- Hethcote, H. W. (2000). *The Mathematics of Infectious Diseases*.
