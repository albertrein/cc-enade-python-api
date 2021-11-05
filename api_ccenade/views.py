from django.http import JsonResponse
from django.db import connection

def usuarios(requests):
    if requests.method == "GET":
        cursor = connection.cursor()
        cursor.execute('''SELECT email FROM usuarios''')
        row = cursor.fetchone()
        usuarios = {"nome":row}
        return JsonResponse(usuarios)

