from .common_selectors import *


class RegPageSelectors:
    """Describing locators for Register Page"""

    class PersonalDetails:
        """fields using for registration"""
        first_name = (el_id, "input-firstname")
        last_name = (el_id, "input-lastname")
        email = (el_id, "input-email")
        password = (el_id, "input-password")

    input_newsletter = (el_id, "input-newsletter")
    agree = (css, "input[name=agree]")
    submit_btn = (css, "button[type=submit]")
    alert = (css, "#alert div")
    common_success = (el_id, "common-success")
