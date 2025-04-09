import flet as ft

def get_client(page: ft.Page):

    selected_files = ft.Text()

    async def pick_files_result(e: ft.FilePickerResultEvent):
        print(e)
        selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
        )
        selected_files.update()


    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    if pick_files_dialog not in page.overlay:
        page.overlay.append(pick_files_dialog)

    return ft.Column(
        [
            ft.ElevatedButton(
                "Coche entra",
                icon=ft.Icons.ARROW_CIRCLE_UP,
                on_click=lambda _: pick_files_dialog.pick_files(),
            ),
            ft.ElevatedButton(
                "Coche sale",
                icon=ft.Icons.ARROW_CIRCLE_DOWN,
                on_click=lambda _: pick_files_dialog.pick_files(),
            ),
            selected_files,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )
