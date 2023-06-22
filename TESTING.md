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

</details>

[Back To Top](#table-of-contents)

_____

## CSS

CSS code was tested using the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) via text input. 

<details>
<summary>Screenshot with results for the styles.css file</summary>
<br>

</details>

[Back To Top](#table-of-contents)
_____

## Python

Python code was tested using [Code Institute's Python Linter](https://pep8ci.herokuapp.com/).

Long lines in `settings.py` and `env.py` were cleared using `# noqa`. These were values by the Django generated AUTH_PASSWORD_VALIDATORS and the long password values.

[Back To Top](#table-of-contents)
_____

## JavaScript

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
