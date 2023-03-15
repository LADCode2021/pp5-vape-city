# PP5 - Vape City

Vape City is an e-commerce site that allows users to order vaping products, create accounts to view order history, sign-up to newsletters and contact the store. As an avid vaper I struggle to find vaping e-commerce platforms with good UX that are reliable. This is a problem in the vaping industry as retail vaping products are generally supplied by very small businesses that cannot afford good developers. They also cannot use popular self-build platforms such as Shopify as most ban the setup of vape shops due to the lack of regulation in the vaping space. My goal with this site is to use the skills and knowledge I have learning throughout this course to solve this real-world problem with an e-commerce site that could become a trusted brand with good UX and a reliable store.

[The live project can be viewed here.](https://pp5-vape-city.herokuapp.com/)

![](docs/images/ismysiteresponsive-screenshot.png)

# Planning

I started this project by setting up a project in GitHub and using agile methodologies to define user stories that would guide me in the development of site. This allowed me to develop the site in small sprints by focusing on one user story at a time. The goal with using this agile methodology was to prevent me becoming overwhelmed with several developments at once. In the past I have tended to flip between front-end UX and back-end application and get lost or overwhelmed trying to code too many things at once.

Please see my initial GitHub issues:

![](docs/images/to-do-list-screenshot.png)

I finished the majority of my initial issues and also added a couple more. I didn't end up creating functionality for subscribing for regular products or deleting accounts. These are things I would consider for future iterations but they were not in scope for the initial sprints on this project. Please see my finished board:

![](docs/images/to-do-list-finished.png)

# Features

## Existing Features

### Homepage with banner

home-page-screenshot.png

### Navigation menu with dropdowns

nav-with-drop-down.png

### Shop by product category on homepage

shop-by-product-hompage.png

### Shop all products with sort functionality

shop-by-sort.png

### Shop by filter and sort

shop-by-filter-and-sort.png

### Individual product detail page without variations

individual-product-detail-page.png

### Individual product detail page with variations

product-detail-page-variations.png

### Basket with items showing variation or no variation








## Future Features

* A blog page
* Subscription to certain products
* Size and colour variations for certain product types, i.e. Mods and Tanks

# Business Model

The business model I have chosen for this site is B2C (Business to Customer). 

The marketing approaches I have implemented so far are: 

* Search Engine Optimisation (SEO) with rel tags, meta description, robots.txt file and sitemap.xml.
* Content marketing linked in with SEO by ensuring content is specific and follows keyword research I have done around the most popular vape searches, i.e. disposable vape
* Social Media Marketing with a Facebook page setup for the store (https://www.facebook.com/people/Vape-City/100090646303099/?mibextid=LQQJ4d)
* Email Marketing with a newsletter sign-up in the footer of the site

# Custom Models

# Testing

## Manual Testing

### Test Navigation

I tested all navigation links in both the navbar and inline links and everything went to where it was supposed to.

### Contact Form Tests

I tested:

* Form submit with empty fields and the form would not submit and gave feedback to the user

![](docs/images/empty-field-test.png)

* Form submit with invalid email and it would not submit and gave user feedback to user

![](docs/images/invalid-email-test.png)

* Form submit with invalid phone number and it gave the user feedback

![](docs/images/contact-form-phone-error.png)

### Registration Form Tests

* Test Registration form submits

* Test empty values in all fields

I tested all fields individually as empty fields and all fields raised an error asking the user to fill in the field.

* Test valid email address

I tested whether the field would allow me to enter an incorrect email. It didn't let me and asked me please enter '@' in an email address.

* Test existing account

I tried to create an account with existing email address and it raised an error telling me a user with that name already exists.

### Login Form Tests

* Test empty values in all fields

* Test valid email address

* Test incorrect password


## CRUD Operation Tests

* Test add new product to DB from frontend

This did work initially but I later found an error when adding a category. Please see below for error found.

I was also able to confirm that adding invalid data to the fields would prevent the form submitting. I tested every field and they all gave feedback to the user. Here is an example:

![](docs/images/add-product-form-error-example.png)


* Test add new category to DB from frontend

While adding a new category to the DB from the front end I discovered that it would raise two messages. One an error saying a product couldn't be added and one saying a category had been added.

![](docs/images/add-category-error.png)

I checked the views.py and the way I had written the code was causing the error. I had both forms in the same if request.POST. In doing so it would still try to validate the product form when I was actually submitting a category. To correct the error I split the two forms into different if request.POST conditions and checked whether a unique field to that model was being submitted. This corrected the error:

![](docs/images/add-product-error-fix.png)

* Test add flavour and strength variations to DB

I was successfully able to add new flavours ands strengths to products. Please see an example with user feedback message showing it worked (form to submit shown above in existing features):

![](docs/images/add-variation-success.png)

* Test edit product in DB

![](docs/images/edit-product-in-db.png)

![](docs/images/edit-product-success.png)

* Test add product without variation to basket

![](docs/images/add-product-wihout-variations-success.png)

* Test add product with variation to basket

![](docs/images/add-product-with-variation-to-basket.png)

* Test update quantity of item in basket

The item updates successfully when typing new quantities in and when using the increment and decrement buttons. It will also delete the item if the user puts 0 in the box. I have not included a screenshot for every variation of update. Please see updating quantity to 2 as an example below: 

![](docs/images/update-quantity-in-basket.png)

* Test remove item from basket

In initial testing this worked fine. As in I could remove items with and without variations. But my original testing was in different states of basket. When I did final testing as in tested every possible remove scenario I found that items without variations would not remove and raised a server 500 error. This was related to an if condition I had created to create variables of variations to include in remove success messages. To correct the issue I had to remove this functionality.

![](docs/images/remove-non-variation-item-error.png)

Once removed I was able to remove items with variations:

![](docs/images/remove-item-with-variation-from-basket-success.png)

And items without variations:

![](docs/images/remove-non-variation-item-success.png)

* Test checkout success/webhook handler

When testing checkout the order was being created and giving the checkout success page when adding a product without variations. However, it was being created twice in the database. I checked stripe and the order was only there once. This was a good test in that i know the order was being created by the webhook handler but it must have meant there was an error in my code somewhere.

I tested it in dev and only one order was created but it wasn't doing the order total correctly in the database and the webhook handler was failing in stripe. I discovered there was an issue with the delivery cost sum as it was still set to work out my percentage of order in models.py which I had already removed. I also rolled back to before I had refactored it for PEP8 style errors in case I had introduced an error somewhere.

Once I had pushed to GitHub again I still got a checkout success page but the webhook failed on stripe this time when testing a product with variations. I had forgotten to update the webhook handler with variables that created variations from the item string. I copied the code over from views and pushed to GitHub again.

The order successfully submits again but once again two orders are created in the database. The webhook is also successful again in Stripe and tells me the order has been created from webhook.

Something is going wrong on the order.save in the checkout views that is allowing it to save the order but then the webhook handler doesn't recognise an order exists.


## Remaining Bugs

* There is an error on index.html. I added in last minute a new div to link through to show all products in each category. It broke the forloop counter. On large-xl screens the products are supposed to have 4 columns on each row. After adding an additional div after the forloop counter it pushes one of the products onto the next line. I have a theory on how to fix it but I have run out of time to implement in time for submission. 

* All of the links through to products in each category align with the top of the card when pushed to a new line. If I ever wanted to have more than 4 products to display for each category on the homepage I would need to fix this as it is not good UX. The bug also exists on mobile devices.

* The scroll bar in the basket popup when adding multiple products is not working. It displays a long list which is not great UX. I have run out of time to fix thi in time for submission.

* I discovered in testing the issue with adding categories (described above). The original views.py if statement needs to be corrected in the view for adding variations also. I have run out of time to implement and test this fix. It's not super urgent as the variations will still add. It just throws an error message unnecessarily.

* This is not necessarily a bug but it affects user feedback when removing items with variations from the basket. I had an if condition in the remove_from_basket view that created flavour and strength variables to include in success messages if the user removed an item with a strength/flavour from the basket. However, as mentioned in testing when removing items without variations from the basket I received a internal 500 error. I have a theory on how to fix this so I can include variations in remove messages but I have run out of time to implement and test.

* In the deployed app there is a bug which allows an order to be created twice in the database. It also won't calculate the order total. It works in dev but not on the deployed app. I have run out of time to fix this issue.

## Validator Testing

I validated views.py, models.py and forms.py in Code Institute PEP8 Linter (https://pep8ci.herokuapp.com/) and no errors were returned.

# Deployment

I followed the steps detailed in the Boutique Ado deployment instructions. I have not included these below as it is now a written guide on the LMS.


# Technologies Used

I used the following technologies:

* Hardware: MacBook Pro
* GitHub
* GitPod
* Google Chrome, Firefox and Safari web browsers
* Django
* Heroku
* Amazon AWS
* ElephantSQL
* Stripe

# Packages/Libraries used

* asgiref==3.5.2
* boto3==1.26.29
* botocore==1.29.29
* crispy-bootstrap4==2022.1
* dj-database-url==0.5.0
* Django==3.2
* django-allauth==0.41.0
* django-countries==7.2.1
* django-crispy-forms==2.0
* django-storages==1.13.1
* gunicorn==20.1.0
* jmespath==1.0.1
* oauthlib==3.2.2
* Pillow==9.3.0
* psycopg2==2.9.5
* python3-openid==3.2.0
* pytz==2022.6
* requests-oauthlib==1.3.1
* s3transfer==0.6.0
* sqlparse==0.4.3
* stripe==5.2.0

# Credits

* Site adapted and built on Boutique Ado walkthrough project

* Image credits in image alt text

* Code Institute lesson content adapted in some areas.









