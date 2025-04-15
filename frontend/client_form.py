import flet as ft
import requests

def create_client(page: ft.Page, id=0):
    id_field = ft.TextField(label="Id", disabled=True)
    matriculas_field = ft.TextField(label="Matricula")
    usuario_field = ft.TextField(label="Usuario")

    # Submit button
    def submit_form(e):
        global id

        endpoint = 'agregar_usuario' if id == None else 'actualizar_cliente'

        data = {
            "id": id_field.value,
            "usuario": usuario_field.value,
            "matricula": matriculas_field.value,
        }
        
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
            id_field,
            usuario_field,
            matriculas_field,
            submit_button
        ])