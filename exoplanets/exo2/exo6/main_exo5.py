import flet
from flet import Page, Text, colors
import flet as ft
from urllib.request import urlopen
import json

#flet build apk --include-packages flet_webview

def main(page: Page):
    page.title = "EXOPLANETES"
    page.scroll = "adaptive"
    #page.bgcolor = 'black'
    nbexo = 100

    urlexo1 = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+count(pl_name)+as+nbe+from+ps+where+default_flag=1&format=json"
    print(urlexo1)
    data = json.loads(urlopen(urlexo1).read().decode("utf-8"))
    print(data)
    data0=data[0]
    print(data0)
    data0_1= data0['nbe']
    print(data0_1)

    page.add(
        
        Text(
            f"Nombre d'exoplanètes trouvées à ce jour : {data0_1} .",
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