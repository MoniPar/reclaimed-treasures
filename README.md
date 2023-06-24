# VERA'S RECLAIMED TREASURES

Welcome to Vera's Reclaimed Treasures, a full stack e-commerce website built using the Django framework, Bootstrap, HTML, CSS, Python & JavaScript.  It utilises Stripe as the payment processor and Amazon Web Services S3 Bucket for storing static and media files. The project has been deployed on Heroku and uses a postgreSQL database instance hosted on ElephantSQL.

This project was created for educational purposes only as my fifth and final project for a Diploma in Software Development with Code Institute.

Vera's Reclaimed Treasures is an online store where one can buy unique and sustainable products, hand-painted on upcycled materials in myriads of patterns and colourful designs.

[Link to the live website](https://veras-reclaimed-treasures.herokuapp.com/).

![VRT Am I Responsive](docs/responsive/am-i-responsive.png)
_____

## Table of Contents

- [VERA'S RECLAIMED TREASURES](#veras-reclaimed-treasures)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Business Model](#business-model)
    - [Marketing Strategy](#marketing-strategy)
      - [Social Media Marketing](#social-media-marketing)
      - [Email Marketing](#email-marketing)
    - [Search Engine Optimisation](#search-engine-optimisation)
    - [Website Main Goals](#website-main-goals)
  - [User Experience](#user-experience)
    - [User Stories](#user-stories)
  - [User Interface](#user-interface)
  - [Features](#features)
  - [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks \& Dependencies](#frameworks--dependencies)
    - [Tools](#tools)
  - [Deployment](#deployment)
  - [Validation \& Testing](#validation--testing)
  - [Bugs](#bugs)
  - [Credits](#credits)
    - [Media](#media)
    - [Code](#code)
    - [Acknowledgements](#acknowledgements)

[Back to Top](#table-of-contents)
_____

## Introduction

In my planning phase for this project, I wanted to create an ecommerce store for hand-made candles and soaps until I came across this lady's hand-painted collection of upcycled products at a fair in Malta. I was absolutely enthralled by what she had managed to create and decided to ask her for permission to use her creations for the basis of my ecommerce store.  That lady's name is Vera and her small business is called Vera's Magical Creations. At the moment Vera reaches potential customers at local markets, through her [facebook page]((https://www.facebook.com/profile.php?id=100070440427112)), or by word of mouth. All transactions are cash based and delivered in person which is time consuming.  
This project aims to create a more permanent online presence for Vera's business.  It gives her a way to organize her products, keep track of orders and automate sales without necessarily having to interact directly with all her customers.  An online store can help her reach a wider audience and maximize her business's potential.

This project aims to create a more permanent online presence for Vera's business.  It gives her a way to organize her products, keep track of orders and automate sales without necessarily having to interact directly with all her customers.  An online store can help her reach a wider audience and maximize her business's potential.

By following the principles of User Experience Design, Search Engine Optimization and utilizing the Django full-stack framework and Stripe API for secure payments, Vera's Reclaimed Treasures offers its customers an efficient and seamless way to view and purchase her products from anywhere in the world.

You can test the payment functionality by using the following details in the checkout page:
•	Card Number: 4242 4242 4242 4242
•	Expiry Date: Any future date formatted to MM/YY
•	CVN: Any 3 digit number
•	Postcode: Any 5 digits

[Back to Top](#table-of-contents)
_____

## Business Model

Vera's Reclaimed Treasures is a Business to Consumer(B2C) e-commerce site.  It gives the site owner an online presence where people can find her latest works and browse a wide range of finished pieces.  In addition to being a store, it is also a showcase of Vera's artistic abilities.  It carries a message of eco-consciousness and will appeal to people who are seeking eco-friendly, creative art pieces.
As a small, fledgling business, Vera’s Reclaimed Treasures, relies on engaging with the customers, open communication and relationship building.  The website offers ways to get in touch with Vera with feedback, queries and suggestions.  Customers can also post reviews on individual products which would help Vera improve the product selection while giving the customers a positive shopping experience.
The site's target audience falls into two overlapping tiers.  The first is people who are more broadly interested in art for use of décor or gifts.  The second are interested in reuse of discarded materials and items from an eco-friendly perspective.  These audiences are both very active demographics on Social Media, including Facebook, with many pages and discussion groups catering to them.

### Marketing Strategy

The marketing strategy at the outset will rely on a combination of organic content through social media,  and a newsletter subscription service.  Through creating attractive and engaging posts and emails, the aim will be to both foster and grow an audience for Vera's art while also directing traffic to the website.

#### Social Media Marketing

As mentioned earlier, Vera already has established a Business Facebook page and she has a few followers, who have purchased her products in the past and who are interested in the same causes as her.  If utilized properly, this offers potential for business growth. 
Pros of a Business Facebook Page:

- Organic approach allows for limited growth at no cost.
- Potential customers can be attracted to the posts based on interests relevant to the business, specifically Art and Environmentalism.
- Fosters a sense of community through engagement, building brand personality.
- Helps improve customer service and support.
- The existing Facebook page already has an established presence and a foundation of showcasing many of her art pieces.
- The Facebook Business page will include the link to the online ecommerce store, while users of the site are also linked back to her Facebook page so that they are kept in the loop about any new pieces, posts etc.

Opportunities for improvement:

- Increase the variety and consistency of content and posts.  This can include images and videos of Vera working at her craft.  
- Useful posts like tips and tricks and how to reuse recycled materials.
- Have Q & A sessions: getting people to ask questions which she will answer in a video.
- Posts about upcoming promotions, sales & deals.
- Posts about upcoming in person events where Vera will be displaying and selling some of her work and asking people to bring recycled materials.

For the purposes of this project, a mock-up Business Facebook page was created, similar to Vera's own.
  
![Mock-up Facebook Page](docs/vrt-facebookb.png)

Links to the Social links can be found in the Footer of the website as well as on the Contact Page.

![Image of Social links on Footer](docs/footer-social.png)

#### Email Marketing

A Newsletter subscription service will be set up on the Ecommerce website.  This will keep users up to date on Vera's news, special promotions and more while encouraging them to revisit the website.

Pros of posting a Newsletter:

- Easy and free to set up.
- Acts as a reminder to previous customers and others interested in Vera's products.
- Doesn't need to be as consistent as Facebook posts.
- Different approaches can be tested out, allowing for a more refined marketing strategy over time.
- A way to inform potential and returning customers about seasonal products, discount codes and bring in dates.
  
A newsletter sign-up form has been added to the Footer of the website.

![Image of MailChimp Newsletter sign-up form on footer](docs/newsletter-signupform.png)

### Search Engine Optimisation

Search Engine Optimisation(SEO) is a set of practices designed to improve the appearance and positioning of web pages in organic search results. To improve my website's visibility on search engines, I started by conducting some keyword research and defining short-tail keywords and long-tail keywords.  I used [Word Tracker]( https://www.wordtracker.com/) to narrow them down to the most relevant.  Once I had identified the keywords, I used them in the website's meta tags, title, headings, content and image alt descriptions.  These will help search engines understand the relationship between the different pages on the website. 
A [sitemap.xml]( https://www.xml-sitemaps.com/) and a robots.txt file were also added to my project.  The sitemap lists all the pages on the website, while the robots.txt file tells search engines which pages they should not crawl.
In the footer I added one link to the Eco Market Malta website. This website ranks higher on Google and is very relevant to Vera's Reclaimed Treasures as it promotes artists and eco-friendly products.
A privacy policy was also added to the website. While this is not a direct ranking factor for SEO, it is recommended to have Google and other search engines index it. In addition, it helps improve the website's credibility and trustworthiness and compliance with various laws and regulations related to data protection and privacy.

### Website Main Goals

For the site owner:

- To be able to showcase her collection to a wider audience.
- To provide her customers with up-to-date information about her business and herself.
- To have an inventory of her products displayed in the one place.
- To have a safe and efficient way to get payment for her products.
- To keep track of the orders made by her customers.
- To have a limit on Made to Order purchases.
- To be able to easily mark products as not available.
- To be able to add new products to the inventory through the admin panel.
- To be able to quickly respond to customer queries.
- To be able to improve her product selection through customers’ orders and feedback. 

For the user/customer:

- To give users a responsive and easy to navigate website with a clear purpose.
- To provide users with products that meet their expectations.
- To allow users to view details on products and add them to their shopping basket.
- To allow users to purchase Made to Order products if the stock runs out.
- To allow users to checkout quickly and safely.
- To give users the option to save their information for future visits.
- To give registered users the ability to view their previous orders.
- To give registered users the ability to submit product reviews.
- To give users ways to contact the business owner easily and efficiently.

[Back to Top](#table-of-contents)
_____

## User Experience

This section aims to determine what a user would expect from interacting with the website. Each User Story was recorded in [GitHub Issues](https://github.com/MoniPar/reclaimed-treasures/issues).  Scenarios of actions each type of user, including the business/site owner, wishes to take are listed below.  These were categorised into Epics listed in the Agile Methodology section, for the development of the project.  Two of the user stories listed below weren't completed on time and have been placed in the backlog for future iterations.

### User Stories

From User/Customer perspective:

- [#7](https://github.com/MoniPar/reclaimed-treasures/issues/7) As a user, I can register an account, so that I have access to other features of the website.
- [#8](https://github.com/MoniPar/reclaimed-treasures/issues/8) As a user, I can check my emails for a registration confirmation email, so that I can verify that my registration was successful.
- [#9](https://github.com/MoniPar/reclaimed-treasures/issues/9) As a User, I can login and logout from my account, so that I can access my account's information and keep my information secure.
- [#10](https://github.com/MoniPar/reclaimed-treasures/issues/10) As a User, I can reset my password, so that I can recover access to my account if I forget my password.
- [#11](https://github.com/MoniPar/reclaimed-treasures/issues/11) As a User, I can land on the homepage of the site, so that I can learn more about the business and the types of products they sell.
- [#12](https://github.com/MoniPar/reclaimed-treasures/issues/12) As a User, I can view the logo and the links in the navigation bar, so that I can easily navigate to other pages of the site.
- [#13](https://github.com/MoniPar/reclaimed-treasures/issues/13) As a User, I can access contact details, social and developer links across all pages, so that I can follow/contact the business owner and the website creator.
- [#15](https://github.com/MoniPar/reclaimed-treasures/issues/15) As a User, I can find out more about the artist/business owner, so that I can decide if I want to deal with them or not.
- [#17](https://github.com/MoniPar/reclaimed-treasures/issues/17) As a User, I can quickly write a message to the business owner using the contact form, so that I can query a commission or give feedback.
- [#18](https://github.com/MoniPar/reclaimed-treasures/issues/18) As a User, I can sign up to the newsletter, so that I keep updated on the latest products, offers and pop up stalls.
- [#19](https://github.com/MoniPar/reclaimed-treasures/issues/19) As a User, I can connect with my social media account, so that I can easily create an account.
- [#24](https://github.com/MoniPar/reclaimed-treasures/issues/24) As a Customer, I can view a list of products, so that I can select some to purchase.
- [#25](https://github.com/MoniPar/reclaimed-treasures/issues/25) As a Customer, I can view individual product details, so that I can identify more details about the product.
- [#26](https://github.com/MoniPar/reclaimed-treasures/issues/26) As a Customer, I can search for a specific product or view a category of products, so that I can quickly find products I'm interested in.
- [#27](https://github.com/MoniPar/reclaimed-treasures/issues/27) As a Customer, I can sort the list of available products, so that I can easily identify the best rated and best priced categorically sorted products.
- [#29](https://github.com/MoniPar/reclaimed-treasures/issues/29) As a customer, I can access my basket, so that I can review items before I purchase them.
- [#31](https://github.com/MoniPar/reclaimed-treasures/issues/31) As a customer, I can add items and identify their total cost in the basket, so that I know how much I'm spending.
- [#33](https://github.com/MoniPar/reclaimed-treasures/issues/33) As a Customer, I can update the quantity of each item in my basket, so that I can easily make changes to my purchase before checkout.
- [#34](https://github.com/MoniPar/reclaimed-treasures/issues/34) As a User, I can see real-time notifications as I interact with the website, so that I can have a better experience.
- [#36](https://github.com/MoniPar/reclaimed-treasures/issues/36) As a Customer, I can confirm my items and total cost in the checkout page, so that I can continue to enter the required information to complete my order.
- [#38](https://github.com/MoniPar/reclaimed-treasures/issues/38) As a Customer, I can easily enter my payment information, so that I can checkout quickly and with no hassles.
- [#39](https://github.com/MoniPar/reclaimed-treasures/issues/39) As a Customer, I can view an order confirmation after checkout, so that I can confirm that my order was successful.
- [#42](https://github.com/MoniPar/reclaimed-treasures/issues/42) As a Customer, I can have a personalised user profile, so that I can save my payment info and view my order history and confirmations.
- [#43](https://github.com/MoniPar/reclaimed-treasures/issues/43) As a Customer, I can edit personal information on my profile, so that I can use the correct details when processing future orders.
- [#44](https://github.com/MoniPar/reclaimed-treasures/issues/44) As a Customer, I can receive an email confirmation after checking out, so that I can keep the confirmation of the transaction for my records.
- [#46](https://github.com/MoniPar/reclaimed-treasures/issues/46) As a Customer, I can check products' ratings and reviews and submit my own, so that I can make up my mind if I want to purchase the product and provide feedback on products purchased.
- [#48](https://github.com/MoniPar/reclaimed-treasures/issues/48) As a Customer, I can edit and delete my reviews, so that I have the ability to correct any mistakes I make.
- [#47](https://github.com/MoniPar/reclaimed-treasures/issues/47) As a User, I can navigate to the About page, so that I can learn more about the shop owner.
- [#52](https://github.com/MoniPar/reclaimed-treasures/issues/52) As a User, I can easily navigate back to the top of the page with one click, so that I don't have to scroll back up through all the products in order to access the links at the top of the page.

The following User Stories were used to implement features which make the website run more smoothly and give the user a better experience using the website.  Some are made from the Business owner's or Developer's perspective.  Stories concerned with setting up and other developer tasks were left out from this list. Due to time lost with Code Anywhere technical issues, it was decided to leave the Product Management Interface and the Featured Products on Home page out. These were placed in the backlog for future iterations.
- []
-	#16 Featured Products
-	#21 Add product via UI
-	#22 Update product via UI
-	#23 Delete product via UI
-	#32 Quantity Selector
-	#40 Stripe webhooks
-	#41 Product Stock
-	#50 Social Media Marketing
-	#51 SEO Implementations
-	#55 Error Pages


[Back to Top](#table-of-contents)

_____

## User Interface

[Back to Top](#table-of-contents)

_____

## Features

[Back to Top](#table-of-contents)

_____

## Technologies Used

This project was developed using the following languages, frameworks, libraries and dependencies:

### Languages

- [HTML5](https://www.w3schools.com/html/)
- [CSS3](https://www.w3schools.com/css/css_intro.asp)
- [Python 3.8.12](https://www.python.org/downloads/release/python-3812/)
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

### Frameworks & Dependencies

- [Django 3.2.18](https://www.djangoproject.com/) - Free and open source Python Web Framework
- [Gunicorn 20.1.0](https://gunicorn.org/) - A Python WSGI HTTP server compatible with Django and used to run the project on Heroku
- [PostgreSQL 0.5.0](https://www.postgresql.org/) - A powerful, open-source object-relational database system
- [Pyscopg2 2.9.5](https://www.psycopg.org/docs/) - A PostgreSQL database adapter for Python
- [Stripe](https://stripe.com/) - Provides a secure and convenient way to handle online payments
- [Amazon Web Services S3 Bucket](https://aws.amazon.com/s3/) - A cloud storage service which provides object storage, built for storing and recovering any amount of information or data from anywhere over the internet through a web services interface
- [Heroku](https://www.heroku.com) - A cloud platform as a service
- [ElephantSQL](https://www.elephantsql.com/) - PostgreSQL database hosting service
- [SQLite3](https://docs.python.org/3/library/sqlite3.html) - The database provided by Django
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/) - Integrated set of Django applications addressing authentication and registration
- [Bootstrap 4.6.2](https://getbootstrap.com/docs/4.6/getting-started/introduction/) - A Framework for building responsive, mobile-fist sites
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - Provides a |crispy filter and {% crispy %} tag that helps control the rendering behavior of Django forms in a very elegant and DRY way
- [Pillow](https://pypi.org/project/Pillow/) - A Python Imaging Library adds image processing capabilities to your Python interpreter

### Tools

- [Cloud Anywhere](https://codeanywhere.com/solutions/collaborate) - Online Cloud Editor Used
- [GitHub](https://github.com/) - Cloud based git repository used
- [W3C Validator](https://validator.w3.org/) - A validator which checks the markup validity of Web documents in HTML, XHTML, SMIL, MathML, etc.
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) - A validator which checks the validity of CSS code
- [Code Institute's Python Linter](https://pep8ci.herokuapp.com/) - Highlights syntactical and stylistic problems in Python source code
- [JShint](https://jshint.com/) - A JavaScript code quality tool
- [Chrome DevTools and Lighthouse](https://developer.chrome.com/docs/devtools/) - Web Developer Tools
- [Box Shadow Generator](https://cssgenerator.org/box-shadow-css-generator.html) - A box shadow generating tool
- [Am I responsive](https://ui.dev/amiresponsive) - For responsive visuals of the website
- [CanIUse](https://caniuse.com/) - Browser support tables for modern web technologies
- [TinyPNG](https://tinypng.com/) - Compresses images to reduce the file size
- [TinyURL](https://tinyurl.com/app/) - Shortens links
- [Canva](https://www.canva.com/colors/color-palette-generator/) - Colour Palette Generator
- [Google Fonts](https://fonts.google.com/) - Fonts
- [Font Awesome](https://fontawesome.com/) - Icons
- [Balsamiq](https://balsamiq.com/wireframes/) - Low Fidelity Wireframes
- [LucidChart](https://www.lucidchart.com/) - Entity Relationship Diagram
- [BrowserStack](https://www.browserstack.com/) - App and Browser Testing

[Back to Top](#table-of-contents)
_____

## Deployment

All deployment information can be found in [DEPLOYMENT.md](DEPLOYMENT.md)

[Back to Top](#table-of-contents)

_____

## Validation & Testing

All validation & testing information can be found in [TESTING.md](TESTING.md).

[Back to Top](#table-of-contents)
_____

## Bugs

<details>
<summary>Bugs encountered during Development</summary>
<br>

**Copying django-allauth templates**

Problem: Using the `cp -r ../.pip-modules/lib/python3.8/site-packages/allauth/templates/* ./templates/allauth/` command to make a copy of the built-in allauth template directories was giving me `cp: cannot stat '../.pip-modules/lib/python3.8/site-packages/allauth/templates/*': No such file or directory`

Solution: Found on a CI slack channel.  
![Copy django-allauth templates solution](docs/django-allauth-tempsol.png)

**Sorting Products**

Problem: While testing the sort selector box functionality, it was noticed that products sorted by rating descending was displaying a new test product with 'No Rating' first.
Expected behaviour: This product should be displayed last along with the other products with no rating.

Solution: This new test product was logged into the database without a value in the Rating field while the other 'No Rating' products were saved with a value of '0.0'. The arguments for the rating field in the Product model are set to the following:
`rating = models.DecimalField(max_digits=6, decimal_places=1, null=True, blank=True)`.  Since this new product test was stored with a NULL value it was not being counted as '0'. In order to avoid this from occurring again, the model field needs to be changed to either making the field required i.e. `blank=False` or set to `default=0.0`.

Note: One week before project submission, I realised that I completely ignored the sorting factor when it comes to rating after I added the reviews app.  I failed to connect the products.rating field with the reviews.rating field and I had to remove the Sort by Rating functionality.  In future versions I will need to make amends for this and make sure that the two are related together.

**Database product deletion while in basket**

Problem: In development, everytime I tried to run the server I was getting Error 404 Page not found on all the pages of the website including the admin.  Retracing my steps I figured that there might have been a test product still in the basket session when I deleted it from the database.  

Solution: Since I had no access to the Admin, I could not log out the user in order to delete the basket session.  Eventually I did it manually in Django shell by grabbing the user and deleting the session objects.

```python
    from django.contrib.auth.models import User
    from django.contrib.sessions.models import Session

    user = User.objects.get(username='Admin')
    session = Session.objects.all()

    user
    session.delete()
```

When I tried to run the page again, I was able to access all the pages and the basket was empty.

**Integrity Error after checkout**

Problem: An IntegrityError was being thrown after checking out a Made to Order product.  `IntegrityError: new row for relation "products_product" violates check constraint "products_product_stock_check"
DETAIL:  Failing row contains (23, vrtgw0006, Blue Vein Decanter, Patterns, Upcycled clear decanter, hand-painted with a blue and white veni..., Dimensions - 240 x 141mm; Capacity - 700ml; Total weight - 0.75k..., 14.00, 4.2, f, -3, glassware_blue-vein-decanter.jpg, 2).` The error shows that the stock was "-3" on this particular product.  This is because there were 3 ordered, and as the stock was already at 0, it was deducted to a negative value. The order still went through and the payment was successful on Stripe.  

Expected behaviour: The customer is able to order up to 3 Made to Order products and directed to the Checkout Success Page.  

Solution: The product stock deduction code in checkout/views.py was placed inside a while loop in order to only count down stock when there is stock available.

```python
    # Iterates through the items in basket and creates each line item
    for item_id, quantity in basket.items():
        try:
            product = Product.objects.get(id=item_id)
            # Decrements stock depending on quantity purchased
            while product.stock > 0:
                product.stock -= quantity
                product.save()
```

**Product Stock Overflow Issue [Bug: Product stock #45](https://github.com/users/MoniPar/projects/8/views/1?pane=issue&itemId=29840462)**

Customer can checkout an order on made to order products, however they can't checkout if they are trying to order more than what is currently in stock, even if they are within the 3 max limit on made to order.

Expected behaviour:
Customer will get an alert to make them aware that their order might take 3 - 5 extra days if their quantity is greater than the product stock but within the 3 max limit on made to order.

Customer will get a warning if their quantity exceeds the 3 max limit on made to order when the product is still in stock. E.g. if the customer is trying to order 5 items on a product that has a current stock of 1. They are directed to the basket where they can fix their order quantity in order not to exceed the 3 max limit on made to order. In this case when the customer changes the quantity to 4, the order should go through as there's already 1 in stock and they are allowed to order 3 items on made to order products.

Solution:
Bug solved by adding another if statement in the quantity > product stock, checking whether quantity - product stock gives an overflow greater than 3. If it does, the customer is redirected to the shopping basket and given a warning directing them to change the quantity on the specific product.

If the quantity - product stock has an overflow within or equal to the 3 max limit, then the order goes through and are just alerted to expect a slight delay.

**Product Stock: Database altered before Order Success**

While testing the previous issue, it was found that while iterating through the items in the basket, the product stock was being decremented from the database even when the customer was being redirected to the shopping basket and the order was incomplete.

Expected behaviour:
The product stock in the database should only be altered after the customer has actually purchased the products.

Solution:
It was decided to iterate through the products in the basket while checking the product stock against the quantity ordered. But instead of changing the information in the basket, the changes were saved in a list which was then iterated through (instead of the basket) when creating the line items.

**Duplicate orders in Database**

While testing, it was noticed that some orders where being recorded twice in the database as well as on the Order History in the User's Profile page.  This wasn't the case with Stripe as only one payment intent was being created for each order.  Only one order confirmation email was being sent to the customer too.  

Expected behaviour:
Only one order should be registered in the database and on the user's profile for each order made.

Solution:
With further testing, it was noticed that certain orders weren't being duplicated.  When investigating further, the duplicate orders issue was narrowed down to the user not filling in the 'Eircode' field in the checkout form.  This is not a required field and I had previously changed its label to say 'Postcode' rather than the Irish term 'Eircode' by using the 'label' attribute in the OrderForm(ModelForm).  This change must have created inconsistent personal details on orders.  Looking back in the webhook handler for handling payment intent succeeded, I was trying to get the `default_postal_code` from the profile rather than the `default_eircode`.  This was amended back to `default_eircode`, however this did not solve the issue.  What did eventually sort the issue was rather than using the 'label' attribute in the OrderForm(ModelForm), a labels dictionary was added to the `__init__` method. After testing again, whether filling in the post code field or not, orders were not being duplicated.

[Back to Top](#table-of-contents)
_____

## Credits

### Media

Vera Vinita Schembri for allowing me to use images from her collection for 
the purpose of this ecommerce store

Austen Donohoe for the designing the Vera's Reclaimed Treasures Logo and the 
hero images for the Home and Contact Pages.

### Code

The following walkthroughs helped me get my project in shape. I have adapted the code in these walkthroughs for the needs of my project.

* Code Institute's "Boutique Ado", found in the CI's LMS for the Diploma in Software Development.  I followed this walkthrough as the basis for my own store, then added functionality to better serve the purpose of my project.

* [Django Tutorial: A simple contact form](https://www.youtube.com/watch?v=1ihn3iRXtsY)

[BobbyHadz.com - TypeError - Sequence item 0: expected str instance, NoneType found](https://bobbyhadz.com/blog/python-typeerror-sequence-item-0-expected-str-instance-list-found#sequence-item-0-expected-str-instance-nonetype-found)

[How to reduce stock quantity when an order is made](https://stackoverflow.com/questions/65216808/django-how-to-reduce-stock-quantity-when-an-order-is-made)

[How to force a user to logout](https://stackoverflow.com/questions/953879/how-to-force-a-user-logout-in-django)

[Back to Top](#table-of-contents)
_____

### Acknowledgements

[Back to Top](#table-of-contents)

____