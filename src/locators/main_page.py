from .common_selectors import css, el_id, link_text


class MainPage:
    class TopNav:
        nav_float_start = (css, "div.nav.float-start")
        admin_links = (css, "#top .float-end ul > li")
        register_btn = (link_text, "Register")

    class Header:
        logo = (el_id, "logo")
        search = (el_id, "search")
        cart = (el_id, "header-cart")

    class NavBar:
        nav_links = (css, "ul.nav > li")

    class Content:
        slider = (css, "#carousel-banner-0")
        promo = (css, "div#content.col > div.row")
        featured = (css, "h3+div.row div.col")

    class Footer:
        footer_blocks = (css, "footer > div > div")
        footer_bottom = (css, "footer > div > p")