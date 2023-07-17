# Générateur De Mot De Passe

Ce programme est une fonction qui génère un mot de passe aléatoire.

Les paramètres de la fonction permettent de spécifier la longueur du mot de passe ainsi que si le mot de passe doit inclure des chiffres et/ou des lettres majuscules.

Le programme commence par importer les modules "random" et "string".

La fonction "pwgen" prend en entrée la longueur souhaitée pour le mot de passe ainsi que deux paramètres optionnels "with_digits" et "with_uppercase" qui permettent de spécifier si le mot de passe doit inclure des chiffres et/ou des lettres majuscules.

La variable "lowercase" contient toutes les lettres minuscules de l'alphabet. La variable "uppercase" contient toutes les lettres majuscules de l'alphabet. La variable "digits" contient toutes les chiffres de 0 à 9.

La variable "choices" est initialisée avec toutes les lettres minuscules de l'alphabet. Si le paramètre "with_digits" est True, la variable "choices" est mise à jour pour inclure également les chiffres. Si le paramètre "with_uppercase" est True, la variable "choices" est mise à jour pour inclure également les lettres majuscules.

La variable "password" est initialisée avec une liste de caractères aléatoires extraits de la variable "choices" avec une longueur égale à la longueur spécifiée en entrée.

Si les paramètres "with_digits" et "with_uppercase" sont tous les deux True, les trois premiers caractères de la variable "password" sont mis à jour pour inclure une lettre minuscule, un chiffre et une lettre majuscule. Si seulement "with_digits" est True, les deux premiers caractères de la variable "password" sont mis à jour pour inclure une lettre minuscule et un chiffre. Si seulement "with_uppercase" est True, les deux premiers caractères de la variable "password" sont mis à jour pour inclure une lettre minuscule et une lettre majuscule.

Finalement, la fonction renvoie le mot de passe généré sous forme de chaîne de caractères.
