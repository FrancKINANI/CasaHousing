# 📊 Prédiction de Prix de Logements à Casablanca  
**Un projet de Machine Learning simple utilisant Python, Pandas et la Régression Linéaire**  

## 🎯 Objectif  
Prédire le prix des logements à Casablanca en fonction de critères simples (surface, quartier, etc.) à l'aide d'un modèle de **régression linéaire**.  

---

## 📦 Structure du Projet  
```
housing-price-prediction/  
├── data/  
│   └── casablanca_housing.csv  # Dataset d'exemple  
├── housing_prediction.ipynb    # Notebook Jupyter (analyse + modèle)  
├── model.py                    # Script Python autonome  
├── requirements.txt            # Librairies nécessaires  
└── README.md                   # Ce fichier  
```

---

## 🔧 Installation  
1. **Clone le repo** :  
   ```bash  
   git clone https://github.com/ton-username/housing-price-prediction.git  
   ```  

2. **Installe les dépendances** :  
   ```bash  
   pip install -r requirements.txt  
   ```  
   *(Contenu de `requirements.txt` : pandas scikit-learn matplotlib)*  

---

## 🚀 Utilisation  
### Option 1 : Via Jupyter Notebook  
Ouvre `housing_prediction.ipynb` pour :  
- Explorer le dataset avec Pandas  
- Visualiser les données (graphiques)  
- Entraîner et évaluer le modèle  

### Option 2 : Via le script Python  
```bash  
python model.py  
```  
*Le script va :*  
1. Charger les données  
2. Entraîner le modèle  
3. Afficher la précision (score R²)  
4. Sauvegarder le modèle dans `model.pkl`  

---

## 📊 Exemple de Données  
Le fichier `casablanca_housing.csv` doit contenir :  
| surface (m²) | quartier     | prix (DH) |  
|--------------|--------------|-----------|  
| 120          | Maarif       | 2 500 000 |  
| 80           | Ain Diab     | 1 800 000 |  
| ...          | ...          | ...       |  

*(Remplace par tes propres données ou utilise**  

---

## 📈 Résultats Attendus  
- **Précision du modèle** : Score R² entre 0.7 et 0.9 (selon les données).  
- **Visualisation** : Graphique des prix réels vs prédits 

---

## 📝 Comment Contribuer ?  
1. Améliore le modèle avec :  
   - Plus de données réelles  
   - D'autres algorithmes (Random Forest, SVM)  
2. Crée une interface web avec Flask/Streamlit  

---

## 📌 Pourquoi ce Projet ?  
- Idéal pour **débuter en Machine Learning**  
- Montre ta maîtrise de :  
  - **Pandas** (nettoyage/analyse)  
  - **Scikit-learn** (modèles)  
  - **Visualisation** (Matplotlib)  

---
