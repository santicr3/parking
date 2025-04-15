from datetime import datetime
from zoneinfo import ZoneInfo
import flet as ft
import os
import base64
import requests

def get_client(page: ft.Page):
    go_back_button = ft.Button(text=" ", icon=ft.Icons.CHEVRON_LEFT, on_click=lambda _: page.go("/"))
    actual_path = os.path.abspath(os.getcwd())

    exit_debt = ft.Text()
    selected_image = ft.Image(src=os.path.join(actual_path, "frontend/media/default.jpg"), width=300, height=300)

    type = None

    def plate_check(img):

        global type
        endpoint = "parking_entrada" if type == 'entrada' else "parking_salida"

        payload = {'imagen': img}

        response = requests.post(f"http://127.0.0.1:5000/{endpoint}", json=payload)
        
        if response.status_code == 200:
            response_json = response.json()
            print(response_json)
            if(endpoint == 'parking_salida'):
                print(response_json['cliente']['precio'])
                exit_debt.value = f"{response_json['cliente']['precio']}€ por su estancia"
                page.update()
        else:
            print(f"Error: {response.status_code}")
            print(response.json())

    async def pick_files_result(e: ft.FilePickerResultEvent):
        if e.files:
            file = e.files[0]
            print(f"Picked file: {file.name}, path: {file.path}")

            try:
                with open(file.path, "rb") as f:
                    file_bytes = f.read()
                base64_str = base64.b64encode(file_bytes).decode("utf-8")

                selected_image.src = file.path

                plate_check(base64_str)
            except Exception as err:
                selected_image.src = os.path.join(actual_path, "frontend/media/default.jpg")
        else:
            selected_image.src = os.path.join(actual_path, "frontend/media/default.jpg")

        selected_image.update()

    # File picker setup
    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    pick_files_dialog.allowed_extensions = ["png", "jpg", "jpeg", "webp"]

    if pick_files_dialog not in page.overlay:
        page.overlay.append(pick_files_dialog)

    def handle_entry_click(e):
        global type
        type = "entrada"
        pick_files_dialog.pick_files(
            allow_multiple=False,
            file_type=ft.FilePickerFileType.IMAGE,
        )

    def handle_exit_click(e):
        global type
        type = "salida"
        pick_files_dialog.pick_files(
            allow_multiple=False,
            file_type=ft.FilePickerFileType.IMAGE,
        )

    return ft.Column([
        go_back_button,
        ft.Row(
        [
            ft.ElevatedButton(
                "Coche entra",
                icon=ft.Icons.ARROW_CIRCLE_UP,
                on_click=handle_entry_click
            ),
            ft.ElevatedButton(
                "Coche sale",
                icon=ft.Icons.ARROW_CIRCLE_DOWN,
                on_click=handle_exit_click
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        ),
        selected_image,
        exit_debt
    ], alignment=ft.MainAxisAlignment.CENTER,
    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    ) 

