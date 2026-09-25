# mini-broken-runtime-crash
Test angle mort : le BUILD réussit (image produite avec succès), mais le
CONTENEUR plante au démarrage (SyntaxError Python à l'import). À observer :
- Le déploiement passe-t-il bien en FAILED malgré un build "réussi" ?
- Les logs du conteneur (pas seulement du build) sont-ils capturés ?
- Le diagnostic IA a-t-il de quoi identifier la cause, ou seulement le
  message générique "Le build Docker n'a produit aucune image" (qui serait
  FAUX ici, puisque l'image existe bien) ?
