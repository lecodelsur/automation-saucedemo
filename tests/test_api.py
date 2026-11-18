# mi propio "x-api-key": "reqres_2dbd7eae6cda425eb2aefbda8c8a5a50"

import requests
import pytest_check as check



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
    check.is_in("email",data) #assert "email" in data
    check.is_in("first_name",data) #assert "first_name" in data
    check.is_in("last_name",data) #assert "last_name" in data
    check.is_in("id",data) #assert "id" in dat

    # NIVEL 4
    check.equal(data["email"],usuario["email"]) # assert data["email"] == usuario["email"]
    check.equal(data["first_name"],usuario["first_name"]) # assert data["first_name"] == usuario["first_name"]

    # NIVEL 5: TIEMPO DE RESPUESTA
    assert response.elapsed.total_seconds() < 2
    
def test_eliminar_usuario(base_url,headers):
    url = f"{base_url}/users/2"
    
    response = requests.delete(url,headers=headers)
    
    # NIVEL 1: STATUS CODE
    assert response.status_code == 204
    
    # NIVEL 2: HEADERS
    assert "Content-Type" not in response.headers
    
    # NIVEL 3 Y 4: ESTRUCTURA Y CONTENIDO
    assert len(response.content) == 0
    
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