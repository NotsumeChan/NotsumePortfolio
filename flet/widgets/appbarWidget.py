import flet as ft
from flet import AppBar, Text, TextButton


def appbar(p, title:str):
    page = AppBar(
        title=Text("Notsume Portfolio"),
        bgcolor="#7e34cb",
        actions=[
            TextButton("home",disabled= True if  title == "home" else False, on_click=lambda a: p.go("/home")),
            TextButton("Proyects", disabled= True if  title == "Proyects" else False, on_click=lambda a: p.go("/proyects")),
        ]
    )
    return page