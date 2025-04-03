import flet as ft
import client
import admin
def main(page: ft.Page):

    def pick_files_result(e: ft.FilePickerResultEvent):
        selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
        )
        selected_files.update()

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text()

    page.overlay.append(pick_files_dialog)

    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER

    root_page = ft.Container(content=
        ft.Column(
            [
                ft.ElevatedButton(
                    "Admin",
                    icon=ft.Icons.ADMIN_PANEL_SETTINGS_OUTLINED,
                    on_click=lambda _: change_route(page, '/admin'),
                ),

                ft.ElevatedButton(
                    "Client",
                    icon=ft.Icons.PERSON_2_OUTLINED,
                    on_click=lambda _: change_route(page, '/client'),
                ),
            ],
        ),
        )

    def change_route(page: ft.Page, new_route):
        page.route = new_route
        print(page.route)
        page.views.clear()
        if page.route == "/":
            page.views.append(
                ft.View(
                    "/",
                    [
                        root_page
                    ],
                )
            )
        if page.route == "/client":
            page.views.append(
                ft.View(
                    "/client",
                    [
                        client.get_client(page)
                    ],
                )
            )
        if page.route == "/admin":
            page.views.append(
                ft.View(
                    "/admin",
                    [
                        client.get_admin(page)
                    ],
                )
            )
        page.update()

ft.app(main)