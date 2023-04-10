"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgpr1sgu9tun42u57k60-a.oregon-postgres.render.com",
        database="betsol",
        user="betsol_user",
        password="kVVfstlp98yKgWLLGt9qQGnuuM0kHVYz")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
