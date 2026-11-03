<h1>Analyse de déchiffrement lettre par lettre</h1>

Mon projet est une programme qui décrypte un chaîne de caractères où chaque lettre est chiffrée individuellement (comme un One-Time Pad) mais on suppose qu'on sait quand on a trouvé la bonne lettre, et on utilise le texte originale pour vérifier chaque lettre (comme dans TP5)
<br><br>
J'ai testé trois algorithmes de décodage, le brute force ainsi que deux formes d'analyse de fréquence, et crée une graphe avec matplotlib pour montrer le temps que chacun prend.<br>
Le premier suppose que la message chiffrée est dans une certain langue (pour ce projet j'ai utilisé le français, l'anglais et le slovaque pour essayer d'avoir une bonne varieté),
et le deuxième tester les lettres déjà rencontrées pour calculer la langue la plus probable est l'utiliser comme base pour l'analyse de fréquence. 
<br><br>
J'ai testé tout les algorithmes pour chaque langue avec les chaînes de texte pour chaque langue (qui utilise la page de Wikipedia d'agriculture comme source, pour eviter les mots empruntés et être plus neutre),
et utiliser un chaîne qui mélange les trois langues pour tester l'éfficacité du dernier algorithme. 


<img width="1600" height="1200" alt="image" src="https://github.com/user-attachments/assets/520e1235-1add-4faa-8702-5c534d1b23fd" />
