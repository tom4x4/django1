Django     2.2.5
Pillow     6.1.0
pip        19.2.3
pytz       2019.2
setuptools 41.2.0
sqlparse   0.3.0

python3 -m pip install --upgrade pip
pip install -r requirements.txt

----------https://tutorial.djangogirls.org/pl/django_start_project/
https://docs.djangoproject.com/en/2.0/ref/models/fields/#field-types

1---
django-admin startproject mysite .

Kropka . ma kluczowe znaczenie, ponieważ dzięki niej skrypt wie, że ma zainstalować
Django w bieżącym katalogu (kropka . to taka skrócona nazwa bieżącego katalogu)

#
#Aby utworzyć bazę danych dla naszego bloga, wykonajmy następujące polecenie w konsoli:
#(musimy być w katalogu djangogirls, tam gdzie znajduje się plik manage.py).
python manage.py migrate

#

python manage.py runserver 127.0.0.1:8080

#start aplikacji
python manage.py startapp blog

#Tworzymy tabele dla modeli w bazie danych
python manage.py makemigrations blog
python manage.py migrate blog

#admini konto
python manage.py createsuperuser
#panel -- https://docs.djangoproject.com/en/2.0/ref/contrib/admin/

