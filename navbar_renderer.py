from flask_nav.renderers import Renderer
from flask import render_template


class NavbarRenderer(Renderer):
    def visit_Navbar(self, node):
        views = []
        for item in node.items:
            views.append(self.visit(item))
        return render_template("components/navbar.html", views=views)

    def visit_View(self, node):
        print(dir(node))
        return {
            "url": node.get_url(),
            "title": node.text
        }

    def visit_Subgroup(self, node):
        pass
