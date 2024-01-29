import flet as ft
from flet import View
from pages.homePage import HomePage
from pages.projectsPage import ProyectsPage

def main(page:ft.Page):
    page.scroll = True
    def routeChange(view):
        page.views.clear()
        if page.route == "/" or page.route == "/home":
            page.views.append(
                View(
                    "/home",
                    HomePage(page)
                )
            )
        if page.route == "/proyects":
            page.views.append(
                View(
                    "/proyects",
                    ProyectsPage(page)
                )
            )
        page.update()

    page.on_route_change = routeChange
    page.go(page.route)



if __name__ == "__main__":
    app = ft.app(
        target=main,
        assets_dir="assets",
        view=ft.WEB_BROWSER,)

    