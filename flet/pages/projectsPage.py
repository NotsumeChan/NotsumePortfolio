import flet as ft
# indivuals imports from flet
from flet import Text

#imports widgets
from widgets.appbarWidget import appbar
from widgets.bgcolorWidget import BackgroundColor

def ProyectsPage(page):
    page.title = "proyects"
    return [
        appbar(page,"Proyects"),
        BackgroundColor("#59585e",ft.Container())
    ]