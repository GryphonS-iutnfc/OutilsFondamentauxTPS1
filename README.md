(Les notebooks pour les TPs sont dans la repertoire "notebooks", et le projet final est dans la repertoire "project")

<h1>Analyse de déchiffrement lettre par lettre</h1>

Mon projet est une programme qui décrypte un chaîne de caractères où chaque lettre est chiffrée individuellement (comme un One-Time Pad) mais on suppose qu'on sait quand on a trouvé la bonne lettre, et on utilise le texte originale pour vérifier chaque lettre (comme dans TP5). J'ai demandé à quelle point l'analyse par fréquence est utile contre un méthode de brute-force dans des contextes différents.
<br><br>
J'ai testé trois algorithmes de décodage, le brute force ainsi que deux formes d'analyse de fréquence, et crée une graphe avec matplotlib pour montrer le temps que chacun prend.<br>
Le premier suppose que la message chiffrée est dans une certain langue (pour ce projet j'ai utilisé le français, l'anglais et le slovaque pour essayer d'avoir une bonne varieté),
et le deuxième tester les lettres déjà rencontrées pour calculer la langue la plus probable est l'utiliser comme base pour l'analyse de fréquence. 
<br><br>
J'ai testé tout les algorithmes pour chaque langue avec les chaînes de texte pour chaque langue (qui utilise la page de Wikipedia d'agriculture comme source, pour eviter les mots empruntés et être plus neutre),
et utiliser un chaîne qui mélange les trois langues (changeant la langue chaque 100 mots) pour tester l'éfficacité du dernier algorithme. 
<br>
Les resultats étaient plutôt prévisibles, où chaque algorithme est plus efficaçe avec leur langue respectif, et avec une différence plus grande entre les textes non-slovaque et l'algorithme slovaque (et vice-versa), ce qui est probablement parce qu'il y a une difference plus notable entre les lettres les plus fréquents en slovaque et en français/anglais que entre les lettres les plus fréquents entre anglais et français eux-mêmes.
<br>
Malheureusement, même avec un texte avec les changements des langues fréquents (une situation idéel pour l'analyse dynamique), l'algorithme pour décideder la langue du texte était si lent que même la brute force était beaucoup plus rapide. Peut-être si j'ai utilisé un texte assez large l'analyse dynamique aurait été plus efficaçe, mais en pratique je crois que vérifier la langue du texte simplement prend plus de temps qu'utiliser une mauvaise langue pour la décodage.
<br>
J'ai aussi rémarqué pas mal de variance chaque fois que j'ai démarré le code. Il est aussi consistente que je ne pense pas que ce soit une erreur dans le code lui-même, mais une réduction dans cetter variance serait un des problémes que j'essayerais de résoudre si j'ai refait le projet.

<br>
J'ai utilisé l'IA pour écrire le fonction analyse_dynamique, ce que j'ai verifié moi-même, et pour créer les graphes, que j'ai pu comprendre à un point mais pass assez pour tellement vérifier le code, seulement le resultat.


<img width="1600" height="1200" alt="image" src="https://github.com/user-attachments/assets/520e1235-1add-4faa-8702-5c534d1b23fd" />
