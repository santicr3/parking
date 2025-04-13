import flet as ft
import os
import base64


def get_client(page: ft.Page):

    actual_path = os.path.abspath(os.getcwd())

    selected_file = ft.Text()

    selected_image = ft.Image(src=actual_path+"frontend/media/default.jpg", width=300, height=300)

    async def pick_files_result(e: ft.FilePickerResultEvent):
        if e.files:
            file = e.files[0]
            print(file)
            
            selected_file.value = file.name
            selected_image.src = file.path

            file_bytes = await page.client_storage.read_bytes(file)

            base64_str = base64.b64encode(file_bytes).decode("utf-8")

            selected_image.src = f"data:image/jpeg;base64,{base64_str}"
            selected_file.value = base64_str
        else:
            selected_file.value = "Cancelled!"
            selected_image.src = "./media/default.jpg"

        selected_file.update()
        selected_image.update()

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result, allowed_extensions=["png", "jpg", "jpeg", "webp"])
    if pick_files_dialog not in page.overlay:
        page.overlay.append(pick_files_dialog)

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
