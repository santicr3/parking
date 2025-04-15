import flet as ft
import requests

def create_car(page: ft.Page, id=0):
    id_field = ft.TextField(label="Id", disabled=True)
    matricula_field = ft.TextField(label="Matricula")
    hora_entrada_field = ft.TextField(label="Hora de entrada")
    fecha_entrada_field = ft.TextField(label="Fecha de entrada")
    hora_salida_field = ft.TextField(label="Hora de salida")
    usuario_field = ft.TextField(label="Usuario")
    precio_field = ft.TextField(label="Precio")
    id_cliente_field = ft.TextField(label="Id Cliente")

    # Submit button
    def submit_form(e):
        global id

        endpoint = 'parking_entrada' if id == None else 'actualizar_datos_parking_cliente'

        data = {
            "id": id_field.value,
            "matricula": matricula_field.value,
            "hora_entrada": hora_entrada_field.value,
            "fecha_entrada": fecha_entrada_field.value,
            "hora_salida": hora_salida_field.value,
            "usuario": usuario_field.value,
            "precio": precio_field.value,
            "cliente_id": id_cliente_field.value
        }
        
        response = requests.post("http://127.0.0.1:5000/"+endpoint, json=data)

        if response.status_code == 200:
            data = response.json()
            return data['datos']
        else:
            print(f"Error: {response.status_code}")
            print(response.json())


    submit_button = ft.ElevatedButton(text="Guardar", on_click=submit_form)

    page.update()

    # Add fields to the page
    return ft.Column([
            id_field,
            matricula_field,
            hora_entrada_field,
            fecha_entrada_field,
            hora_salida_field,
            usuario_field,
            precio_field,
            id_cliente_field,
            submit_button
        ])