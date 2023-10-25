import flet as ft


class AuthView:
    def __init__(self):
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
