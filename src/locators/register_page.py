from .common_selectors import el_id, css


class RegisterPage:
    """Describing locators for Register Page"""

    class PersonalDetails:
        """fields using for registration"""
        first_name = (el_id, "input-firstname")
        last_name = (el_id, "input-lastname")
        email = (el_id, "input-email")
        password = (el_id, "input-password")
    input_newsletter_yes = (el_id, "input-newsletter-yes")
    input_newsletter_no = (el_id, "input-newsletter-no")
    agree = (css, "input[name=agree]")
    submit_btn = (css, "button[type=submit]")
    alert = (css, "#alert div")
