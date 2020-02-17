django-tables2-2.2.1
https://django-tables2.readthedocs.io/en/latest/pages/tutorial.html




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

