# Projet_Python_data_analysis-public

Parenthèse : Le dataset choisit (Bar Crawl: Detecting Heavy Drinking https://archive.ics.uci.edu/ml/datasets/Bar+Crawl%3A+Detecting+Heavy+Drinking) ne correspond pas à celui attribué car le dataset attribué (Unmanned Aerial Vehicle (UAV) Intrusion Detection https://archive.ics.uci.edu/ml/datasets/Unmanned+Aerial+Vehicle+%28UAV%29+Intrusion+Detection) est vide/n'existe pas

1. Description de l'étude
	Dans cette étude, nous avons essayé de prévoir l'état débriété d'une personne à partir de données d'accéléromètre de son téléphone.

2. Fichiers et scripts
	- Un jupyter notebook "projet.ipynb" a été fait afin d'importer les données, de traiter ces données et contient 3 modèles prédictifs
	- Le meilleur modèle exporter en pickle "model.pickle"
	- Un script python déployant une API pour utiliser le modèle "API.py" a été réalisé avec Flask
	- Un script python donnant une éxecution de l'API "request.py" (faire tourner l'API avant)
	- Les données utilisées stockées dans le fichier data

3. Les résultats
	- Le modèle obtenu a un taux de réussite à 80% (non négligeable) mais la base de données n'est pas assez conséquente et les conditions de l'étude pas assez réglementées pour avoir un modèle fiable
	- Nous obtenons une mauvaise répartition entre les données d'état sobre contre l'état saoul.
	- Une seule donnée (accéléromètre) n'est pas suffisant pour un modèle de prédiction fiable.

4. Conclusion
	- Des résultats prometteurs, mais étude à refaire à plus grande échelle.
