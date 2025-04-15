import flet as ft
import requests
import json
from urllib.parse import urlparse, parse_qs

def route_change(e):
    route = urlparse(e.route)
    path = route.path
    query = parse_qs(route.query)

    if path == "/actualizar_cliente":
        id = query.get("id", [None])[0]
        print(f"ID received: {id}")

    print(id)

    return id    

def create_client(page: ft.Page, id=None):
    go_back_button = ft.Button(text=" ", icon=ft.Icons.CHEVRON_LEFT, on_click=lambda _: page.go("/admin"))
    matriculas_field = ft.TextField(label="Matricula")
    usuario_field = ft.TextField(label="Usuario")

    # Submit button
    def submit_form(e):
        endpoint = 'agregar_usuario' if id == None else 'actualizar_cliente'

        data = {
            "usuario": usuario_field.value,
            "matricula": json.loads(matriculas_field.value),
        }

        print(endpoint)
        
        response = requests.post("http://127.0.0.1:5000/"+endpoint, json=data)

        if response.status_code == 200:
            data = response.json()
            return data['message']
        else:
            print(f"Error: {response.status_code}")
            print(response.json())


    submit_button = ft.ElevatedButton(text="Guardar", on_click=submit_form)

    page.update()

    # Add fields to the page
    return ft.Column([
            go_back_button,
            usuario_field,
            matriculas_field,
            submit_button
        ])