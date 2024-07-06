import flet
from flet import Page, Text, colors
import flet as ft

def main(page: Page):
    page.title = "Text custom styles"
    page.scroll = "adaptive"
    #page.bgcolor = 'black'

    page.add(
        
        Text(
            "Size 60, Bold, Italic",
            size=60,
            color=colors.WHITE,
            bgcolor=colors.BLUE_700,
            weight="bold",
            italic=True,
        ),     
    )


    def highlight_link(e):
        e.control.style.color = ft.colors.BLUE
        e.control.update()

    def unhighlight_link(e):
        e.control.style.color = None
        e.control.update()

    page.add(
        ft.Text(
            disabled=False,
            color=colors.BLACK,
            spans=[
                ft.TextSpan(
                    "Go to Google",
                    ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE),
                    url="https://google.com",
                    on_enter=highlight_link,
                    on_exit=unhighlight_link,
                )
            ],
        ),
    )


flet.app(target=main)