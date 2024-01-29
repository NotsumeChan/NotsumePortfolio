import flet as ft

def BackgroundColor(color:str, content):
    return ft.Container(
        margin=-10,
        gradient= ft.LinearGradient(
            colors=["#7e34cb", color],
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            stops=[0.0, 1.4]
        ),
        expand=True,
        content = content
        )