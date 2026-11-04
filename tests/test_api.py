# mi propio "x-api-key": "reqres_2dbd7eae6cda425eb2aefbda8c8a5a50"

import requests

def test_obtener_usuario():
    url = "https://reqres.in/api/users/2"

    header = { "x-api-key": "reqres_2dbd7eae6cda425eb2aefbda8c8a5a50" }

    response = requests.get(url,headers=header)

    # NIVEL 1: STATUS CODE
    codigo = response.status_code
    assert codigo == 200

    # NIVEL 2: HEADERS
    assert "application/json" in response.headers["Content-Type"]

    # NIVEL 3: ESTRUCTURA
    data = response.json()

    assert isinstance(data,dict) # Validar que el contenido sea un diccionario
    assert "data" in data
    assert isinstance(data["data"],dict)

    assert "id" in data["data"]
    assert "email" in data["data"]
    assert "first_name" in data["data"]
    assert "last_name" in data["data"]

    # NIVEL 4: CONTENIDO
    assert data["data"]["id"] == 2
    assert data["data"]["email"] == "janet.weaver@reqres.in"

    # NIVEL 5: TIEMPO DE RESPUESTA
    assert response.elapsed.total_seconds() < 2


def test_crear_usuario():
    url = "https://reqres.in/api/users/"
    
    header = { "x-api-key": "reqres_2dbd7eae6cda425eb2aefbda8c8a5a50" }

    usuario = {
        "email":"lecodelsur@gmail.com",
        "first_name":"Sergio",
        "last_name":"Sanchez",
        "job":"Alumno"
    }

    response = requests.post(url,headers=header,json=usuario)

    # NIVEL 1
    assert response.status_code == 201

    # NIVEL 2
    assert "application/json" in response.headers["Content-Type"]

    # NIVEL 3
    data = response.json()
    assert "email" in data
    assert "first_name" in data
    assert "last_name" in data
    assert "id" in data

    # NIVEL 4
    assert data["email"] == usuario["email"]
    assert data["first_name"] == usuario["first_name"]

    # NIVEL 5: TIEMPO DE RESPUESTA
    assert response.elapsed.total_seconds() < 2

"""
{
    "data":{
        "id":2,
        "email":"jose.montezuma@bue.edu.ar",
        "nombre":"Jose",
        "apellido":"Montezuma"
    },
    "support":{}
}
"""