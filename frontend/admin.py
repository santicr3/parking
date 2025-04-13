import flet as ft
import os
import base64


def get_admin(page: ft.Page):

    actual_path = os.path.abspath(os.getcwd())

    return ft.Column(
        [
            ft.ElevatedButton(
                "Coche entra",
                icon=ft.Icons.ARROW_CIRCLE_UP,
                on_click=lambda _: pick_files_dialog.pick_files(
                    allow_multiple=False,
                    file_type=ft.FilePickerFileType.IMAGE,
                ),
            ),
            ft.ElevatedButton(
                "Coche sale",
                icon=ft.Icons.ARROW_CIRCLE_DOWN,
                on_click=lambda _: pick_files_dialog.pick_files(
                    allow_multiple=False,
                    file_type=ft.FilePickerFileType.IMAGE,
                ),
            ),
            selected_file,
            selected_image,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

def get_cars():
    print("Getting cars...")

def get_clients():
    print("Getting cars")