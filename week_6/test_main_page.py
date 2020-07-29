from os import getenv

BASE_URL = getenv('BASE_URL', "http://selenium1py.pythonanywhere.com/{language}/")
IMPLICIT_WAIT = 2
EXPLICIT_WAIT = 4
WINDOW_SIZE = ("1280", '1024')