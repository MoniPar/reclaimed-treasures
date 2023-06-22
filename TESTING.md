# Table of Contents

- [Table of Contents](#table-of-contents)
- [Code Validation](#code-validation)
  - [HTML](#html)
  - [CSS](#css)
  - [Python](#python)
  - [JavaScript](#javascript)
- [Lighthouse](#lighthouse)
- [Responsiveness](#responsiveness)
- [Browser Compatibility](#browser-compatibility)
- [User Stories](#user-stories)
- [Features](#features)

_____

# Code Validation

## HTML

HTML code was tested using the [W3C Validator](https://validator.w3.org/) via text input. Each page's source code was copied and pasted into the validator and checked for errors and warnings.

<details>
<summary>Home & About Pages</summary>
<br>

![HTML Validation for Home Page](docs/validation/html-val_home.png)

![HTML Validation for About Page](docs/validation/html-val_about.png)

</details>

<details>
<summary>Shop, Product Details & Review Pages</summary>
<br>

![HTML Validation for Shop Page](docs/validation/html-val_shop.png)

![HTML Validation for Product Detail Page](docs/validation/html-val_product-detail.png)

![HTML Validation for Add Review Page](docs/validation/html-val_add-review.png)

![HTML Validation for Edit Review Page](docs/validation/html-val_edit-review.png)

![HTML Validation for Delete Confirmation Review Page](docs/validation/html-val_delete-review.png)

</details>

<details>
<summary>Basket & Checkout Pages</summary>
<br>

![HTML Validation for Basket Page](docs/validation/html-val_basket.png)

![HTML Validation for Checkout Page](docs/validation/html-val_checkout.png)

![HTML Validation for Checkout Success Page](docs/validation/html-val_checkout-success.png)

</details>

<details>
<summary>Profile & Contact Pages</summary>
<br>

![HTML Validation for Profile Page](docs/validation/html-val_profile.png)

![HTML Validation for Contact Page](docs/validation/html-val_contact.png)

</details>

<details>
<summary>Signup, Login & Logout Pages</summary>
<br>

![HTML Validation for Signup Page](docs/validation/html-val_signup.png)

![HTML Validation for Login Page](docs/validation/html-val_login.png)

![HTML Validation for Logout Page](docs/validation/html-val_logout.png)

</details>

<details>
<summary>Error Pages</summary>
<br>

![HTML Validation for Error404 Page](docs/validation/html-val_error404.png)

![HTML Validation for Error403 Page](docs/validation/html-val_error403.png)

![HTML Validation for Error500 Page](docs/validation/html-val_error500.png)

</details>

[Back To Top](#table-of-contents)

_____

## CSS

CSS code was tested using the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) via file input.  No errors found, warnings due to vendor prefixes.

<details>
<summary>Screenshot with results for the styles.css file</summary>
<br>

BASE STYLESHEET

![CSS Validation for base.css file](docs/validation/base.png)

PRODUCTS STYLESHEET

![CSS Validation for products.css file](docs/validation/products.png)

CHECKOUT STYLESHEET

![CSS Validation for checkout.css file](docs/validation/checkout.png)

PROFILE STYLESHEET

![CSS Validation for profile.css file](docs/validation/profile.png)

CONTACT STYLESHEET

![CSS Validation for contact.css file](docs/validation/contact.png)

ABOUT STYLESHEET

![CSS Validation for about.css file](docs/validation/about.png)

</details>

[Back To Top](#table-of-contents)
_____

## Python

Python code was tested using [Code Institute's Python Linter](https://pep8ci.herokuapp.com/).

Long lines in 'settings.py' and 'env.py' were cleared using `# noqa`. These were values by the Django generated `AUTH_PASSWORD_VALIDATORS` and the long password values in 'env.py'.

<details>
<summary>Main App & custom_storages.py</summary>
<br>

![Python Validation for settings.py](docs/validation/settings.png)

![Python Validation for urls.py](docs/validation/urls.png)

![Python Validation for views.py](docs/validation/views.png)

![Python Validation for custom_storages.py](docs/validation/custom_storages.py.png)

</details>

<details>
<summary>Home App</summary>
<br>

![Python Validation for views.py](docs/validation/home-views.py.png)

![Python Validation for urls.py](docs/validation/home-urls.py.png)

</details>

<details>
<summary>Profiles App</summary>
<br>

![Python Validation for admin.py](docs/validation/profiles-admin.png)

![Python Validation for forms.py](docs/validation/profiles-forms.png)

![Python Validation for models.py](docs/validation/profiles-models.png)

![Python Validation for urls.py](docs/validation/profiles-urls.png)

![Python Validation for views.py](docs/validation/profiles-views.png)

</details>

<details>
<summary>Products App</summary>
<br>

![Python Validation for admin.py](docs/validation/products-admin.py.png)

![Python Validation for models.py](docs/validation/products-models.py.png)

![Python Validation for urls.py](docs/validation/products-urls.py.png)

![Python Validation for views.py](docs/validation/products-views.py.png)

</details>

<details>
<summary>Basket App</summary>
<br>

![Python Validation for basket_tools.py](docs/validation/basket-basket_tools.py.png)

![Python Validation for context.py](docs/validation/basket-context.py.png)

![Python Validation for urls.py](docs/validation/basket-urls.py.png)

![Python Validation for views.py](docs/validation/basket-views.py.png)

</details>

<details>
<summary>Checkout App</summary>
<br>

![Python Validation for admin.py](docs/validation/checkout-admin.py.png)

![Python Validation for apps.py](docs/validation/checkout-apps.py.png)

![Python Validation for forms.py](docs/validation/checkout-forms.py.png)

![Python Validation for models.py](docs/validation/checkout-models.py.png)

![Python Validation for signals.py](docs/validation/checkout-signals.py.png)

![Python Validation for urls.py](docs/validation/checkout-urls.py.png)

![Python Validation for views.py](docs/validation/checkout-views.py.png)

![Python Validation for webhook_handler.py](docs/validation/checkout-webhook_handler.py.png)

![Python Validation for webhooks.py](docs/validation/checkout-webhooks.py.png)

</details>

<details>
<summary>Reviews App</summary>
<br>

![Python Validation for admin.py](docs/validation/reviews-admin.py.png)

![Python Validation for forms.py](docs/validation/reviews-forms.py.png)

![Python Validation for models.py](docs/validation/reviews-models.py.png)

![Python Validation for urls.py](docs/validation/reviews-urls.py.png)

![Python Validation for views.py](docs/validation/reviews-views.py.png)

</details>

<details>
<summary>Contact App</summary>
<br>

![Python Validation for admin.py](docs/validation/contact-admin.py.png)

![Python Validation for forms.py](docs/validation/contact-forms.py.png)

![Python Validation for models.py](docs/validation/contact-models.py.png)

![Python Validation for urls.py](docs/validation/contact-urls.py.png)

![Python Validation for views.py](docs/validation/contact-views.py.png)

</details>

[Back To Top](#table-of-contents)
_____

## JavaScript

[JShint](https://jshint.com/) was used to validate customised scripts. No Errors or warnings were flagged.

<details>
<summary>Screenshots available here</summary>
<br>

**Script in basket.html**
![JavaScript Validation for script in basket.html](docs/validation/js_val-basket.html_script.png)

**Modified quantity_input_script.html**
![JavaScript Validation for script in quantity_input_script.html](docs/validation/js_val-quantity_input_script.png)

**Slightly modified countryfield.js file**
![JavaScript Validation for countryfield.js](docs/validation/js_val-countryfield_script.png)

**Slightly modified stripe_elements.js file**
![JavaScript Validation for stripe_elements.js](docs/validation/js_val-stripe_elements_script.png)

</details>

[Back To Top](#table-of-contents)

_____

# Lighthouse

[Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) was used to audit the website for performance, accessibility, best practice and SEO.  This was run in Chrome DevTools in incognito mode.

<details>
<summary>Home Page</summary>
<br>

MOBILE

![Lighthouse testing results for Home Page Mobile](docs/lighthouse/mobile-home.png)

Low performance score due to render blocking resources and unused javascript.
Render blocking resources included the Bootstrap suit with the highest transfer size.  Coverage was used to identify critical CSS and JS but due to time constraints, these could not be eliminated.
Stripe was flagged as unused JS, however it was decided to leave this in the base.html as recommended by Stripe documentation to manage fraudulent activity.

DESKTOP

![Lighthouse testing results for Home Page](docs/lighthouse/desktop-home.png)

</details>

<details>
<summary>Shop Page</summary>
<br>

MOBILE

![Lighthouse testing results for Shop Page](docs/lighthouse/mobile-shop.png)

Low performance score due to use of HTTP/1. Recommendation to use HTTP/2 with Amazon Web services. This is out of my control and could not switch at this stage.
Unused JavaScript - once again Stripe was flagged highest for this. Stripe recommends to place the JS link in the base.html to prevent fraudulent activity.

DESKTOP

![Lighthouse testing results for Shop Page](docs/lighthouse/desktop-shop.png)

</details>

<details>
<summary>Product Detail Page & Review Forms</summary>
<br>

PRODUCT DETAIL MOBILE

![Lighthouse testing results for Product Detail Page](docs/lighthouse/mobile-product_detail.png)

Low performance score due to render blocking resources and unused javascript.

PRODUCT DETAIL DESKTOP

![Lighthouse testing results for Product Detail Page](docs/lighthouse/desktop-product_detail.png)

ADD REVIEW MOBILE

![Lighthouse testing results for Add Review Page](docs/lighthouse/mobile-add_review.png)

Low performance score due to unused javascript and render blocking resources.

ADD REVIEW DESKTOP

![Lighthouse testing results for Add Review Page](docs/lighthouse/desktop-add_review.png)

EDIT REVIEW MOBILE

![Lighthouse testing results for Edit Review Page](docs/lighthouse/mobile-edit_review.png)

EDIT REVIEW DESKTOP

![Lighthouse testing results for Edit Review Page](docs/lighthouse/desktop-edit_review.png)

DELETE REVIEW CONFIRMATION MOBILE

![Lighthouse testing results for Delete Confirmation Review Page](docs/lighthouse/mobile_delete_review.png)

DELETE REVIEW CONFIRMATION DESKTOP

![Lighthouse testing results for Delete Confirmation Review Page](docs/lighthouse/desktop-delete_review.png)

</details>

<details>
<summary>Profile Page</summary>
<br>

MOBILE

![Lighthouse testing results for Profile Page](docs/lighthouse/mobile-profile.png)

DESKTOP

![Lighthouse testing results for Profile Page](docs/lighthouse/desktop-profile.png)

</details>

<details>
<summary>About Page</summary>
<br>

MOBILE

![Lighthouse testing results for About Page](docs/lighthouse/mobile-about.png)

Low performance score due to unused javascript, render blocking resources and use of HTTP1.

DESKTOP

![Lighthouse testing results for About Page](docs/lighthouse/desktop-about.png)

</details>

<details>
<summary>Basket Page</summary>
<br>

MOBILE

![Lighthouse testing results for Basket Page](docs/lighthouse/mobile-basket.png)

DESKTOP

![Lighthouse testing results for Basket Page](docs/lighthouse/desktop-basket.png)

</details>

<details>
<summary>Checkout & Checkout Success Pages</summary>
<br>

CHECKOUT PAGE MOBILE

![Lighthouse testing results for Checkout Page](docs/lighthouse/mobile-checkout.png)

CHECKOUT PAGE DESKTOP

![Lighthouse testing results for Checkout Page](docs/lighthouse/desktop-checkout.png)

CHECKOUT SUCCESS MOBILE

![Lighthouse testing results for Checkout Success Page](docs/lighthouse/mobile-checkout_success.png)

CHECKOUT SUCCESS DESKTOP

![Lighthouse testing results for Checkout Success Page](docs/lighthouse/desktop-checkout_success.png)

</details>

<details>
<summary>Contact & Contact Success Page</summary>

CONTACT MOBILE

![Lighthouse testing results for Contact Page](docs/lighthouse/mobile-contact.png)

CONTACT DESKTOP

![Lighthouse testing results for Contact Page](docs/lighthouse/desktop-contact.png)

CONTACT SUCCESS MOBILE

![Lighthouse testing results for Contact Success Page](docs/lighthouse/mobile-contact_success.png)

CONTACT SUCCESS DESKTOP

![Lighthouse testing results for Contact Success Page](docs/lighthouse/desktop-contact_success.png)

</details>

<details>
<summary>Signup, Login & Logout</summary>
<br>

SIGNUP MOBILE

![Lighthouse testing results for Signup Page](docs/lighthouse/mobile-register.png)

SIGNUP DESKTOP

![Lighthouse testing results for Signup Page](docs/lighthouse/desktop-register.png)

LOGIN MOBILE

![Lighthouse testing results for Login Page](docs/lighthouse/mobile-login.png)

LOGIN DESKTOP

![Lighthouse testing results for Login Page](docs/lighthouse/desktop-login.png)

LOGOUT MOBILE

![Lighthouse testing results for Logout Page](docs/lighthouse/mobile-logout.png)

LOGOUT DESKTOP

![Lighthouse testing results for Logout Page](docs/lighthouse/desktop-logout.png)

</details>

[Back To Top](#table-of-contents)

_____

# Responsiveness

[Back To Top](#table-of-contents)

_____

# Browser Compatibility

[Back To Top](#table-of-contents)

_____

# User Stories

[Back To Top](#table-of-contents)

_____

# Features

[Back To Top](#table-of-contents)

_____
