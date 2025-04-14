import flet as ft
import os
import requests

def get_data(endpoint):
    response = requests.get("http://127.0.0.1:5000/"+endpoint)

    if response.status_code == 200:
        data = response.json()
        return data['datos']
    else:
        print(f"Error: {response.status_code}")
        print(response.json())

def delete_register(id, endpoint):
    print(id)
    response = requests.delete("http://127.0.0.1:5000/"+endpoint, json={"id": id })

    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Error: {response.status_code}")
        print(response.json())


def get_admin(page: ft.Page):

    actual_path = os.path.abspath(os.getcwd())

    clientes = get_data("obtener_clientes")
    entradas = get_data("obtener_datos_parking")

    print(clientes)

    tabla_clientes = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Id")),
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Matriculas asociadas")),
            ft.DataColumn(ft.Text("Acciones")),
        ],
        rows=[
            ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(cliente["id"])),
                ft.DataCell(ft.Text(cliente["usuario"])),
                ft.DataCell(ft.Text(str(cliente["matriculas"]))),
                ft.DataCell(ft.Button(text=" ", icon=ft.Icons.RESTORE_FROM_TRASH, bgcolor=ft.Colors.RED_900, icon_color=ft.colors.WHITE, on_click=lambda _, id=cliente["id"]: delete_register(id, "borrarCliente"))),
            ]
            ) for cliente in clientes
        ]
    )

    tabla_entradas = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Id")),
            ft.DataColumn(ft.Text("Matricula")),
            ft.DataColumn(ft.Text("Hora de entrada")),
            ft.DataColumn(ft.Text("Fecha de entrada")),
            ft.DataColumn(ft.Text("Hora de salida")),
            ft.DataColumn(ft.Text("Usuario")),
            ft.DataColumn(ft.Text("Precio")),
            ft.DataColumn(ft.Text("Id Cliente")),
            ft.DataColumn(ft.Text("Acciones")),
        ],
        rows=[
            ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(entrada["id"])),
                ft.DataCell(ft.Text(str(entrada["matricula"]))),
                ft.DataCell(ft.Text(str(entrada["hora_entrada"]))),
                ft.DataCell(ft.Text(str(entrada["fecha_entrada"]))),
                ft.DataCell(ft.Text(str(entrada["hora_salida"]))),
                ft.DataCell(ft.Text(str(entrada["usuario"]))),
                ft.DataCell(ft.Text(str(entrada["hora_salida"]))),
                ft.DataCell(ft.Text(str(entrada["usuario"]))),
                ft.DataCell(ft.Button(text=" ", icon=ft.Icons.RESTORE_FROM_TRASH, bgcolor=ft.Colors.RED_900, icon_color=ft.colors.WHITE, on_click=lambda _, id=entrada["id"]: delete_register(id, "borrarClienteParking"))),
            ]
            ) for entrada in entradas
        ]
    )

    

    page.update()

    return ft.Row(
        [
            tabla_clientes,
            tabla_entradas
        ]
    )