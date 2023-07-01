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

Website was tested extensively on Chrome devtools for responsiveness.  All pages are fully responsive on screens with width between 320px and 2560px. Friends and family tested the website on their devices and all reported no issues with responsiveness.

<details>
<summary>Navigation, Footer & Home Page</summary>
<br>

**NAVIGATION & HOME HERO**

    Mobile iPhone 5/SE Width 320px

![Mobile Navigation & Hero](docs/responsive/mobile-navhero-iphone5SE.png)

<br>

    Tablet iPad Width 768px

![Tablet Navigation & Hero](docs/responsive/tablet-navhero-ipad768.png)

<br>

    Desktop Width 1024px

![Desktop Navigation & Hero](docs/responsive/desktop-navhero-1024.png)

**FOOTER**

    Mobile Samsung Galaxy S8 Width 360px

![Mobile Footer](docs/responsive/mobile-footer-samsungs8360.png)

<br>

    Tablet Width 768px

![Tablet Footer](docs/responsive/tablet-footer-768.png)

<br>

    Desktop Nest Hub Max Width 1280px

![Desktop Footer](docs/responsive/desktop-footer-nesthubmax1280.png)
    
<br>

**HOME PAGE CONTENT**

    Mobile iPhone 12 Pro Width 390px

![Mobile Home Content](docs/responsive/mobile-home-iphone12pro390.png)

<br>

    Tablet Surface Pro Width 912px

![Tablet Home Content](docs/responsive/tablet-home-surfacepro912.png)

<br>

    Desktop Width 1440px 

![Desktop Home Content](docs/responsive/desktop-home-1440.png)

<br>
</details>

<details>
<summary>Shop Page & Product Detail</summary>
<br>

**SHOP**

    Mobile Samsung Galaxy S20 Width 420px

![Mobile Shop Page](docs/responsive/mobile-shop-samsunggalaxys20ultra412.png)

<br>

    Tablet iPad Width 768px

![Tablet Shop Page](docs/responsive/tablet-shop-ipad768.png)

<br>

    Desktop Nest Hub Width 1024px

![Desktop Shop Page](docs/responsive/desktop-shop-nesthub1024.png)

<br>

**PRODUCT DETAIL**

    Mobile Galaxy S5 Width 360px

![Mobile Product Detail Page](docs/responsive/mobile-productdetail-galaxys5360.png)

<br>

    Tablet Surface Pro 7 Width 912px

![Tablet Product Detail Page](docs/responsive/tablet-productdetail-surfacepro912.png)

<br>

    Desktop Width 1440px

![Desktop Product Detail Page](docs/responsive/desktop-productdetail-1440.png)

<br>

**REVIEWS SECTION**

    Mobile Width 375px

![Mobile Reviews Section](docs/responsive/mobile-reviews-375.png)

<br>

    Tablet Width 768px

![Tablet Reviews Section](docs/responsive/tablet-reviews-768.png)

<br>

    Desktop Nest Hub Max Width 1280px

![Desktop Reviews Section](docs/responsive/desktop-reviews-nesthubmax1280.png)

<br>

**ADD REVIEW**

    Mobile iPhone X Width 375px

![Add review form on mobile](docs/responsive/mobile-addreview-iphonex375.png)

<br>

    Desktop Width 1024px

![Add review form on desktop](docs/responsive/desktop-addreview-1024.png)

<br>

**EDIT REVIEW**

    Tablet Width 768px

![Edit review form on tablet](docs/responsive/tablet-editreview-768.png)

<br>

**DELETE REVIEW**

    Mobile Galaxy S9 Width 320px

![Delete review confimation on mobile](docs/responsive/mobile-deletereview-galaxys9320.png)

<br>

    Desktop Width 1024px

![Delete review confirmation on desktop](docs/responsive/desktop-deletereivew-1024.png)

<br>
</details>

<details>
<summary>Basket & Checkout</summary>
<br>

**BASKET PAGE**

    Mobile Width 320px

![Mobile Basket Page](docs/responsive/mobile-basket-320.png)

<br>

    Tablet Width 912px

![Tablet Basket Page](docs/responsive/tablet-basket-912.png)

<br>

    Desktop Width 1024px

