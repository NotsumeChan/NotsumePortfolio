import flet as ft
# indivuals imports from flet
from flet import Text, ElevatedButton, Image

#imports widgets
from widgets.appbarWidget import appbar
from widgets.bgcolorWidget import BackgroundColor

def HomePage(page : ft.Page):
    page.title = "home"
    return [
        appbar(page, "home"),
        BackgroundColor("#f2f2f2",ft.Container(
            padding= 100,
            content=ft.ResponsiveRow(
                [   
                    ft.Column([ft.Image(src=f"NotsumeGitHub.jpg", width=200, height=200, border_radius=40)],col={"xl": 2},),  
                    ft.Column([
                        Text("hi, i'm Notsume, a python expert developer\nstudent in the university Tecnico Santa Maria in Chile\n", size = 20, color="black"),
                        ft.Row([
                            ElevatedButton(
                                bgcolor=ft.colors.with_opacity(0, color="#59585e"),
                                content= Image(src=f"icons/github.png", width=50, height=50),
                                on_click=lambda a: page.launch_url("https://github.com/NotsumeChan?tab=repositories"),
                                elevation=0,
                            ),
                            ElevatedButton(
                                bgcolor=ft.colors.with_opacity(0, color="#59585e"),
                                content= Image(src=f"icons/linkedin.png", width=50, height=50),
                                on_click=lambda a: page.launch_url("https://www.linkedin.com/in/lucas-d%C3%ADaz-5771482b1/"),
                                elevation=0,
                            ),
                            ])]
                            ,col={"xl": 4},)
  
                    
                    
                ],

                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ),
        )
        ]