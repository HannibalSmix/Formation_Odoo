# Python – Environnements virtuels (venv)

## Objectif
Comprendre et utiliser les environnements virtuels pour isoler les dépendances d’un projet Python.

## Pourquoi utiliser un venv ?

**Sans environnement virtuel :**
* Dépendances installées globalement.
* Conflits entre projets possibles.

**Avec environnement virtuel :**
* Dépendances isolées par projet.
* Versions contrôlées.
* Projet reproductible.

## Structure d’un projet
```text
mon_projet/
│
├── venv/                # L'environnement (isolé)
├── main.py              # Votre code
└── requirements.txt     # Liste des dépendances
```
*Le dossier `venv/` contient l’environnement Python. Les fichiers du projet restent en dehors.*

## Étapes d’utilisation

### 1. Créer le projet
```bash
mkdir mon_projet
cd mon_projet
```

### 2. Créer l’environnement virtuel
```bash
python -m venv venv
```

### 3. Activer l’environnement
*   **Windows :** `venv\Scripts\activate`
*   **Mac / Linux :** `source venv/bin/activate`

> Le terminal affiche `(venv)` en début de ligne lorsque l’environnement est actif.

### 4. Installer une dépendance
```bash
pip install rich
```

### 5. Tester
Lancez `python`, puis dans l’interpréteur :
```python
import rich
print("OK")
```

### 6. Sauvegarder les dépendances
```bash
pip freeze > requirements.txt
```
*Exemple de contenu : `rich==13.x.x`*

### 7. Désactiver l’environnement
```bash
deactivate
```

---

## Réinstaller un projet

1. **Supprimer l’environnement existant (si besoin)**
   * Windows : `rmdir /s /q venv`
   * Mac / Linux : `rm -rf venv`

2. **Recréer et activer**
   * `python -m venv venv`
   * Activation (selon OS voir étape 3)

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

---

## Points importants
* **Un projet = un environnement virtuel.**
* **Activer** toujours l'environnement avant un `pip install`.
* Utiliser systématiquement un fichier **requirements.txt**.
* **Ne pas versionner** le dossier `venv/` (l'ajouter au `.gitignore`).

## Vérifier l’environnement utilisé
Pour savoir quel interpréteur Python est actuellement sollicité :
```python
import sys
print(sys.executable)
```
