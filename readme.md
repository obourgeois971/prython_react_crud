https://github.com/navinreddy20/fastapi-demo
https://www.youtube.com/watch?v=IR_EqMAlJZE&list=PLsyeobzWxl7qF4ASwCZZDXor_Y0YJ3Qfc&index=13

install de python
$ python --version

pour une install globale
$ pip install fastapi

pour une install spécifique
$ python -m venv myenv

activation de l'environnement
Activer: D:\workspace\workspace-python\workspace-python-01\src\myenv\Scripts\Activate.ps1
desactiver: desactivate

liste des packet installer
$ pip list

install fastapi et uvicorn (server web)
pip install fastapi uvicorn
pip install uvicorn
python -m pip install uvicorn fastapi (verif: python -m uvicorn --version)
python -m pip install fastapi uvicorn

pour executer un programme python
$ python main.py

lancer les server uvicorn
$ uvicorn main --reload
$ python -m uvicorn main:app --reload

url du swagger: http://localhost:8000/docs/

instal SQLAlchemy
pip install sqlalchemy psycopg2
pip install pymysql
