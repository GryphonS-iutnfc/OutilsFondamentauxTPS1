(Les notebooks pour les TPs sont dans la repertoire "notebooks", et le projet final est dans la repertoire "project")

<h1>Analyse de déchiffrement lettre par lettre</h1>

Mon projet est un programme qui décrypte une chaîne de caractères où chaque lettre est chiffrée individuellement (comme un One-Time Pad) mais on suppose qu'on sait quand on a trouvé la bonne lettre, et on utilise le texte original pour vérifier chaque lettre (comme dans TP5). J'ai demandé à quel point l'analyse par fréquence est utile contre une méthode de brute force dans des contextes différents.
<br>
J'ai testé trois algorithmes de décodage, le brute force ainsi que deux formes d'analyse de fréquence, et créé un graphique avec matplotlib pour montrer le temps que chacun prend.
Le premier suppose que le message chiffré est dans une certaine langue (pour ce projet j'ai utilisé le français, l'anglais et le slovaque pour essayer d'avoir une bonne variété), et le deuxième teste les lettres déjà rencontrées pour calculer la langue la plus probable et l'utiliser comme base pour l'analyse de fréquence.
<br>
J'ai testé tous les algorithmes pour chaque langue avec les chaînes de texte pour chaque langue (qui utilise la page de Wikipedia d'agriculture comme source, pour éviter les mots empruntés et être plus neutre), et utilisé une chaîne qui mélange les trois langues (changeant la langue tous les 100 mots) pour tester l'efficacité du dernier algorithme.
Les résultats étaient plutôt prévisibles, où chaque algorithme est plus efficace avec sa langue respective, et avec une différence plus grande entre les textes non slovaques et l'algorithme slovaque (et vice-versa), ce qui est probablement parce qu'il y a une différence plus notable entre les lettres les plus fréquentes en slovaque et en français/anglais qu'entre les lettres les plus fréquentes entre anglais et français eux-mêmes.
<br>
Malheureusement, même avec un texte avec les changements de langue fréquents (une situation idéale pour l'analyse dynamique), l'algorithme pour décider la langue du texte était si lent que même la brute force était quand même beaucoup plus rapide. Peut-être que si j'avais utilisé un texte assez large, l'analyse dynamique aurait été plus efficace, mais en pratique je crois que vérifier la langue du texte simplement prend plus de temps qu'utiliser une mauvaise langue pour le décodage.
J'ai aussi remarqué pas mal de variance chaque fois que j'ai exécuté le code. Il est aussi consistant que je ne pense pas que ce soit une erreur dans le code lui-même, mais une réduction de cette variance serait un des problèmes que j'essayerais de résoudre si je refais le projet.
<br>
J'ai utilisé l'IA pour écrire le fonction analyse_dynamique, ce que j'ai verifié moi-même, et pour créer les graphes, que j'ai pu comprendre à un point mais pass assez pour tellement vérifier le code, seulement le resultat.
<br>
J'ai utilisé l'IA pour écrire la fonction analyse_dynamique, ce que j'ai vérifié moi-même, et pour créer les graphiques, que j'ai pu comprendre dans une certaine mesure mais pas assez pour tellement vérifier le code, seulement le résultat. 


<img width="1600" height="1200" alt="image" src="https://github.com/user-attachments/assets/520e1235-1add-4faa-8702-5c534d1b23fd" />
