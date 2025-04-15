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
    response = requests.delete("http://127.0.0.1:5000/"+endpoint, json={"id": id })

    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Error: {response.status_code}")
        print(response.json())

def edit(page, id, endpoint):
    page.go(endpoint)

def get_admin(page: ft.Page):

    go_back_button = ft.Button(text=" ", icon=ft.Icons.CHEVRON_LEFT, on_click=lambda _: page.go("/"))

    def refresh_tables():
        clientes = get_data("obtener_clientes")
        entradas = get_data("obtener_datos_parking")

        #clientes_table.controls[2] = build_clientes_table(clientes)
        #entradas_table.controls[1].controls[0] = build_entradas_table(entradas)
        page.update()

    def delete_and_refresh(id, endpoint):
        delete_register(id, endpoint)
        refresh_tables()

    def build_clientes_table(clientes):
        return ft.DataTable(
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
                        ft.DataCell(ft.Row([ft.IconButton(
                                icon=ft.Icons.RESTORE_FROM_TRASH,
                                bgcolor=ft.Colors.RED_900,
                                icon_color=ft.colors.WHITE,
                                on_click=lambda _, id=cliente["id"]: delete_and_refresh(id, "borrarCliente"),
                            ),
                            #ft.IconButton(
                            #    icon=ft.CupertinoIcons.PENCIL,
                            #    bgcolor=ft.Colors.YELLOW_900,
                            #    icon_color=ft.colors.WHITE,
                            #    on_click=lambda _, id=cliente["id"]: page.go(f"/actualizar_cliente?id={id}"))
                            ])),
                    ]
                ) for cliente in clientes
            ]
        )
    
    

    def build_entradas_table(entradas):
        return ft.DataTable(
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
                        ft.DataCell(ft.Text(str(entrada["precio"]))),
                        ft.DataCell(ft.Text(str(entrada["usuario"]))),
                        ft.DataCell(ft.Row([ft.IconButton(
                                icon=ft.Icons.RESTORE_FROM_TRASH,
                                bgcolor=ft.Colors.RED_900,
                                icon_color=ft.colors.WHITE,
                                on_click=lambda _, id=entrada["id"]: delete_and_refresh(id, "borrarClienteParking"),
                            ),
                            #ft.IconButton(
                            #    icon=ft.CupertinoIcons.PENCIL,
                            #    bgcolor=ft.Colors.YELLOW_900,
                            #    icon_color=ft.colors.WHITE,
                            #    on_click=lambda _, id=entrada["id"]: page.go(f"/actualizar_cliente?id={id}"))
                            ])),
                    ]
                ) for entrada in entradas
            ]
        )

    clientes_table = ft.Column([
        ft.Text("Tabla de clientes:", size=20),
        ft.IconButton(icon=ft.Icons.ADD, bgcolor=ft.Colors.GREEN_900, icon_color=ft.colors.WHITE, on_click=lambda _: page.go("/crear-cliente")),
        build_clientes_table(get_data("obtener_clientes")),
    ])

    entradas_table = ft.Column([
        ft.Text("Tabla de registros:", size=20),
        ft.ListView(
            controls=[build_entradas_table(get_data("obtener_datos_parking"))],
            expand=True,
        )
    ])

    return ft.Column([
        go_back_button,
        clientes_table,
        entradas_table,
    ])
