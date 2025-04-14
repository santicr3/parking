import flet as ft
import client
import admin

def main(page: ft.Page):

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    root_page = ft.Container(
        content=ft.Column(
            [
                ft.ElevatedButton(
                    "Admin",
                    icon=ft.Icons.ADMIN_PANEL_SETTINGS_OUTLINED,
                    on_click=lambda _: page.go("/admin"),
                ),
                ft.ElevatedButton(
                    "Client",
                    icon=ft.Icons.PERSON_2_OUTLINED,
                    on_click=lambda _: page.go("/client"),
                ),
            ],
        ),
    )

    def change_route(e: ft.RouteChangeEvent):
        page.views.clear()

        route = e.route
        print("Ruta actual:", route)


        if route == "/":
            page.views.append(
                ft.View(
                    "/",
                    [root_page],
                )
            )
        elif route == "/client":
            page.views.append(
                ft.View(
                    "/client",
                    [client.get_client(page)],
                )
            )
        elif route == "/admin":
            print("Route: Admin")
            page.views.append(
                ft.View(
                    "/admin",
                    [admin.get_admin(page)],
                )
            )

        page.update()

    page.on_route_change = change_route

    page.go(page.route)


ft.app(main)
