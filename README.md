* [Cours django](<https://openclassrooms.com/fr/courses/7172076-debutez-avec-le-framework-django/7514338-tirez-le-maximum-de-ce-cours>)

mkdir new_project

cd new_project

git init 

python -m venv env 3

source env/Scripts/activate 

pip install django 

pip freeze > requirements.txt

* django-web-app/ - le répertoire racine de notre repository

* .gitignore

* requirements.txt - une liste des packages requis

* merchex/ - le répertoire contenant notre projet Django, l'application, la base de données et l'utilitaire de ligne de commande

* manage.py - le script utilitaire de ligne de commande de Django

* db.sqlite3 - le fichier de la base de données de Django

* merchex/ - le répertoire du projet, généré par « django-admin startproject merchex » : la « tour de contrôle » de notre projet

* settings.py - la configuration de l'ensemble du projet

* ...et d'autres fichiers relatifs au projet. 

* listings/ - le répertoire de l’application généré par « python manage.py startapp listings »

* ...les fichiers spécifiques aux applications que nous explorerons tout au long du cours


Pour lancer le serveur : python manage.py runserver