![Desktop Basket Page](docs/responsive//desktop-basket-1024.png)

<br>

**CHECKOUT PAGE**

    Mobile Width 320px

![Mobile Checkout Page](docs/responsive/mobile-checkout-320.png)

<br>

    Tablet Width 768px

![Tablet Checkout Page](docs/responsive/tablet-checkout-768.png)

<br>

    Desktop Width 1024px

![Desktop Checkout Page](docs/responsive/desktop-checkout-1024.png)

<br>

**CHECKOUT SUCCESS PAGE**

    Mobile iPhone 14 Width 390px

![Mobile Checkout Success page](docs/responsive/mobile-orderconfirm-iphone14390.png)

<br>

    Tablet iPad Mini Width 768px

![Tablet Checkout Success Page](docs/responsive/tablet-orderconfirm-ipadmini768.png)

<br>

    Desktop Width 1024px

![Desktop Checkout Success Page](docs/responsive/desktop-orderconfirm-1024.png)

<br>
</details>

<details>
<summary>Profile</summary>
<br>

    Mobile Samsung S8 Width 360px

![Profile page on mobile](docs/responsive/mobile-profile-samsungs8360.png)

<br>

    Desktop Nest Hub Max Width 1280px

![Profile page on destkop](docs/responsive/desktop-profile-nesthubmax1280.png)

<br>
</details>

<details>
<summary>Registration & Authentication</summary>
<br>

**REGISTER PAGE**

    Mobile iPhone X Width 414

![Register page on mobile](docs/responsive/mobile-register-iphonxr414.png)

<br>

    Desktop Width 1024px

![Register page on desktop](docs/responsive/desktop-registration-1024.png)

<br>

**LOGIN PAGE**

    Tablet iPad Air Width 820px

![Login page on tablet](docs/responsive/tablet-login-ipadair820.png)

<br>

**LOGOUT PAGE**

    Mobile Samsung Galaxy A5 Width 412px

![Logout page on mobile ](docs/responsive/mobile-logout-samsunggalaxya51412.png)

<br>
</details>

<details>
<summary>About & Contact Pages</summary>
<br>

**ABOUT PAGE**

    Mobile Width 375px

![About page on mobile](docs/responsive/mobile-about-375.png)

<br>

    Tablet iPad Mini Width 768px

![About page on tablet](docs/responsive/tablet-about-ipadmini768.png)

<br>

    Desktop

![About page on desktop](docs/responsive/desktop-aboutcta-1368.png)

<br>

**CONTACT PAGE**

    Mobile Samsung Galaxy A5 Width 412px

![Contact page on mobile ](docs/responsive/mobile-contact-samsunga51412.png)

<br>

    Tablet Surface Duo Width 540px

![Contact page on tablet](docs/responsive/tablet-contact-surfaceduo540.png)

<br>

    Desktop Surface Pro Width 1369

![Contact page on laptop](docs/responsive/desktop-contact-surfacepro1368.png)

<br>
</details>

<details>
<summary>Error Pages</summary>
<br>

**ERROR 403**

    Mobile Width 320px

![Error 403 page on Mobile](docs/responsive/mobile-error403.png)

<br>

    Tablet Width 768px

![Error 403 on Tablet](docs/responsive/tablet-error403.png)

<br>

    Desktop Width 1024px

![Error 403 on Desktop](docs/responsive/desktop-error403.png)

<br>

**ERROR 404**

    Mobile Width 320px

![Error 404 on Mobile](docs/responsive/mobile-error404-iphonese375.png)

<br>

    Tablet Width 768px

![Error 404 page on tablet](docs/responsive/tablet-error404.png)

<br>

    Desktop 1024px

![Error 404 page on desktop](docs/responsive/desktop-error404.png)

<br>
</details>

[Back To Top](#table-of-contents)

_____

# Browser Compatibility

Website was tested on current Chrome, Firefox, Edge, Brave for compatibility. It was also tested on Safari on an iPad running on iOS 12.5.7 and an iPhone on the latest iOS.

<details>
<summary>Table of results</summary>
<br>

| Intended      | Chrome    | Firefox   | Edge  | Brave     | Safari iOS12   | Safari iOS16     |
|---------------|-----------|-----------|-------|-----------|----------------|------------------|
| Appearance    | Good      | Good      | Good  | Good      | Poor           | Good             |
| Responsiveness| Good      | Good      | Good  | Good      | Good           | Good             |

The issue with using Safari on iOS12 is that it doesn't support webp images, therefore all product images in the Shop Page and some of the images on the About Page were not visible.

<br>
</details>

[Back To Top](#table-of-contents)

_____

# User Stories

As mentioned in the Agile Methodology Section in the [README](readme.md), User Stories were created in [GitHub Issues]( https://github.com/MoniPar/reclaimed-treasures/issues) which guide the process for the development of this project.  Each User Story has been manually tested and the results have been collected in the tables below.  They have been organized by their respective Epics.  Please note that Epic 1 – Initial Setup, is not included in this section as it defines setup and installation.

<details>
<summary>Landing Page and Navigation</summary>
<br>

[User Story #11](https://github.com/MoniPar/reclaimed-treasures/issues/11)

As a User, I can land on the homepage of the site, so that I can learn more about the business and the types of products they sell.

|Acceptance Criteria | Test | Comments |
|---------------------------|-------|----------------|
|Website's URL directs user to the homepage | Achieved | |
|The Homepage has a clear overview of what the site is about | Achieved | |

[User Story #12](https://github.com/MoniPar/reclaimed-treasures/issues/12)

As a User, I can view the logo and the links in the navigation bar, so that I can easily navigate to other pages of the site.

| Acceptance Criteria | Test | Comments |
|---------------------------|-------|----------------|
| The header is displayed at the top of the page across all pages of the website | Achieved | |
|The main header displays the logo, links, search bar, account and shopping basket icons | Achieved | |
| Links to the other pages of the site can be easily accessed by all users | Achieved | Profile page can only be accessed by registered users |
| Hamburger button for mobile toggles navbar links | Achieved | |

[User Story #13](https://github.com/MoniPar/reclaimed-treasures/issues/13)

As a User, I can access contact details, social and developer links across all pages, so that I can follow/contact the business owner and the website creator.

| Acceptance Criteria | Test | Comments |
|---------------------------|-------|----------------|
| The footer is displayed at the bottom of the page across all pages of the website | Achieved | |
| Contact details and social links are clearly displayed on all screen sizes | Achieved | |
| Social links and privacy policy open in a new tab | Achieved | |
| Copyright date and link to website’s creator profile is included at the bottom | Achieved | |
| Contact link and newsletter signup are included at the top | Achieved | Contact link has been included with the useful links |

[User Story #14](https://github.com/MoniPar/reclaimed-treasures/issues/14)

As a business owner, I can have a banner with a CTA clearly visible on the landing page, so that users are encouraged to access the shop and view/buy products.

| Acceptance Criteria | Test | Comments |
|---------------------------|-------|----------------|
| A hero image that draws the eye and gives the user a visual representation of the artist’s designs | Achieved | |
| An overlay with text which encapsulates what the business is about | Achieved | |
| A visible Shop Now button which links to the Shop/Products page | Achieved | |

[User Story #15](https://github.com/MoniPar/reclaimed-treasures/issues/15)

As a User, I can read about the business, so that I can decide if I want to purchase from them or not.

| Acceptance Criteria | Test | Comments |
|---------------------------|-------|----------------|
| A short section about the products | Achieved | |
| A short section about the process | Achieved | |
| A link to more information which will lead to the About page | Achieved | |

[User Story #16](https://github.com/MoniPar/reclaimed-treasures/issues/16)

As a business owner, I can choose which products to feature on the landing page, so that users are encouraged to check them out.

| Acceptance Criteria | Test | Comments |
|---------------------------|-------|----------------|
| A products section which displays at least three categories of products | Yet to Achieve | |
| Each product is displayed on a card with name, image and a button which leads to the shop | Yet to Achieve | |

<br>
</details>

<details>
<summary>User Registration & Authentication</summary>
<br>

[User Story #7](https://github.com/MoniPar/reclaimed-treasures/issues/7)

As a User, I can register for an account so that I have access to other features of the website.

| Acceptance Criteria | Test | Comments |
|---------------------------|-------|----------------|
| A user can register for an account using a username, email and password | Achieved | |

[User Story #8](https://github.com/MoniPar/reclaimed-treasures/issues/8)

As a User, I can check my emails for a registration confirmation email, so that I can verify that my registration was successful.

| Acceptance Criteria | Test | Comments |
|---------------------------|-------|----------------|
| The user is asked to verify their email address upon registration | Achieved | |
| The user is directed to a temporary success URL if the email is verified | Achieved | |

[User Story #9](https://github.com/MoniPar/reclaimed-treasures/issues/9)

As a User, I can login and logout from my account, so that I can access my account’s information and keep my information secure.

| Acceptance Criteria | Test | Comments |
|---------------------------|-------|----------------|
| User is able to login to their account with their username and password | Achieved | |
| User is able to logout from their account | Achieved |

[User Story #10](https://github.com/MoniPar/reclaimed-treasures/issues/10)

As a User, I can reset my password, so that I can regain access to my account.

| Acceptance Criteria | Test | Comments |
|---------------------------|-------|----------------|
| User is able to reset their password by entering their email address | Achieved | |
| User receives email with a link directing them to the reset password form  | Achieved | |

[User Story #19](https://github.com/MoniPar/reclaimed-treasures/issues/19)

As a User, I can connect with my social media account, so that I can create an account.

| Acceptance Criteria | Test | Comments |
|---------------------------|-------|----------------|
| User can register using their Facebook account | Yet to Achieve | |

<br>
</details>

<details>
<summary>Product Management</summary>
<br>

[User Story #20](https://github.com/MoniPar/reclaimed-treasures/issues/20)

As a Shop Owner, I can use the Admin interface to add, update, view and delete products so that I can populate the online shop.

| Acceptance Criteria | Test | Comments |
|---------------------------|-------|----------------|
|The ability to add, update, view and delete categories in the admin panel | Achieved | |
|The ability to add products and their relative information and images via the admin panel | Achieved | |
|The ability to view a list of products, update and delete specific products via the admin panel | Achieved | |

[User Story #21](https://github.com/MoniPar/reclaimed-treasures/issues/21)

As a Store Owner, I can add a product via the User interface, so that I can add new items to my store.

|Acceptance Criteria | Test | Comments |
|---------------------------|-------|----------------|
| Store owner is able to add products to the store via a form on the frontend | Yet to Achieve | For now this can be done via the Admin interface |

[User Story #22](https://github.com/MoniPar/reclaimed-treasures/issues/22)

As a Store Owner, I can edit/update a product, so that I can change the product price, description, image and other product criteria.

|Acceptance Criteria | Test | Comments |
|---------------------------|-------|----------------|
| The Store Owner is able to update a product through a form on the frontend | Yet to achieve | For now this can be done via the Admin interface |

[User Story #23](https://github.com/MoniPar/reclaimed-treasures/issues/23)

As a Store Owner, I can delete a product, so that I can remove items that are no longer on sale.

|Acceptance Criteria | Test | Comments |
|---------------------------|-------|----------------|
| The Store Owner is able to delete a product via a form on the frontend | Yet to achieve | For now this can be done via the Admin interface |
|The Store Owner is able to update and delete a product via the quick links | Yet to achieve | For now updating and deleting products can only be done via the Admin interface |
|Only the Store Owner/Superuser is able to access this functionality | N/A | There is no functionality to test |

<br>
</details>

<details>
<summary>Product Viewing & Navigation</summary>
<br>

[User Story #24](https://github.com/MoniPar/reclaimed-treasures/issues/24)

As a Customer, I can view a list of products so that I can select some to purchase.

|Acceptance Criteria | Test | Comments |
|---------------------------|-------|----------------|
| The customer is able to see a list of products in the Shop/Products page | Achieved | |
| Each product card displays an image, name, price, category, pattern, rating and link  | Achieved | |
| The customer is able to view a specific category of products | Achieved | |
| The customer is able to quickly identify deals and new products | Achieved | |

[User Story #25](https://github.com/MoniPar/reclaimed-treasures/issues/25)

As a Customer, I can view individual product details, so that I can identify more information about the product.

|Acceptance Criteria | Test | Comments |
|---------------------------|-------|----------------|
| The customer is able to click on each individual product's image or link “view detail” to view more details about the product | Achieved | |
| The product detail page includes the product's description, additional info, stock status as well as quantity selector buttons and add to basket button | Achieved | Also a highlighted notice on Made to Order Products & a disabled “Not Available” button instead of the quantity selector buttons on products that are not available|
| The customer is able to see any available reviews on the product made by other customers or themselves | Achieved | |

[User Story #26](https://github.com/MoniPar/reclaimed-treasures/issues/26)

As a Customer, I can search for a specific product or view a category of products, so that I can quickly find products I'm interested in.

|Acceptance Criteria | Test | Comments |
|---------------------------|-------|----------------|
| Customer is able to search for a product by name | Achieved | |
| Customer is able to search for a product by other keywords found in the description | Achieved | |
| Customer is able to see what they've searched for and the number of results | Achieved | |
| Customer can return back to the shop page using the link at the front of the product count | Achieved | |
| Customer is able to see which category they have selected | Achieved | |

[User Story #27](https://github.com/MoniPar/reclaimed-treasures/issues/27)

As a Customer, I can sort the list of available products, so that I can easily identify the best rated & best priced categorically sorted products.
|Acceptance Criteria | Test | Comments |
|---------------------------|-------|----------------|
| User can sort all products as well as categories of products in desc and asc order | Achieved | |
| User can sort products by price in desc and asc order | Achieved | |
| User can sort products by rating in desc and asc order | Achieved | |
| User can sort products by name in desc and asc order | Achieved | |
| User can sort products by theme in desc and asc order | Achieved | |
| User can sort all products by category in desc and asc order| Achieved | |
| User can sort all products by availability in desc and asc | Partially Achieved | Not available products do not take precedence over made to order products yet |

[User Story #46](https://github.com/MoniPar/reclaimed-treasures/issues/46)

As a User, I can check products' reviews, so that I can make up my mind if I want to purchase the product.
As a Registered User, I can add a review, so that I can submit my feedback about a product.

|Acceptance Criteria | Test | Comments |
|---------------------------|-------|----------------|
| Users are able to see ratings for products in the shop | Achieved | Products that haven't yet been rated are marked as “No Rating” |
| Users are able to see reviews, if any, on each product's detail page | Achieved | |
| Registered users are able to rate and submit reviews of products | Achieved | |
| Registered customers are able to rate and submit reviews of products they have purchased | Achieved | |

[User Story #48](https://github.com/MoniPar/reclaimed-treasures/issues/48)

As a Customer, I can edit and delete my reviews, so that I have the ability to correct any mistakes I make.

|Acceptance Criteria | Test | Comments |
|---------------------------|-------|----------------|
| Registered customers can edit their submitted reviews | Achieved | |
| Registered customers can delete their submitted reviews | Achieved | |

[User Story #52]( https://github.com/MoniPar/reclaimed-treasures/issues/52)

As a User, I can easily navigate back to  the top of the page with one click, so I can easily access other parts of the website.

This User Story has been marked as won't have at this time as the user can easily navigate to other parts of the website because the Navigation bar is always fixed on top.

<br>
</details>

<details>
<summary>User Profile</summary>
<br>

[User Story #42](https://github.com/MoniPar/reclaimed-treasures/issues/42)

As a Registered Customer, I can have a personal user profile, so that I can save my payment info and view my order history and confirmations.

|Acceptance Criteria | Test | Comments |
|---------------------------|-------|----------------|
| A User profile is automatically created for the user upon registration | Achieved | | 
| Registered users are able to access their profile through the link in the navbar | Achieved | |
| Registered users are able to logout from their profile through the link in the navbar | Achieved | |

[User Story #43](https://github.com/MoniPar/reclaimed-treasures/issues/43)

As a Customer, I can edit personal information on my profile, so that I can use the correct details when processing future orders.

|Acceptance Criteria | Test | Comments |
|---------------------------|-------|----------------|
| The customer is able to update their personal information on their profile | Achieved | |
| The customer is able to see a history of their orders in their profile | Achieved | |
| The information saved in the profile can be retrieved in the Checkout form, if the user checks the save info box | Achieved | | 

<br>
</details>

<details>
<summary>Shopping Basket</summary>
<br>

[User Story #29](https://github.com/MoniPar/reclaimed-treasures/issues/29)

As a customer, I can access my basket so I can review items before I purchase them.

|Acceptance Criteria | Test | Comments |
|---------------------------|-------|----------------|
|Customer is able to access the basket page via the main navigation | Achieved | |
| Customers who have added products to their basket will be able to see the products | Achieved | |
| Customers who have not yet added products will see some text and a link to the shop | Achieved | |

[User Story #30](https://github.com/MoniPar/reclaimed-treasures/issues/30)

As a developer, I can create a context processor, so that I can access the basket related variables from other apps in my project.

This User Story should have been marked as a developer task.

[User Story #31](https://github.com/MoniPar/reclaimed-treasures/issues/31)

As a customer, I can add items and identify the total cost in the basket, so that I know how much I'm spending.

|Acceptance Criteria | Test | Comments |
|---------------------------|-------|----------------|
| The customer can add items to their basket | Achieved | |
| The customer can easily return back to the shop page from the basket page | Achieved | |
| The customer can view the subtotal and total sum of the items in their basket | Achieved | |

[User Story #32](https://github.com/MoniPar/reclaimed-treasures/issues/32)

As a developer, I can add functionality with the plus (+) and (-) buttons on the quantity selector, so that the user has a better experience adding products to their basket.

|Acceptance Criteria | Test | Comments |
|---------------------------|-------|----------------|
| The customer is able to use buttons to increase/decrease the quantity of the products they want to order from the product detail page | Achieved | |
| The customer is able to use buttons to increase/decrease the quantity of the products they want to order from the basket page | Achieved | |
| Using buttons the customer is only able to add up to 3 items on products that are Made to Order from the product detail page | Achieved | |
| Using buttons the customer is only able to add up to 3 items on products that are Made to Order from the basket page | Achieved | |

[User Story #33](https://github.com/MoniPar/reclaimed-treasures/issues/33)

As a Customer, I can update the quantity of each item in my basket, so that I can easily make changes to my order before checkout.

|Acceptance Criteria | Test | Comments |
|---------------------------|-------|----------------|
| The customer is able to update the quantity of each item in their basket via the update link | Achieved | |
| The customer is able to remove a product from their basket via the remove link | Achieved | |
| The customer is able to see the subtotal for the amount of each product in their basket | Achieved | |

[User Story #34](https://github.com/MoniPar/reclaimed-treasures/issues/34)

As a User, I can see real-time notifications as I interact with the website, so that I can have a better experience.

|Acceptance Criteria | Test | Comments |
|---------------------------|-------|----------------|
| The User is provided with neat and clear notifications when using functional features of the site | Achieved | |
| The notifications are designed to display the result of the user's interaction | Achieved | |

<br>
</details>

<details>
<summary>Checkout</summary>
<br>

[User Story #35](https://github.com/MoniPar/reclaimed-treasures/issues/35)

As a developer, I can create a checkout app, so that I can implement functionality for the customer to enter information and view their delivery cost, order and grand total.

This user story should have been marked as a developer task.

[User Story #36](https://github.com/MoniPar/reclaimed-treasures/issues/36)

As a customer, I can confirm my items and total cost in the checkout page, so that I can continue to enter the required information to complete my order.

|Acceptance Criteria | Test | Comments |
|---------------------------|-------|----------------|
| Customer is able to view the items they want to order | Achieved | |
| Customer is able to view the order cost, delivery cost and grand total | Achieved | |
| Customer is easily able to enter their information and delivery/billing address in the required fields | Achieved | |
| Customer can go back to the basket page to add, replace or delete items | Achieved | |

[User Story #37](https://github.com/MoniPar/reclaimed-treasures/issues/37)

As a developer, I can use Stripe Elements, so that I can setup a secure payment system to the online shop.

|Acceptance Criteria | Test | Comments |
|---------------------------|-------|----------------|
| A payment field matching all other fields is displayed on the checkout page | Achieved | |
| The payment field required a card number, expiration date and cvc (poscode for US) | Achieved | |
| An invalid card number turns red | Achieved | An error msg is also displayed |

[User Story #38](https://github.com/MoniPar/reclaimed-treasures/issues/38)

As a Customer, I can easily enter my payment information, so that I can checkout quickly and efficiently.

|Acceptance Criteria | Test | Comments |
|---------------------------|-------|----------------|
| The form is submitted by entering any test card number and any other digits for the rest | Achieved | |
| A successful payment notification is displayed in Stripe/developers/events | Achieved | | 

[User Story #39](https://github.com/MoniPar/reclaimed-treasures/issues/39)

As a customer, I can view an order confirmation after checkout, so that I can confirm that my order was successful.

|Acceptance Criteria | Test | Comments |
|---------------------------|-------|----------------|
| The customer is able to see their products and totals in the checkout page | Achieved | | 
| The customer is alerted to enter required fields in the checkout form | Achieved | |
| If the form is valid the customer is able to checkout using the test card number | Achieved | |
| The customer is then directed to the checkout success page where they can see their order summary | Achieved | See Checkout Success Image below |
| Stripe shows payment intent succeeded | Achieved | See Payment Intent Succeeded below |
| The order is created with all the expected lineitems and the order in the admin panel | Achieved |See Order & Line Items below |
| The stock (on products in stock) is deducted on the product table in the admin panel | Achieved | |

<details>
<summary>VRT Checkout Success</summary>
<br>

![VRT Checkout Success ](docs/features/checkoutsuccess.png)

<br>
</details>

<details>
<summary>Stripe Payment Intent Succeeded</summary>
<br>

![Stripe Payment Intent Succeeded](docs/features/stripe-paymentintentsucceeded.png)

<br>
</details>

<details>
<summary>Admin Order & Line Items</summary>
<br>

![Admin Order](docs/features/admin-order.png)

![Admin Line Items](docs/features/admin-lineitems.png)

<br>
</details>

<details>
<summary>Test results for a typical successful order</summary>
<br>

|Acceptance Criteria | Test | Comments |
|--------------------|------|----------|
| A loading modal informs the user that the transaction is being processed | Achieved | |
| The Order Success Confirmation page is displayed with order details | Achieved | |
| The payment intent is successfully created in Stripe printing out “verified order already in the database” | Achieved | |
| The order is submitted to the DB | Achieved | |
| The stock is decremented | Achieved | |
| The basket is cleared | Achieved | |
| Order confirmation can be found in registered user’s profile | Achieved | |
| Confirmation email received | Achieved | |

<br>
</details>

[User Story #40](https://github.com/MoniPar/reclaimed-treasures/issues/40)

As a developer, I can make sure that customers can confidently provide the information required safely and securely so that they can have a positive experience on the site.

Webhook handler for issues during checkout transactions tested in *development*: Simulated by commenting out `form.submit()` in stripe_elements.js

|Acceptance Criteria | Test | Comments |
|---------------------------|-------|----------------|
| A loading modal informs the user that the transaction is being processed | Achieved | |
| The payment intent is successfully created in Stripe printing out "Created order in webhook" | Achieved | |
| The order is submitted to the DB | Achieved | |
| The stock is decremented | Yet to Achieve | |
| The basket is cleared | Yet to Achieve | |
| Order confirmation can be found in registered user's profile | Achieved | |
| Confirmation email received | Achieved | |

Webhook handler for issues during checkout transactions tested in *production*: Simulated by closing the website before checkout success page is displayed. Two different outcomes from the number of tests undertaken:

| Criteria | Outcome 1 | Outcome 2 |
|----------|-----------|-----------|
| A loading modal informs the user that the transaction is being processed | Achieved | Achieved |
| User closes the tab before checkout success page is displayed | Achieved | Achieved |
| The payment intent is successfully created in Stripe printing out “Created order in Webhook” | Not Achieved - “Verified order already in the database” | Achieved | 
| The order is submitted to the DB | Achieved | Achieved |
| The stock is decremented | Achieved | Not Achieved |
| The basket is cleared | Achieved | Not Achieved |
| Order confirmation can be found in registered user's profile | Not Achieved | Achieved |
| Confirmation email received | Achieved | Achieved |

[User Story #41](https://github.com/MoniPar/reclaimed-treasures/issues/41)

As a developer, I can decrement stock on payment success, so that I can add functionality when item becomes out of stock.

|Acceptance Criteria | Test | Comments |
|---------------------------|-------|----------------|
| “Stock: (no. of stock)” is displayed on the UI on each product detail | Achieved | |
| Product stock is decremented upon normal successful order | Achieved | Yet to achieve when order is created in webhook |
| When product stock is 0, the “Stock: (no. of stock)” on the UI changes to “Made to Order” | Achieved | |
| Max quantity one can order on products that have sufficient stock is 10 | Achieved | |
| Max quantity one can order on Made to Order products is 3 | Achieved | | 
| Max quantity overflow one can order on products that have insufficient stock is 3   | Achieved | |

[User Story #44](https://github.com/MoniPar/reclaimed-treasures/issues/44)
As a customer, I can receive email confirmation after checkout, so that I can keep the confirmation of the transaction for my records.
|Acceptance Criteria | Test | Comments |
|---------------------------|-------|----------------|
| The customer receives a confirmation email of their order | Achieved | |
| The registered customer is able to view their order history in their profile even if the checkout success page fails | Mixed Results | See [User Story #40](https://github.com/MoniPar/reclaimed-treasures/issues/40) |

<br>
</details>

<details>
<summary>SEO & WebMarketing</summary>
<br>

[User Story #18](https://github.com/MoniPar/reclaimed-treasures/issues/18)

As a user, I can sign up to the website’s newsletter so that I can keep updated with the latest news, offers, products and pop up stalls.

|Acceptance Criteria | Test | Comments |
|---------------------------|-------|----------------|
| A Newsletter email signup form is displayed on the footer | Achieved | |
| When user enters email address and hits subscribe, a success message is displayed below the field | Achieved | |
| Email address is recorded on the Mailchimp account | Achieved |

[User Story #50](https://github.com/MoniPar/reclaimed-treasures/issues/50)

As a business owner, I can have my Facebook business page linked with my website, so that I can connect and interact with my customers directly and potentially extend my reach through posts and other content creation. 

|Acceptance Criteria | Test | Comments |
|---------------------------|-------|----------------|
| Website users can access the Facebook page through the link in the footer and on the contact page | Achieved | |
| Facebook users can access the website through the link on the Facebook account and posts | Achieved| |
| Facebook page has relevant information about the business, including keywords used through the website | Achieved | |

[User Story #50](https://github.com/MoniPar/reclaimed-treasures/issues/50)

As a developer, I can add metadata, a sitemap and robots.txt file so that the website can be found and ranked by search engines.

|Acceptance Criteria | Test | Comments |
|---------------------------|-------|----------------|
| The description & relevant keywords and titles are included on the main pages of the website’s metatags | Achieved | |
| A sitemap.xml file is included in the project’s root folder | Achieved | |
| A robots.txt file is also included in the project’s root folder | Achieved | |

<br>
</details>

<details>
<summary>Other Features</summary>
<br>

[User Story #47](https://github.com/MoniPar/reclaimed-treasures/issues/47)

As a user, I can navigate to the About page, so that I can learn more about the shop owner and her business.

|Acceptance Criteria | Test | Comments |
|---------------------------|-------|----------------|
| User can easily navigate to the About page from the navigation link and the About me link on the Home page | Achieved | | 
| An image of the shop owner is displayed here | Achieved | |
| Information about the shop owner and her business are displayed here | Achieved | |
| A CTA with a link to the shop | Achieved | Carousel slide |
| A card with a link to the contact page | Achieved | Carousel slide |

[User Story #17](https://github.com/MoniPar/reclaimed-treasures/issues/17)

As a user, I can quickly write a message to the business owner using the contact form, so that I can ask questions or give feedback.

|Acceptance Criteria | Test | Comments |
|---------------------------|-------|----------------|
| Contact page displays hero with a heading inviting users to get in touch | Achieved | |
| Some text with info about why should users get in touch is displayed | Achieved | |
| Contact info including: phone, email, social links are also included here | Achieved | |
| Social links open in a new tab | Achieved | | 
| A Contact form with fields for: Subject, email, phone no., and message box are displayed | Achieved | |
| User is alerted to any missing information when they try to submit the form with empty required fields | Achieved | |
| When form is valid, user is directed to a Thank You page with a message and a link to the Home Page | Achieved | |
| Form information is recorded in the DB | Achieved | |
| Shop owner receives an email with subject, user's name, email, phone and message | Achieved | See image below |

<detail>
<summary>Contact form query alert email</summary>
<br>

![Contact mail received](docs/features/contactemailreceipt.png)

<br>
</detail>

[User Story #55](https://github.com/MoniPar/reclaimed-treasures/issues/55)

As a developer, I can build custom error pages, so that the user remains on the site and has a way to get back to the homepage or access navigation.

|Acceptance Criteria | Test | Comments |
|---------------------------|-------|----------------|
| Custom error pages have styles that match the website | Achieved | |
| The pages define the error and display a button which brings the user back to the homepage | Achieved | |

<br>
</details>

[Back To Top](#table-of-contents)

_____

# Features

Each feature listed in the [README.md](README.md) file has been manually tested on the browsers listed in [Browser Compatibility Testing](#browser-compatibility) and the results are listed in the tables below.

<details>
<summary>Header & Navigation</summary>
<br>

**Top Navigation**

*Unregistered / Not logged in user*

| Feature | Action | Effect |
|------------|----------|---------|
| Logo	| hover over	 | address shows as home 	|
|	| click/tap	 | directs to Home Page 		|
| Search icon on mobile	 | tap		|  colour changes, search field opens below |
| Search bar	| click/tap  text input	| gets focus and prompt for text |
|		| type & enter		| directs to Shop Page with query |
|		| enter only		| directs to Shop Page all products |
| Search icon on desktop| hover over 	| colour changes, tooltip “Submit my search request”|
|			 | click		| directs to Shop Page all products |
| Account icon	| hover over	| colour changes, tooltip “My Account”, address shows as # |
|		|click/tap	| drops down Register, Login links |
| Register link	| hover over	| gets background colour, address shows as signup|
|		| click / tap	| directs to Registration Page |
| Login link	| hover over 	| gets background colour, address shows as login |
|		| click / tap	| directs to Login Page |
|Basket Icon on mobile | tap 	| colour changes, drops down basket total link |
|Basket total link	|tap	| directs to Shopping Basket |
|Basket Icon on desktop | hover over | colour changes, tooltip “Shopping Basket”, address changes to basket |
|			| click / tap    | directs to Shopping Basket Page |

All Tests Passed

<br>

*Registered / Logged in user*

| Feature | Action | Effect |
|------------|----------|---------|
| My Profile link	| hover over	|gets background colour,  address shows as profile |
|		| click / tap	| directs to user’s Profile Page |
| Logout link	| hover over 	| gets background colour, address shows as logout |
|		| click / tap	| directs to Log Out Page |

All Tests Passed

<br>

**Main Navigation**

| Feature | Action | Effect |
|------------|----------|---------|
| Hamburger button on mobile | tap | toggles down menu |
| Home link	| hover over	| colour changes, address shows as home |
|		| click / tap 	| directs to Home Page |
|Shop link	|hover over	| colour changes, address shows # |
|		| click / tap	| drops down menu with more links |
| CDs link	|hover over	| background colour changes, address shows as shop/?category=cd |
|		| click / tap	| directs to Shop Page with category CD |
| Glassware link	| hover over	| background colour changes, address shows as shop|?category=glassware |
|		| click / tap	| directs to Shop Page with category Glassware |
| Frames link	| hover over	| background colour changes, address shows as shop/?category=frames |
|		| click / tap	| directs to Shop Page with category Frames |
| Pebbles link	| hover over 	| background colour changes, address shows as shop/?category=pebbles |
|		| click / tap	| directs to Shop Page with category Pebbles |
| New link	| hover over	| background colour changes, address shows as shop/?category=new |
|		| click / tap	| directs to Shop Page with category New |
| Deals link	| hover over	| background colour changes, address shows as shop/?category=deals |
|		| click / tap 	| directs to Shop Page with category Deals |
| All Products link | hover over | background colour changes, address shows as shop/?category=cds,glassware,frames,pebbles,new,deals |
|		| click / tap	| directs to Shop Page with all products |
| About link	| hover over 	| colour changes, address shows about |
|		| click / tap	| directs to About Page |
| Contact link	| hover over	| colour changes, address shows contact |
|		| click / tap	| directs to Contact Page |

All Tests Passed

<br>
</details>

<details>
<summary>Footer</summary>
<br>

| Feature | Action | Effect |
|------------|----------|---------|
| Newsletter Email field	| click / tap text input    | gets focus and prompt for text, red text below “This field is required” |
| Subscribe button          | hover over	            | changes colour |
| 		                    | click / tap	            | text below “Thank you for subscribing!” |
| Website logo	            | hover over                | address shows home |
|		                    | click / tap               | directs to Home Page |
| Contact phone             | hover over                | changes colour, address shows phone number |
|		                    | click / tap               | opens new tab / asks to open or switch app |
| Contact email             | hover over                | changes colour, address shows mailto:vera@reclaimedtreasures.mt |
|		                    | click / tap               | opens outlook, mail, gmail or asks how to open or switch app |
| Follow Me Facebook link 	| hover over                | changes colour, address shows https://www.facebook.com/verasreclaimedtreasures |
|				            | click / tap	            | opens new tab to Facebook page |
| Follow Me Instagram link	| hover over                | changes colour, address shows https://www.instagram.com |
|				            | click / tap 	            | opens new tab to Instagram |
| Useful links privacy policy	| hover over	        | changes colour, address shows to https://www.privacypolicygenerator.info/... |
|				            | click / tap	            | opens new tab to VRT’s privacy policy |
| Useful links contact link	| hover over	            | changes colour, address shows Contact Page |
|				            | click / tap	            | directs to Contact Page |
| Useful links EcoMarket Malta	| hover over	        | changes colour, address shows https://ecomarketmalta.wordpress.com |
| 				            | click / tap	            | opens new tab to EcoMarket Malta |
| Copyright link			| hover over	            | changes colour, address shows https://www.linkedin.com/in/monique-parnis |
|				            | click / tap	            | opens new tab to Linked In Profile |

All Tests Passed

<br>
</details>

<details>
<summary>Landing Page Hero & Home Content</summary>
<br>

| Feature | Action | Effect |
|------------|----------|---------|
| Large Hero	| View	| displays large background image with keywords “Upcycled Home Décor / Revibe your space with a conscience” and a Shop Now button |
| Shop Now button 	|hover over	| changes colour and background colour, address shows shop |
|			| click / tap	| directs to Shop Page with all products |
| Home Content 	| View		| 3 cards with icon, heading, text & button |
| About Me button	| hover over	| changes colour and background colour, address shows about |
|			| click / tap	| directs to About Page |
| Get in Touch button 	| hover over	| changes colour and background colour, address shows contact |
|			| click / tap	| directs to Contact Page |
| My Collection button	| hover over	| changes colour and background colour, address shows shop |
|			| click / tap	| directs to Shop Page with all products |

All Tests Passed

<br>
</details>

<details>
<summary>Shop/All Products</summary>
<br>

**All Products**

| Feature	 | Action 	| Effect 		|
|--------------------|--------------------|-------------------|
| Shop Page	| View		| Products Heading, Category badges, Link to All Products, Product Count, Sort Selector Box, Product Cards |
| Category badges | View	| Glassware, Pebbles, Frames, CDs, Deals, New button shaped badges |
| Glassware	| Hover over	| Change colour and background colour, address shows shop/?category=glassware |
| 		| click / tap	| Directs to a products view of product cards with a category of glassware |
| Pebbles	| Hover over	| Change colour and background colour, address shows shop/?category=pebbles |
|		| click / tap	| Directs to a products view of product cards with a category of pebbles |
| Frames	| Hover over	| Change colour and background colour, address shows shop/?category=frames |
|		| click / tap	| Directs to a products view of product cards with a category of frames |
| CDs		| Hover over	| Change colour and background colour, address shows shop/?category=cds |
|		| click / tap	| Directs to a products view of product cards with a category of cds |
| Deals		| Hover over	| Change colour and background colour, address shows shop/?category=deals |
|		| click / tap	| Directs to a products view of product cards with a category of deals |
| New		| Hover over	| Change colour and background colour, address shows shop/?category=new |
|		| click / tap	| Directs to a products view of product cards with a category of new |
| Products Home link	| Hover over	| Changes colour, gets underline |
|			| click / tap	| Directs back to all products, clears category badges |
| Product Counter	| View		| Changes depending on the number of products displayed on the page |

All Tests Passed

<br>

**Sort-Selector**

| Feature	 | Action 	| Effect 		|
|--------------------|--------------------|-------------------|
| Sort-selector box	| click / tap 	| drops down a list of sort choices |
| Price (low to high)	| click / tap / enter |Sorts products by price ascending |
| Price (high to low) 	| click / tap / enter |Sorts products by price descending |
| Rating (low to high)	| click / tap / enter |Sorts products by rating ascending |
| Rating (high to low)	| click / tap / enter |Sorts products by rating descending |
| Name (A – Z)		| click / tap / enter |Sorts products by name alphabetical order |
| Name (Z – A)		| click / tap / enter |Sorts products by name reverse alphabetical |
| Theme (A – Z)		| click / tap / enter |Sorts products by theme alphabetical order |
| Theme (Z – A)		| click / tap / enter |Sorts products by theme reverse alphabetical |
| Category (A – Z)	| click / tap / enter |Sorts products by category alphabetical order |
| Category (Z – A)	| click / tap / enter |Sorts products by category reverse alphabetical |
| Availability (low to high) | click / tap / enter | Sorts products by availability ascending |
| Availability (high to low) | click / tap / enter | Sorts product by availability descending | 

All tests passed but sorting by availability does not give precedence to Not Available products. 

<br>

**Product Cards**

| Feature	 | Action 	| Effect 		|
|--------------------|--------------------|-------------------|
| Product image	| hover over	| address shows shop/product id |
|			| click / tap	| directs to Product Detail Page |
|Name			| view		| displays product name	|
|Price			| view		| displays product price		|
|Category link		| view		| displays product category |
|			|hover over	| gets underline, address shows shop/?category=”specific product category” |
|			| click / tap	| directs to specific category products view |
| Theme		| view		| displays product theme	|
| Rating			| view		| displays product rating or No rating |
| View details link	| hover over	| gets underline, address shows shop/product id |

All Tests Passed

<br>
</details>  

<details>
<summary>Product Detail</summary>
<br>

**Product Detail Section**

| Feature	 | Action 	| Effect 		|
|--------------------|--------------------|-------------------|
| Product image 	| hover over 	| address shows s3.amazonaws.com/media/<image file name>.jpg |
| 	| click / tap	| directs to full page image file |
| Category link		| hover over	| address shows shop/?category=<category name> |
|	| click / tap	| directs to specific category products view |
| Additional information| hover over	|gets underline, address shows shop/<product id>/# |
|	| click / tap	| opens dropdown with additional information |
| Quantity Selector (-) 	| default view	| lighter in colour than the (+) selector |
|			| hover over | colour changes, tooltip “Decrease Quantity” |
|	| click / tap	| no effect |
| Quantity Selector (+) 	| default view	| darker in colour than the (-) selector |
|			| hover over | colour changes, tooltip “Increase Quantity” |
|	| click / tap	| quantity in input box is incremented |
| Input field	| type non digits	| no effect |
|		| type digits		| displays digits |
|		| leave blank		| no effect |
| Add to Basket button	| hover over 	| change colour |
|	| click / tap	| if quantity is valid, success message is triggered and product + quantity are added to basket|
|	|		|if quantity is invalid, error message is triggered | 
| Back to shop button	| hover over 	| changes colour & background, address shows shop |
|	| click / tap	| directs back to products page |

All Tests Passed

<br>

The following tables test further functionality on the Quantity Selector and Add to Basket buttons depending on certain conditions. 

**Quantity Selector on Made to Order Products**

| Feature | Condition | Action | Effect |
|------------|-------------|----------|---------|
| (+) button | input field default (=1) | repeated clicks / taps | increments until quantity = 3 |
| (-) button | input field default (=1) | repeated clicks / taps | decrements until quantity = 1 |
| Add to basket button | input field value = 0 |click / tap| triggers error message value must be > or = 1 |
| 	| input field value is > 3 | click / tap | triggers error message value must be < or = 3 |
| 	| input field value is negative  integer | click / tap | triggers error message value must be > or = 1 |
|	| input field value >= 1 and <= 3 | click / tap | triggers success toast and adds product + quantity to basket |
|	| input field value is none | click / tap | triggers success toast and adds product + quantity of 0 to basket |

All Tests Passed

<br>

**Quantity Selector on Products in Stock**

| Feature | Condition | Action | Effect |
|------------|-------------|----------|---------|
| (+) button | input field default (=1) | repeated clicks / taps | increments until quantity = 10 |
| (-) button | input field default (=1) | repeated clicks / taps | decrements until quantity = 1 |
| Add to basket button | input field value = 0 |click / tap| triggers error message value must be > or = 1 |
| 	| input field value is > 10 | click / tap | triggers error message value must be < or = 10 |
| 	| input field value is negative integer | click / tap | triggers error message value must be > or = 1 |
|	| input field value >= 1 and <= 10 | click / tap | triggers success toast and adds product + quantity to basket |
|	| input field value is none | click / tap | triggers success toast and adds product + quantity of 0 to basket |

All Tests Passed

<br>
</details>  

<details>
<summary>Product Reviews</summary>
<br>

*Unregistered / Not Logged-in User*

**Without Reviews**

| Feature	 | Action 	| Effect 		|
|--------------------|--------------------|-------------------|
| Heading 	| view		| Customer reviews for <specific product name> |
| Text		| view		| There are currently no reviews on this product |
| Register link	| hover over	| gets underline, address shows accounts/signup |
|		| click / tap	| directs to Register Page |
| Login link	| hover over	| gets underline, address shows accounts/login	|
|		| click / tap	| directs to Login Page 	|
| Back to Shop button | hover over	| change colour & background, address shows shop |

All Tests Passed

<br>

**With Reviews**

| Feature	 | Action 	| Effect 		|
|--------------------|--------------------|-------------------|
| Heading 	| view		| Customer reviews for <specific product name> |
| Review cards	| view	| include rating, comment, name of reviewer, date of review submission |
| Register link	| hover over	| gets underline, address shows accounts/signup |
|		| click / tap	| directs to Register Page |
| Login link	| hover over	| gets underline, address shows accounts/login	|
|		| click / tap	| directs to Login Page 	|
| Back to Shop button | hover over	| change colour & background, address shows shop |

All Tests Passed 

<br>

*Registered / Logged-in User*

**Without Reviews**

| Feature	 | Action 	| Effect 		|
|--------------------|--------------------|-------------------|
| Heading 	| view		| Customer reviews for <specific product name> |
! Add review button | hover over | changes colour, address shows reviews/add_review/<product id> |
| 		| click / tap	| directs to Add Review Page |
| Text		| view		| There are currently no reviews on this product |
| Small text	| view		| To submit a review for this product please use the Add Review button above. Thank You |
| Back to Shop button | hover over	| change colour & background, address shows shop |

All Tests Passed

<br>

*Registered / Logged-in User*

**With Reviews (not own)**

| Feature	 | Action 	| Effect 		|
|--------------------|--------------------|-------------------|
| Heading 	| view		| Customer reviews for <specific product name> |
! Add review button | hover over | changes colour, address shows reviews/add_review/<product id> |
| 		| click / tap	| directs to Add Review Page |
| Review cards	| view	| include rating, comment, name of reviewer, date of review submission |
| Small text	| view		| To submit a review for this product please use the Add Review button above. Thank You |
| Back to Shop button | hover over	| change colour & background, address shows shop |

All Tests Passed

<br>

*Registered / Logged-in User*

**With Own Review**

| Feature	 | Action 	| Effect 		|
|--------------------|--------------------|-------------------|
| Heading 	| view		| Customer reviews for <specific product name> |
! Edit review button | hover over | changes colour, address shows reviews/edit_review/<review id> |
| 		| click / tap	| directs to Edit Review Page |
| Review cards	| view	| include rating, comment, name of reviewer, date of review submission |
| Own review card | view | includes above with own name as well as Edit and Delete buttons |
| Edit button	| hover over | changes colour & background, address shows reviews/edit_review/<review id> |
|		| click / tap	| directs to Edit Review Page |
| Delete button | hover over | changes colour & background, address shows reviews/delete_review/<review id> |
| 		| click / tap	| directs to Delete Review Page |
| Small text	| view		| You have already submitted  a review for this product! If you would like to update your review, please use the Edit Review button above. Thank You! |
| Back to Shop button | hover over	| change colour & background, address shows shop |

All Tests Passed

<br>
</details>

<details>
<summary>Add Review</summary>
<br>

The Add Review Page is accessed via the Product Detail Page by a logged-in user who hasn't as yet submitted a review for that particular product.

| Feature	 | Action 	| Effect 		|
|--------------------|--------------------|-------------------|
| Rating choice field	| click / tap | Opens dropdown with rating choices 1 to 5 |
|			| select	| Selected number displayed in rating field |
| Comment	| click / tap | Prompt for text input |
| Cancel button | hover over | changes colour & background, address shows shop/<product id> |
|	| click / tap | Redirects to Product Detail Page |
| Add button | hover over | changes colour |
|	| click / tap | if form is not valid, error messages displayed to fill in required fields |  
|	| click / tap | if form is valid redirect back to Product Detail Page, get success toast |

All Tests Passed

<br>
</details>

<details>
<summary>Edit Review</summary>
<br>

The Edit Review Page is accessed via the Product Detail Page by a logged-in user who has already submitted a review for that particular product

| Feature	 | Action 	| Effect 		|
|--------------------|--------------------|-------------------|
| Edit Review form	| view	| Pre-populated |
| Rating choice field	| click / tap | Opens dropdown with rating choices 1 to 5 |
|			| select	| Selected number displayed in rating field |
| Comment	| click / tap | Prompt for text input |
| Cancel button | hover over | changes colour & background, address shows shop/<product id> |
|	| click / tap | Redirects to Product Detail Page |
| Update  button | hover over | changes colour | 
|	| click / tap | if form is not valid, error messages displayed to fill in required fields |  
|	| click / tap | if form is valid redirect back to Product Detail Page, get success toast |

All Tests Passed

<br>
</details>

<details>
<summary>Delete Review</summary>
<br>

The Delete Review Confirmation Page is accessed via the Product Detail Page by a logged-in user who has already submitted a review for that particular product.

| Feature	 | Action 	| Effect 		|
|--------------------|--------------------|-------------------|
| Delete Review Confirmation | view | Confirms with user that they want to delete review |
| Cancel button | hover over | changes colour & background, address shows shop/<product id> |
|	| click / tap | Redirects to Product Detail Page |
| Yes, Delete  button | hover over | changes colour | 
|	| click / tap | Deletes review, redirects to Product Detail Page, triggers success toast |

All Tests Passed

<br>
</details>

<details>
<summary>Defensive Tests on Reviews</summary>
<br>

The following table includes tests for preventing unauthorised users from adding, updating and deleting reviews as well as logged in users who have already submitted a review on a particular product.

| User  | Feature	 | Action 	| Effect 		|
|-------|------------|----------|---------------|
| Not logged in | add review page | type `/reviews/add_review/<any available product id>` at the end of url | directed to Login Page |
|       | edit review page | type `/reviews/edit_review/<any available review id>` at the end of url | directed to Login Page |
|       | delete review page | type `/reviews/delete_review/<any available review id>` at the end of url | directed to Login Page |
| Logged in | edit someone else's review | type `/reviews/edit_review/<review id of another user>` at the end of url | directed to Forbidden 403 |
|       | delete someone else's review | type `/reviews/delete_review/<review id of another user>` at the end of url | directed to Forbidden 403 |
| Has reviewed | add review page | type `/reviews/add_review/<reviewed product id>` at the end of url | directed to Product Detail Page with warning toast |

All Tests Passed

<br>

    Unauthorised review editing

![Forbidden 403 Access Denied](docs/features/defensive-editreview.png)

<br>

    Unauthorised review deletion

![Forbidden 403 Access Denied](docs/features/defensive-deletereview.png)

<br>

    User has reviewed warning message

![Warning message for user who has already reviewed product](docs/features/defensive-addreview.png)

<br>
</details>

<details>
<summary>Basket</summary>
<br>

The Basket Page can be accessed via the basket icon on the top navigation bar as well as by the button that appears in the toast after adding a product to the basket.

**Empty Basket** 

| Feature	 | Action 	| Effect 		|
|--------------------|--------------------|-------------------|
| Text	| view	| You haven’t added anything to your basket yet! |
| Back to Shop button | hover over | changes colour & background, address shows shop |

All Tests Passed

<br>

**Items in Basket**

The following table is the default test scenario of the interactive elements on the Basket Page. 

| Feature	 | Action 	| Effect 		|
|--------------------|--------------------|-------------------|
| (-) button	| hover over	| changes colour |
|		| click / tap	| decrements quantity in input field |
| (+) button	| hover over 	| changes colour |
|		| click / tap	| increments quantity in input field |
| Update button | hover over 	| changes colour and background colour |
| 		| click / tap	| product quantity updated, totals change depending on the quantity, success toast displays updated product & basket summary |
| Remove button | hover over	| changes colour and background colour |
| 		| click / tap 	| product removed, totals change, success toast displays updated product & basket summary |
| Keep Shopping button | hover over | changes colour & background colour, address shows shop |
|			| click / tap | directs to Shop / All Products Page |
| Secure Checkout button | hover over | changes colour, address shows checkout |
|		| click / tap | directs to Checkout Page |

All Tests Passed

<br>

The following table tests the quantity selector buttons on certain conditions.

| Feature	 |Condition 	| Action 	| Effect 		|
|--------------------|--------------------|-------------------|--------------------|
| Quantity selector (-) dimmed 	| quantity = 1 | hover over | changes colour |
|		| 		| click / tap | no effect |
|Quantity selector (-) 		| quantity > 1 | repeated clicks / taps | decrements till quantity = 1, becomes dimmed |
|	*	| quantity = 0	| click / tap | decrements to negative integer |
|	*	| quantity = None | click / tap | decrements to negative integer |
| Quantity selector (+)	| product in stock | click / tap | increments till quantity = 10, becomes dimmed |
|		|product Made to Order | click / tap | increments till quantity = 3, becomes dimmed |
| 	*	| quantity > 10 | click / tap | quantity keeps being incremented |

All Tests Passed -> Tests marked with * have unwanted consequences, further validation has been written to amend this.

<br>

The following table tests functionality of the Update button on Made to Order products.

| Feature	 |Condition 	| Action 	| Effect 		|
|--------------------|--------------------|-------------------|--------------------|
|Update button | quantity <= 3 | click / tap | success toast | 
|		| quantity > 3 | click / tap | error toast – only up to 3 allowed |
|	^	| quantity <= 0 | click / tap | removes product from basket |
|	^	| quantity = None | click / tap | removes product from basket |

All Tests Passed -> Tests marked with ^ amend the unwanted consequences from previous tests.

<details>
<summary>Error Toast for quantity > 3</summary>
<br>

![Error toast for quantity > 3](docs/features/mobile-basketerrormessage.png)

<br>
</details>

<br>

The following table tests functionality of the Update button on products in stock.

| Feature	 |Condition 	| Action 	| Effect 		|
|--------------------|--------------------|-------------------|--------------------|
|Update button | quantity < product stock | click / tap | success toast | 
|		| quantity > product stock by < 3 | click / tap | success toast |
|	*	|quantity > product stock by > 3 | click / tap | success toast |
|	^	| quantity <= 0 | click / tap | removes product from basket |
|	^	| quantity = None | click / tap | removes product from basket |
|	^	| quantity > 10 	| click / tap | error toast – adjust quantity to < 10 |

All Tests Passed -> Test marked with * has unwanted consequences, further validation has been written to amend this using the Secure Checkout button.  Tests marked with ^ amend the unwanted consequences from previous tests.

<details>
<summary>Error Toast for quantity > 3</summary>
<br>

![Error toast for quantity > 10](docs/features/toasterror-quantityover10.png)

<br>
</details>

<br>

The following table tests functionality of the Secure Checkout button for validation that hasn't been captured with the Quantity Selector buttons or the Update button.

| Feature	 |Condition 	| Action 	| Effect 		|
|--------------------|--------------------|-------------------|--------------------|
|Secure Checkout button | quantity > product stock by > 3 | click / tap | error toast: adjust quantity to stay within overflow limit |
|	-	|quantity = 0 | click / tap | directs to Checkout Page with Item marked as quantity 0 and a subtotal of 0 |
| 	-	|quantity = None | click / tap | directs to Checkout Page with Item marked as quantity 1 and subtotal of 1 x item price |  

All Tests Passed -> The tests marked with - don't have the ideal effect but the user can always go back by clicking the Adjust Basket button and update the quantity or remove the items.  If the user decides to continue with the checkout process nonetheless, their order confirmation will have the item with the quantity = 0 at no charge and the item with the quantity set to None in the basket as 1 with charge.  The order will be processed and recorded in the database as the user's order confirmation displays.  The item with the quantity = 0 will not be deducted from the product stock.  

<details>
<summary>Error Toast for quantity > product stock by more than 3</summary>
<br>

![Error toast for quantity greater than the overflow of 3](docs/features/toasterror-overflow.png)

<br>
</details>

<br>

</details>

<details>
<summary>Checkout</summary>
<br>

**Checkout Page**

*Registered / Logged in Users*

| Feature	 | Action 	| Effect 		|
|--------------------|--------------------|-------------------|
| Form Validation | submit form with required fields left blank | tooltip directs user to fill in required field |
| Save info box 	| Tick and check profile info after checkout | profile details populated with correct info |
| Payment field | Enter invalid card no | text goes red, error message below “x your card number is invalid” | 
| Adjust Basket button | hover over | colour & background changes, address shows basket |
|	| click / tap	| directs to Basket Page |
| Complete Order button | hover over | changes colour |
|			| click / tap | if form is valid  directs to green overlay with spinner then Checkout Success Page |  

All Tests Passed

<br>

*Unregistered / Not logged in Users*

This table tests two links that are available for unregistered guests instead of the Save Info box in the previous table.

| Feature	 | Action 	| Effect 		|
|--------------------|--------------------|-------------------|
| Create an account link | hover over | gets underline, address shows accounts/signup |
|			| click / tap | directs to Register Page |
| Login to save information link | hover over | gets underline, address shows accounts/login |
|			| click / tap | directs to Login Page |

All Tests Passed

<br>

**Checkout Success Page**

| Feature	 | Action 	| Effect 		|
|--------------------|--------------------|-------------------|
|Success Toast 	| View		| displays just below the navbar, includes order no. & email address|
|Order Confirmation Information | view | displays product names, quantity, totals, delivery info & email address | 
|View latest deals button | hover over | changes colour, address shows shop/?category=new,deals |
|		| click / tap | directs to Shop Page with deals and new categories |

All Tests Passed

<br>
</details>

<details>
<summary>Profile</summary>
<br>

| Feature	 | Action 	| Effect 		|
|--------------------|--------------------|-------------------|
| Form 		| Fill in | Form is filled in with user’s default delivery info |
| Update profile button | hover over | change colour |
|			| click / tap | Toast Success Profile updated successfully |
| Checkout Form | Choose products and navigate to Checkout | Checkout form is pre-populated with Profile form info |
| Order number | hover over | displays full order number, address shows profile/order_history/<order number> |
|	| click / tap | directs to order history  detail, toast alert notifies user that this is a past confirmation for order number … |
| Back to Profile button | hover over | changes colour, address shows profile |
|	| click / tap | directs to Profile Page |

All Tests Passed

<br>
</details>

<details>
<summary>Registration & Authentication</summary>
<br>

**Registration Page**

This page can be accessed by a non-logged in user via the My Account icon on the navbar, the Review section on Product Detail Pages, the Checkout form on the Checkout Page as well as the Login Page.

| Feature	 | Action 	| Effect 		|
|--------------------|--------------------|-------------------|
| login link	| hover over	| gets underline, address shows accounts/login |
|		|click / tap	| directs to the Login Page |
| Form validation | submit form with required fields left blank | tooltip directs user to fill in required field |
|Back to Login button | hover over | changes colour & background, address shows accounts/login |
|		|click/tap	| directs to the Login Page |
|Register button	|hover over	|changes colour	|
|			|click / tap	| directs to Confirm Email Page, alert toast shows user’s email address |
| Home button | hover over	|changes colour & background, address shows home |
|		| click / tap 	| directs to the Home Page |

All Tests Passed

<br>

**Confirm Email Page**

| Feature	 | Action 	| Effect 		|
|--------------------|--------------------|-------------------|
|Instructs the user to check their email to verify Email address | view | user clicks on the link in the email received |
|Confirm Email Page with email URL | view | instructs user to confirm email and username by clicking the Confirm button |
|Confirm button | hover over | changes colour |
|		| click / tap | directs to Login Page with success alert |

All Tests Passed

<br>

**Login Page**

The Login Page can be accessed by a registered user straight after registration or via the My Account icon in the Top Navigation bar.  A non-logged in user can also access the Login Page via the Review section on the Product detail pages and the Checkout form.

| Feature	 | Action 	| Effect 		|
|--------------------|--------------------|-------------------|
| registration link| hover over	| gets underline, address shows accounts/signup|
|		|click / tap	| directs to the Registration Page |
| Form validation | submit form with required fields left blank | tooltip directs user to fill in required field |
|		|submit form with wrong information | error message highlighted at the top of the form |
|Remember me checkbox | click / tap | ticks the checkbox |
|Login button	|hover over	|changes colour	|
|			|click / tap	| directs to Home Page, success toast alerts user that they are successfully logged in |
|Forgot Password? Link |hover over | gets underline, address shows accounts/password/reset|
|		| click / tap | directs to Password Reset Page |
| Home button | hover over	|changes colour & background, address shows home |
|		| click / tap 	| directs to the Home Page |

All Tests Passed

<br>

**Logout Page**

The Logout Page can be accessed via the My Account icon dropdown on the Top Navigation bar. 

| Feature	 | Action 	| Effect 		|
|--------------------|--------------------|-------------------|
| Cancel button	| hover over	| changes colour & background, address shows home |
|		| click / tap 	| directs to Home Page without logging out |
| Logout button	| hover over	| changes colour |
|		| click / tap	| directs to Home Page logging out user, success toast message |

All Tests Passed

<br>

**Reset Password**

The Reset password page can be accessed via the Forgot my password link on the Login Page.

| Feature	 | Action 	| Effect 		|
|--------------------|--------------------|-------------------|
| Email field	| submit form blank | tooltip directs user to fill in required field |
|Back to Login button | hover over   | changes colour & background, address shows accounts/login |
|		| click / tap |directs back to Login Page |
|Reset my Password button | hover over | changes colour |
|		|click / tap | directs to Password Reset Done Page |
|Password Reset Done Page | view | instructs user to click link in sent email |
|Confirm Email Page	|view	|instructs to confirm email and username |
|Confirm button	| hover over | changes colour |
|		|click / tap | directs to Change Password Page |
|Change Password form | submit form blank | tooltip directs user to fill in required field |
|change password button | hover over | changes colour |
|	| click / tap | directs to Change Password confirmation page, success toast password changed |

All Tests Passed

<br>
</details>

<details>
<summary>About Page</summary>

<br>

| Feature	 | Action 	| Effect 		|
|--------------------|--------------------|-------------------|
| Carousel	| hover over right arrow | brightens up | 	
|	| click / tap | goes to next slide |
|		| hover over left arrow | brightens up |	
|	| click / tap | goes to previous slide |
| Shop Now button | hover over | changes colour, address shows shop |
|		| click / tap | directs to Shop Page |
| Get in Touch button | hover over | changes colour, address shows contact |
|		| click / tap | directs to Contact Page |

All Tests Passed

<br>
</details>

<details>
<summary>Contact</summary>
<br>

| Feature	 | Action 	| Effect 		|
|--------------------|--------------------|-------------------|
| contact phone | hover over |changes colour, gets underline, address shows tel:<phonenumber> |
|		| click / tap | opens new tab / asks to open or switch app |
| contact email | hover over |changes colour, gets underline, address shows mailto:<emailaddress> |
|		| click / tap | opens outlook, mail, gmail or asks how to open or switch app |
| facebook link | hover over |changes colour, address shows <Facebook Business Page> |
|		| click / tap | opens new tab with Facebook Business page |
| Instagram link | hover over |changes colour, address shows <Instagram Page> |
|		| click / tap | opens new tab with Instagram page |
| Form Validation | submit form with required fields left blank | tooltips direct user to fill in required fields |
| Submit button | hover over | changes colour |
|		| click / tap | submits form & directs user to Thank you page, alert toast success |
| Home button on Thank you page | hover over | change colour & background, address shows home |
|		| click / tap | directs to Home Page |

All Tests Passed

<br>
</details>  

<details>
<summary>Error Pages</summary>
<br>

| Feature	 | Action 	| Effect 		|
|--------------------|--------------------|-------------------|
| To test Error 404 page | type `/test` at the end of url | directed to Error 404 page |
| Head Back Home button | hover over | changes colour, address shows home |
|       | click / tap | directs to Home Page |
| To test Error 403 page | As admin type `/reviews/edit_review/31` at the end of url | directed to Error 403 |
| Home button | hover over | changes colour, address shows home |
|       | click / tap | directs to Home Page |

All Tests Passed

<br>
</details>

[Back To Top](#table-of-contents)

_____

[Back to README.md](README.md)