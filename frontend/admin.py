import flet as ft
import os
import base64
import requests

def get_data(endpoint):
    requests.get("https://api.example.com/data/"+endpoint)

    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error: {response.status_code}")



def get_admin(page: ft.Page):

    actual_path = os.path.abspath(os.getcwd())

    table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("First name")),
            ft.DataColumn(ft.Text("Last name")),
            ft.DataColumn(ft.Text("Age"), numeric=True),
        ],
        rows=[]
    )

    page.update()

    return table