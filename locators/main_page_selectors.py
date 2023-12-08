from .common_selectors import css, link_text, el_id, xpath


class MainPageSelectors:
    alert = (xpath, '//*[@id="alert"]/dirv')

    class TopNav:
        nav_float_start = (css, "div.nav.float-start")
        admin_links = (css, "#top .float-end ul > li")
        login_btn = (link_text, "Login")
        register_btn = (link_text, "Register")
        logout_btn = (link_text, "Logout")

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
