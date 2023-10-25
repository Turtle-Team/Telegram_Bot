import flet as ft
from views.auth.auth import AuthView


class AdminView:

    def __init__(self, page: ft.Page):
        self.page = page
        self.page.on_route_change = self.route_change
        self.page.on_view_pop = self.view_pop
        self.page.go(page.route)
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def route_change(self, route):
        self.page.views.clear()
        self.page.views.append(
            ft.View(
                "/",
                [
                    ft.Column([
                        ft.Text(
                            value="Авторизация",
                            color=ft.colors.BLACK,
                            size=24,
                            weight=ft.FontWeight.BOLD
                        ),

                        ft.Container(
                            content=ft.TextField(
                                label="Логин",
                                border_color=ft.colors.BLACK,
                                focused_border_color=ft.colors.BLACK,
                                focused_color=ft.colors.BLACK,
                                cursor_color=ft.colors.BLACK,
                                color=ft.colors.BLACK
                            ),
                            width=300,
                            padding=ft.padding.only(top=16)
                        ),

                        ft.Container(
                            content=ft.TextField(
                                label="Пароль",
                                password=True,
                                can_reveal_password=True,
                                border_color=ft.colors.BLACK,
                                focused_border_color=ft.colors.BLACK,
                                focused_color=ft.colors.BLACK,
                                cursor_color=ft.colors.BLACK,
                                color=ft.colors.BLACK
                            ),
                            width=300,
                            padding=ft.padding.symmetric(vertical=16)
                        ),
                        ft.Container(
                            content=ft.ElevatedButton("Войти", on_click=self.navigateToStore),
                            width=150,
                            height=40
                        )
                    ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    )
                ],
                bgcolor="#FFFFFF",
                vertical_alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
        troute = ft.TemplateRoute(self.page.route)
        if troute.match("/store/:id"):
            self.page.views.append(
                ft.View(
                    f"/store/{troute.id}",
                    [
                        ft.AppBar(title=ft.Text(troute.id), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Go Home", on_click=lambda _: self.page.go("/"))
                    ],
                )
            )
        self.page.update()

    def navigateToStore(self, id: int):
        self.page.go(f"/store/{id}")

    def view_pop(self, pop):
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)


ft.app(AdminView, view=ft.WEB_BROWSER)
