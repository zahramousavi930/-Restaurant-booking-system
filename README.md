# -Restaurant-booking-system

main frameworks and languages: 
python, 
django,
postger database 
JavaScript, 
html,
css ,
sass, 
bootstrap , 
bootstrap icon
,fontawesome


Restaurant site is use for reserve and buy online food for all user you can book a table any time and any day that you want.



![23](https://github.com/zahramousavi930/ckz8748-django-booking-system-b2059e81383e.herokuapp.com/)




Demo like:  https://django-resturant-dc830834c6f2.herokuapp.com/

Features

    User authentication and account management (registration, login, password reset)
    Add Foods to the shopping cart
    Manage the shopping cart (update quantities, remove items)
    Checkout and place orders
    Order history for user
    Admin dashboard for managing food, reserv and users



Forms:

users can leave comment, signup , login, reset password, reservation with forms and they can access to their reserve info in shopping cart or panel.

User Registration and Authentication: Users can register, log in, and log out without any issues.


Testing: Detailed testing write-ups are provided in the GitHub repository, documenting the test scenarios, methodologies, and results.


commens and food:

after create food admin must active it to show in Maine page.
user after leav comment admin could ready it and then show it to main page.



Custom 404 Error:

A custom 404 error page is implemented to provide a user-friendly experience when a page is not found.



Custom of reaturant Models :
1- Users can create and manage their reservation, adding , removing or edit their reservation.

2-Users can leave comment and like food of menu.

3- Users can track the status of their orders and reservation.



other feature:

Social media marketing through platforms like Facebook and Instagram to reach and engage with the target audience.

Influencer collaborations and partnerships to increase brand visibility and generate sales.

The HTML templates include descriptive meta tags that enhance search engine visibility and provide meaningful information about the website's pages.

Search engine optimization (SEO) techniques to improve organic visibility and attract potential customers.



Deployment
I deployed this website by using GitPod, heroku and following the below steps:

Gitpod and heroku pages deployment

Log in to Github 
login  to heroku
use gitpod to deploy and commit change things to GitHub
add Procfile  and gunicorn for run code in heroku





test all part of views and form by inner framework of django test
user must login first then use all feature of a site


![3](https://github.com/zahramousavi930/-Restaurant-booking-system/assets/102755356/ee3c095d-fc78-49fa-ad1b-995c85c0e278)



# Restaurant Booking System

Restaurant site is use for reserve and buy online food for all user you can book a table any time and any day that you want.

The site is fully responsive and was built using the Django framework in Python.

The live site has been deployed [here](https://ckz8748-django-booking-system-b2059e81383e.herokuapp.com/).

![23](https://github.com/zahramousavi930/ckz8748-django-booking-system-b2059e81383e.herokuapp.com/)

To test this functionality, please use the card details that can be [found here](https://stripe.com/docs/payments/accept-card-payments?platform=web&ui=elements#web-test-integration).

![Am I Responsive Image](readme_content/responsive.png)

## Contents

- [User Experience (UX)](#user-experience-ux)

  - [User Stories](#user-stories)

    - [Navigation](#navigation)
    - [Accounts](#accounts)
    - [Admin](#admin)
    - [Purchasing](#purchasing)
    - [Interaction](#interaction)

  - [Design](#design)

    - [Colours](#colour)
    - [Fonts](#fonts)
    - [Images](#images)
    - [Wireframes](#wireframes)
    - [Database Schema](#database-schema)

- [Features](#features)

  - [Nav Bar](#nav-bar)
  - [Home page](#home-page)
  - [Accounts](#accounts)
  - [Profile](#profile)
  - [All Products](#all-products)
  - [Product Details](#product-details)
  - [Product Management](#product-management)
  - [Cart](#cart)
  - [Checkout](#checkout)
  - [Celebration Cakes](#celebration-cakes)
  - [About Us](#about-us)
  - [Contact](#contact-us)
  - [Toasts](#toasts)
  - [Footer](#footer)
  - [Other](#other)

- [Testing](#testing)
- [Deployment](#deployment)

  - [Github](#github)
  - [Django](#django)
  - [Heroku](#heroku)
  - [AWS](#clone)
  - [Stripe](#Stripe)

- [Credits](#credits)

  - [Media](#media)
  - [Languages](#languages)
  - [Libraries, Frameworks & Tools](#libraries-frameworks-and-tools)

## User Experience (UX)

### User Stories

- #### Navigation

  - As a user, I want to navigate round the site easily to locate the products I want.
  - As a user, I want to view a list of all available products.
  - As a user, I want to be able to view more details on a product, such as price, ingredients and reviews.
  - As a user, I want to be able to refine my search with categories.
  - As a user, I want to be able to sort products by price, review or name.
  - As a user, I want to be able to easily contact the site owner if needed.
  - As a user, I want to be able to see all ingredients contained within the product, including any allergens.

- #### Accounts

  - As a user, I want the option to register for an account, allowing me to save my details and see previous orders.
  - As a user, I want to receive confirmation emails to confirm my registration.
  - As a user, I want the ability to be able to log in and out, and be able to easily work out my current login status.
  - As a user, I want to be able to recover my account information in the event that I forget it.

- #### Admin

  - As an admin, I want to be able to add products easily in a format consistent with the rest of the site.
  - As an admin, I want to be able to edit products easily to ensure the customer is being shown the most up to date information
  - As an admin, I want to be able to delete discontinued products, or mark seasonal products out of stock when not available.
  - As an admin, I want to be able to easily manage the images in the gallery, and update the site policies.
  - As an admin, I want to be able to add and update the ingredients for products, and mark any allergens appropriately.

- #### Purchasing

  - As a user, I want to be able to add items to my cart, allowing me to store things until I'm ready to complete my purchase.
  - As a user, I want to be able to view my cart so I can see the current running total of my potential purchases.
  - As a user, I want the ability to update the quantity of the items in my cart easily.
  - As a user, I want an easily viewable total to allow me to monitor my overall spend.
  - As a user, I want to be able to complete the purchasing journey, without the need to register if I do not wish to.
  - As a user, I want to receive confirmation of my order so I know my order was placed successfully.
  - As a user, I want to be able to view my order history so I can review past purchases.

- #### Interaction

  - As a user, I want to be able to leave a review of products to share my experience with other customers
  - As a user, I want to be able to easily connect to the business' social media pages to keep up to date.
  - As a user, I want to be able to easily contact the site owner if needed.

#

[Back to top ⇧](#nibble-kitchen)

#

## Design

- ### Colours

  The decision was made to keep the colours as simple as possible for the website, with the main content being either black text on a white background, or vice versa.

  This is due to cakes and confectionary being inherently colourful. By reducing the colour palette to the most basic possible helps draw attention to the products displayed, and the colours within.

  ![Colours Image](readme_content/colours.png)

- ### Fonts

  The [Roboto](https://fonts.google.com/specimen/Roboto) font from Google Fonts is used throughout the site on all content.

  This font was chosen due to it's readability, popularity and familiarity, with it being the chosen font for a number of products produced by Google.

- ### Images

  All product images have been taken from the current website for [Nibble Kitchen](https://nibblekitchen.co.uk/), with permission from the owner.

  Other images used throughout the site were chosen from the website [Unsplash](https://unsplash.com/) and were chosen to fit the overall theme of the website.

  Image credits can be found in the [Media](#media) section of this Readme.

- ### Wireframes

- ### Database Schema

  The database schema for the project was:

  ![Database Schema](readme_content/schema.png)

  The full image can be viewed [here](readme_content/schema.png)

#

[Back to top ⇧](#nibble-kitchen)

#

## Features

- ### Nav Bar

  - Links
    ![Navbar Image](readme_content/navbar.png)

    - To allow easy navigation around the site, the navbar is fixed to the top of each page and contains links to all areas of the website, with the exception of the information in the [footer](#footer).
    - The navbar collapses to a hamburger menu once the window width drops below 992px to ensure all information is displayed comfortably to the user.
    - All links, with the exception of About Us and Contact Us, make use of Bootstrap's dropdown plugin. Upon a link being clicked, more options are shown to the user.-

  - Search Bar

    ![Search Bar Image](readme_content/search.png)

    - The search bar is located in the middle of the navbar, above the links and can be used to search the site for products.
    - The search term entered will be used to search the database for any products with matching information in either the product title, product description or product ingredients.
    - On screens with a width below 992px, the search bar is hidden and can be displayed by clicking on the 'Search' button that is present in the navbar.
    - JQuery is used to check the content of the search bar. If no search term has been entered, a warning is shown to the user for 5 seconds.

  - Account

    ![Account Image](readme_content/account.png)

    - A user icon is located in the top right of the page, allowing the user access to manage their account and personal information.
    - Clicking on the icon displays a dropdown menu using Bootstrap's dropdown plugin with a number of options
      - Login & Register are displayed if the user is not logged in.
      - My Profile & Logout are displayed if the user is logged in.
      - Admin Dashboard & Add Product are displayed if the user is a superuser.

  - Cart

    ![Cart Image](readme_content/cart.png)

    - A cart icon is also located in the top right corner of the page displaying the value of the current contents of the cart, and the number of items that are present in the cart.
    - Clicking the cart icon will take the user to the [cart](#cart) page where they can complete their shopping journey.

  - Banner

    ![Banner Image](readme_content/banner.png)

    - A banner is displayed below the navbar advising the user on the current offer for free delivery.
    - If the user does not have any products in their cart, a message is shown stating 'Free delivery on orders over £65'
    - If the user does have items in their cart, the message is updated to notify the customer how much more they need to speed to ready the £65 free delivery limit.

#

[Back to top ⇧](#nibble-kitchen)

#

- ### Home Page

  ![Home Image](readme_content/home.png)

  - The home page has been designed with a minimalist appearance, containing only a hero image, a message, and a button directing the customer to view products on the site.
  - The hero image can be seen in the [Media](#media) section of this readme.
  - The message informs the user of the purpose of the site in a succinct manner, with the action of the button being made obvious by the label contained within.

- ### Accounts

  - Registration Page
    - The registration page is used by users to create a new account for the site.
    - Form validation is used to ensure all fields on the form are completed. If this validation fails, a message is shown to the user and the form is not submitted.
    - Once form validation has passed, the form will be submitted and the user will receive a confirmation email to verify their account.
    #
    ![Registration Image](readme_content/register.png)
    #
  - Login Page
    - The login page is used for users with an existing account to log in to the site.
    - If the user has not verified their account by clicking on the link in the email they are sent, they will be unable to log in.
    - A 'Forgot Password' link is present for users to recover their account in the event that they cannot remember the required information to log in.
    #
    ![Login Image](readme_content/login.png)
    #
  - Logout page
    - The logout page is used by users to log out if they are signed in, removing their session information.
    - The user will be taken to a confirmation page upon clicking the 'Logout' link, to ensure this is the action they wish to take.
    #
    ![Logout Image](readme_content/logout.png)
    #

#

[Back to top ⇧](#nibble-kitchen)

#

- ### Profile

  - Heading

    - The heading of the profile page will display the user's username. In the event that this information cannot be obtained, 'My Profile' will be displayed instead.

      ![Profile Heading Image](readme_content/profile.png)

  - Delivery Information
  - The delivery information section shows any stored address information for the user.
  - The information can be updated on this page, and these change will be used to autocomplete the delivery address when placing an order.
  - The information displayed in this section can also be updated when the user completes the shop journey if they check the 'Save this delivery information to my profile' box.
    ![Delivery Information Image](readme_content/delivery.png)

  - Order History
    - The order history section displays all previous orders placed by the logged-in user.
    - This section will display the order number, date of order, items ordered, quanitity ordered and the overall total.
    - Clicking on the hyperlink tag surrounding each order number will direct the user to a more detailed summary of the order.
      ![Order History Image](readme_content/order_history.png)

#

[Back to top ⇧](#nibble-kitchen)

#

- ### All Products

  - Products Page

    - The products page displays a list of available products in a selected category, search term or, if the correct option is selected, all products are shown.
    - Each product card show an image of the product, the price (or price range), the category in which the product resides and the rating. If no ratings are available 'No Rating' is shown in its place.
    - If a product is on sale, the original price will be shown with strikeout styling applied, the sale price will be shown and a small badge will be placed next to the prices to show the percentage of discount being given.
      ![Products Card Image](readme_content/products.png)

  - Sorting

    - The sort-by box is located in the top right of the products section on screen sizes above 768px width, and in the centre below 768px width.
    - Clicking on the box displays the sorting options available to the user.
      ![Sort By Box Image](readme_content/sorting.png)
    - Within `views.py`, an if statement is present to check if the sortkey contains `desc`. If `desc` is present, `nulls_last=True` is appended to the end of the search term to ensure products with ratings are shown before products with no ratings.

#

[Back to top ⇧](#nibble-kitchen)

#

- ### Product Details

  ![Products Info Image](readme_content/product_info.png)

  - Product Info

    - The product info section of the product details page shows all the important information related to each product.
    - The left part of the product info section is taken up by an image of the product. The image can be enlarged upon clicking to enable a better view. This is done within the page using bootstrap, rather than opening a new tab.
    - The name of the product is displayed at the top of this section and is also added to the title of the page.
    - Below this, the price of the product is shown.
      - If the product is on sale, the original price will be shown with strikeout styling applied, the sale price will be shown and a small badge will be placed next to the prices to show the percentage of discount being given.
      - If the product has sizes, the prices are updated appropriately using JQuery. The values for these prices are obtained from a seperate file which, in turn, queries the database for the correct prices. This ensures the same code can be reused throughout the site.
    - The category for the current product is shown next, with an underline style applied to indicate a hyperlink. Clicking on this link will direct the user to the products page for that category.
    - The Rating for the product is shown next. The rating is calculated by dividing the sum of all reviews by the number of reviews. If there are no reviews for a product, 'No Rating' is shown instead.
    - `Edit` and `Delete` buttons are shown next to the rating if the current user has superuser privileges, allowing the requested action to take place.
    - If the product has different sizes available, the `Size` field will be shown allowing the user to pick between Small, Medium, or Large. This is mainly applicable for the cake jars.
    - The `Quantity` field is shown for all products and allows the user to increment or decrement the value either with the provided buttons, or by typing directly into the box. Javascript is used to check if the value is above 99, which will return the max value to 99 if true.
    - A pair of buttons with the text of `< Keep Shopping` and `Add to Cart` are displayed as the element of the product info section, respectively. The `< Keep Shopping` button will return the user to the main products page, with the `Add To Cart` button adding the item into the user's cart before returning them to the same page.

    #

    ![Ingredients Image](readme_content/ingredients.png)

  - Ingredients

    - The Ingredients section is the first tab within the bottom section of the Product Details page. It begins with information advising that all allergens are marked in bold.
    - The ingredients are stored in the database for each product and are retrieved to be displayed on the page. This was done to ensure that any updates to allergens in the future take effect site wide and to ensure customers with allergens have the best information possible.
    - Below the ingredients section is a disclaimer, providing a list of allergens used and warning that items are baked in a single kitchen and that cross contamination between allergens is possible.

    #

    ![Customer Reviews Image](readme_content/customer_reviews.png)

  - Customer Reviews

    - The Customer Reviews section displays any reviews that have been left by customers previously. If no reviews have been left, the user is instead shown a message stating: `There aren't any reviews for this product. Be the first to leave a review!`, with a link being provided to the `Leave A Review` tab.
    - If reviews are present in the database, the rating is obtained and the relevant rating image is displayed alongside the title of the review. Below this is the username and date on which the comment was made, followed by the comment itself.
    - Superusers and the original user who posted the comment have the ability to delete the comment if required. No user has the ability to edit user reviews to ensure the reviews section is perceived as trustworthy.

    #

    ![Leave A Review Image](readme_content/review.png)

  - Leave A Review

    - The final section on the Product Details is for the user to leave a rating and review of the product.
    - The first part of the form allows the user to leave a rating between 0.5 and 5.0 stars. The rating already selected by the user is highlighted in `Yellow`, with a `Green` highlight being applied to any stars upto where the user is current highlighting with the mouse.
    - The `Title` and `Content` sections of the form allow the user to provided a title and the content of their review respectively.
    - Following the form being validated successfully, the form is submitted and the rating, title and content are submitted to the database. Along with this information, the product ID, date, time and user ID is also stored.
    - If a user has already left a review, they will instead be shown a message stating `You've already left a review for this product!`

- ### Product Management

  - Whether `Adding` or `Editing` a product the user is shown the same form, however the `Edit Product` page will already be populated with data.
  - Due to the similarities of the form, I will first discuss the form itself before going into the different between the two pages.
  - Both pages `REQUIRE` the following information:
    - Category
    - Name
    - Description
    - If the product `Has Sizes`
    - Price (This is used as the Small price for products with sizes, or standard price for other products)
    - Sale Price (This is used in the search function for the purpose of ensuring prices are sorted correctly)
    - Ingredients (The [Sorted M2M Filter Horizontal Widget](https://pypi.org/project/django-sortedm2m-filter-horizontal-widget/) was used to enable vertical sorting of products, replacing the standard `Hold Ctrl and Click` select menu.)
  - All other fields on the page are optional.
  - The only other difference between the pages, other than the ones already mentioned, is the additional modifying of the title when editing a product.

- ### Cart

  - The cart is split into two main elements
    - Products Section
    - Total Section

  #

  ![Cart - Products Image](readme_content/cart_product.png)

  - Products Section
    - The products section is also split down further into 5 sections:
      - The `Product` section displays an image for each of the products contained within the cart.
      - The `Product Info` section displays the name of the product chosen. If the product has a size value, if will be displayed on the following line, otherwise this value will not appear. Finally the SKU of the product will be displayed.
      - The `Price` section displays the unit price for the item, and size if applicable, chosen.
      - The `Quantity` section displays the current quantity of the product chosen, with controls provided to allow the user to update the quantity if they wish to.
      - The final section is the `Subtotal` section which multiplies the value from the `Price` field with the value of the `Quantity` field to calculate the total being paid for this item.

  #

  ![Cart - Total Image](readme_content/cart_total.png)

  - Total Section
    - The `Cart Total` field calculates the sum of all `Subtotal` values within the cart to determine the overall total value of products.
    - The `Delivery` field displays the value of the `Cart Total` field multiplied by the `STANDARD_DELIVERY_PERCENTAGE` value from `settings.py`. This is currently set to 10%.
    - The `Grand Total` field shows the sum of the `Cart Total` and `Delivery` fields.
    - Below the `Grand Total` field is a notice to the customer informing them of the required further spend for them to receive free delivery of their products. This value is calculated by subtracting the `Cart Total` value from the `FREE_DELIVERY_THRESHOLD` value set in `settings.py`. The delivery cost is not included in this calculation.
    - The final part of the `Total Section` are the `Keep Shopping` and `Secure Checkout` buttons. Like the `Product Detail` page, the `< Keep Shopping` button will return the user to the main products page, leaving the current products in the cart as they are. The `Secure Checkout` button will navigate the user to the `Checkout` page which is described in more detail in the next section.

- ### Checkout

  - The Checkout page is split into two main columns: Customer Details & Order Summary. The Checkout app also features a `Checkout Success` page once the order has been submitted, and a loading overlay whilst the order is being submitted.

    - Customer Details

      - The first section of this column asks for the customer to provide their name and email address. The name is required to ensure the correct delivery information is added to the package prior to it being dispatched, with the email address being used to send order confirmation to the customer. The customer is not required to sign in to complete their order, however if they are signed in, and have saved their delivery information, these fields will be populated.
        ![Checkout - Details Image](readme_content/checkout_details.png)
      - The box below this uses the Address Finder API provided by [Woosmap](https://www.woosmap.com/). This has been configured to only search for address within the UK as this is where the business is based. The user has the option of typing their address into this box and clicking the corresponding result, with the information then being used to fill the form below.
      - If the customer does not wish to use the Address Search feature, they can manually enter their details into the address details form, with the following details being required:
        - Phone Number
        - Street Address
        - Town or City
        - Post Code
      - If the user is already registered, and has delivery information stored, this information will be automatically populated.
      - The user also has the option to update or save their delivery information, which can be used to populate the form for future orders by ticking the checkbox below the form.
        ![Checkout - Delivery Image](readme_content/checkout_delivery.png)
      - The payment element of the checkout app is provided by [Stripe](https://stripe.com/). Stripe is used as a secure payment method, and means that no card information is stored within the website database, with all information being provided back to the website via Webhooks.
        - If `payment_intent.succeeded` is returned via the webhook, the order will be submitted.
        - If `payment_intent.payment_failed` is returned via the webhook, the order is not submitted, with the user being returned to the checkout app, with a message provided stating the order has failed.
      - The following card details can be used to test the payment functionality of the Checkout App:

        | Scenario                           | Card Number         | Expiry Date | CVC | Postal Code |
        | ---------------------------------- | ------------------- | ----------- | --- | ----------- |
        | Payment Succeeds                   | 4242 4242 4242 4242 | Any         | Any | Any         |
        | Payment requires authentication    | 4000 0025 0000 3155 | Any         | Any | Any         |
        | Card declined - Insufficient Funds | 4000 0000 0000 9995 | Any         | Any | Any         |

      - The final elements of the `Customer Details` section are the `Adjust Cart` and `Complete Order` buttons. The `< Adjust Cart` button will return the user to the cart app, with any details entered into the form being lost, unless already saved to the users profile. The `Complete Order` button will first submit the payment information via the `Stripe` webhook.
      - Once `payment_intent.succeeded` is received the order will be submitted and the user will be navigated to the `Checkout Success` page.
        ![Checkout - Payment Image](readme_content/checkout_payment.png)

    - Order Summary

      - The order summary section shows a compacted version of the data displayed in the `Cart` app.
      - The title of the `Order Summary` section shows the number of products contained within the cart.
      - Each item within the cart is listed, including the size (if applicable) and quantity.
      - Unlike the `Cart` app, in the `Order Summary` view only the Subtotal for each product is shown.
      - As with the `Cart` app, the Order Total, Delivery charage and Grand Total values are shown to give the customer the opportunity to confirm everything looks correct before their order is submitted.
      - Using `Stripe` webhooks, the database is queried to confirm the order was created successfully. If the order cannot be found, the webhook handler will created the order in the database using the information sent with the original payment intent.
        ![Checkout - Order Summary Image](readme_content/checkout_order_summary.png)

    - Loading Overlay

      - When the `Complete Order` button is clicked and the form validation on the checkout page is passed, a loading overlay is displayed preventing any other changes to the form, or any further form submissions.
      - The loading icon is provided by [Font Awesome](https://fontawesome.com/), using the `fa-cake-candles` class, and is animated with the `fa-beat` class.

        ![Checkout - Loading Image](readme_content/loading.png)

    - Checkout Success

      - Once all of the previous steps have been completed, the `payment_intent.succeeded` response has been received and confirmation that the order has been created in the database, the user is taken to the `Checkout Success` page.
      - Above the order summary itself, a message is shown advising the user that a confirmation email will be sent to them, confirming the details of their order.
      - The user is then provided with the `Order Number` and `Order Date`, which can be used in the event the customer needs to contact the business, speeding up the process of retrieving the relevant order.
      - The `Order Details` section provides further confirmation of the products that have been ordered, including quantity and individual unit price.
      - The `Delivering To` section displays the address information provided by the customer. This is important as it gives the customer a chance to check over the details and to confirm that they are correct.
      - The final section within the order summary box is the `Billing Info` section, providing a further recap of the Order Total, Deliverty charge and Grand Total of the order.
      - Below this is a message advising the customer to get in touch if they spot any errors on the form, ensuring that the corrections can be made as soon as possible.
      - Finally, a button containing the text `Take me back to the cakes!` is displayed and returns the user to the main `Products` page.
        ![Checkout - Checkout Success Image](readme_content/checkout_success.png)

- ### About Us

  - The [image used on the 'About Us' page](https://unsplash.com/photos/5K5Nc3AGF1w) was made available via [Unsplash](https://unsplash.com/) by the user [American Heritage Chocolate](https://unsplash.com/@americanheritagechocolate) and is used under the Unsplash License.
  - The page gives a brief history of the business and the content is set using [Django Quill Editor](https://github.com/LeeHanYeong/django-quill-editor). This allows easier editing for the business owner without needing to have any knowledge of HTML or CSS.
  - The About Us page ends with a reminder to contact the business with any questions or queries, hopefully increasing engagement and leading to more business.

- ### Contact Us

  - The `Contact Us` page is linked to from various other places on the website and allows users to contact the business with any query they may have.
  - The form was purposefully left as basic as possible to give maximum flexibility to the user. The form consists of 3 text fields (Email, Subject and Message.)
  - Once all sections have been completed and the `Submit` button has been clicked, the information is stored in the database and the user is directed to the `Contact Success` page.
  - The `Contact Success` page contains a message stating `Thank for getting in touch with us. We've got your message, and we'll be in touch as soon as possible.`, with a button returning the user to the main products page.
  - The messages sent by users can be viewed from the admin panel, where the option is available to mark a message as actioned, allowing other people who may use the admin panel to see which messages have/have not been responded to.

    ![Contact Us Image](readme_content/contact_us.png)

- ### Toasts

  - Toasts appear in the top-right corner on the screen when any information needs to be relayed to the user. The toasts appear using a CSS animation which alters the location of the toast.
  - The toasts display messages under the categories of `Success`, `Alert`, `Warning` and `Error`.
  - The toasts have slightly different designs depending on the type of toast used.

    - The `Alert`, `Warning` and `Error` toasts all share the same design of a dark header and dark body with only the colour of the icon on the alert change.
    - The `Success` toast instead has a dark header and light body. This is due to the amount of information displayed on the `Success` toast when items are added to the basic and aids readability for the user.

    ![Toasts Image](readme_content/toasts.png)

- ### Footer

  - The footer is displayed on all pages other than the main landing page of the website, and sits at the bottom of each page.
  - The top part of the footer is a full width div containing links to the Social Media pages for the business.
  - The lower section of the footer is split into three columns with the first having a short `About Us` synopsis. The title of the column also links to the `About Us` page, but is not underlined due to the link also being available in the navbar.
  - The middle column contains `Useful Links` which direct to individual pages for the Refunds & Returns Policy, Postage & Packaging Policy and Privacy Policy. Like the `About Us` page, all content on these pages is set using [Django Quill Editor](https://github.com/LeeHanYeong/django-quill-editor). This allows easier editing for the business owner without needing to have any knowledge of HTML or CSS.
  - The third and final column contains contact information for the business, with a `mailto:` link being used to highlight the email address.
  - Icons provided by [Font Awesome](https://fontawesome.com/) throughout the footer.

    ![Footer Image](readme_content/footer.png)

- ### Other

  - Error 404 Page

    If the user navigates to a page that does not exist, the 404.html page will render. This page has the same basic layout as the home page of the site, but displays different text content. The button, however, still returns the user to the main products page.

    ![404 Image](readme_content/404.png)

  - Error 500 Page

    If the user navigates to a page that causes a response the server does not know how to handle, the 500.html page will render. This page has the same basic layout as the home page of the site, but displays different text content. The button, however, still returns the user to the main products page.

    ![404 Image](readme_content/500.png)

#

[Back to top ⇧](#nibble-kitchen)

#

## Testing

Testing and results can be found in the [TESTS.md](TESTS.md) file.

## Deployment

- ### Github

  - Before you start, a repository (repo) is required on Github which can be created in a number of ways.

    - #### Create A New Repo

      1. Log into Github.
      2. In the top left corner of the page is a column titled 'Recent
         Repositories' Click the button labelled 'New'.
      3. Name the repository and click 'Create repository'.
      4. Your new repository is now set up and ready to use.

    - #### Forking

      Creating a forked repo creates a copy of a repo within
      github account.

      How to Fork A Repository:

      1. Sign in to Github and go to the required repo.
      2. Locate the Fork button at the top right of the page.
      3. Click the button then click 'Create Fork'.
      4. You have now successfully forked the repo.

    - #### Clone

      Cloning a repo creates a copy of a repo on your
      local machine.

      How to Clone A Repository;

      1. Sign in to Github and go to the required repo.
      2. At the top of the page, above the files, is a button labelled
         'Code'
      3. Select the required option from HTTPS, SSH or Github CLI, then click the clipboard icon to copy the URL.
      4. Open git bash
      5. Type 'git clone' and then paste the copied URL. Press Enter.

- ### Django

  This project is built on the Django framework.

  Django can be installed by following the steps below:

  1. In your chosen IDE type the command:  
     `pip3 install django`
  2. To create an name your project use the command:  
     `django-admin startproject <your_project_name> .`
  3. A gitignore file is an important addition as you can specify
     which files should not be uploaded to the Github repo, such as
     database credentials.

     A gitignore file can be created in the CLI using the command:

     `touch .gitignore`

     The .gitignore file for this project can be found [here](.gitignore)

  4. To check django has been installed and your project created successfully, type the following command:

     `python3 manage.py runserver`

     Following the link provided in the CLI should display the Django landing page.

  5. Next, initial database migrations need to be completed. This can be achieved with the command:

     `python3 manage.py migrate`

     You can see the changes to be made without executing them with the command:

     `python3 manage.py migrate --plan`

  6. In order to have access to the admin panel, a superuser is required. This is created with the command:

     `python3 manage.py createsuperuser`

     This will then ask you to create a username and password with an optional email address.

  7. Once these steps are completed you can push your changes to Github using the commands below in order, or with the interface in your chosen IDE:

     ```
     git add .
     git commit -m "initial commit"
     git push
     ```

[Back to top ⇧](#nibble-kitchen)

### Heroku

Heroku is the chosen cloud platform for the project, allowing the project to be built and deployed via a link to the Github Repo.

1. Once you are logged in to Heroku, click the 'New' button in the top right corner of the page and select 'Create new app'.
2. Select a name for your app (which must be unique!), select the closest region to you and click 'Create App'.
3. Once the app has been created, select the resources tab, navigate to the 'Add-ons' section and search for 'Heroku Postgres'.
4. Select 'Heroku Postgres', then under 'Plan name' choose 'Hobby Dev - Free' and click 'Submit Order Form'.

To use Postgres with Django, additional tools are required, and can be installed via the CLI in your chose IDE.

1.  In your CLI type the command:  
    `pip3 install dj_database_url`
2.  Once completed, enter the following command into the CLI:  
    `pip3 install psycopg2-binary`
3.  At the top of the settings.py file in your main project folder, and the line:
    ```
    import dj_database_url
    ```
4.  Scroll down in settings.py to the `DATABASES` section. Replace the code in this section with the code below.

    ```
    DATABASES = {
        'default': dj_database_url.parse(<DATABASE_URL_GOES_HERE>)
    }
    ```

    The Postgres Database URL can be found in the settings tab of your app in Heroku, under the Config Vars section.

5.  As we are now connected to a new database, we need to repeat the previous migration steps. This is done by running the command:  
    `python3 manage.py migrate`

6.  We also need to create a new superuser with the command :  
    `python3 manage.py createsuperuser`

7.  Before we commit these changes, we will need to alter the `DATABASES` section in settings.py to prevent the Postgres Database URL ending up in version control.

8.  This can be achieved by replacing the existing content of the `DATABASES` section with the code below.

    ```
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
    }
    ```

9.  Gunicorn needs to be installed next, which acts as our web server. This is done with the command:

    `pip3 install gunicorn`

10. We also need to create a `Procfile` to tell Heroku to create a web dyno. In the root directory of your app, create a file named `Procfile` and inside insert the code:

    `web: gunicorn PROJECT_NAME_HERE.wsgi:application`

11. In Heroku, we need to prevent the collection of static files until we have set up AWS. This is achieved by navigating to the Settings tab in Heroku, selecting the Config_Vars section and entering `DISABLE_COLLECTSTATIC` in the `KEY` field, and `1` in the `VALUE` field and clicking the 'Add' button.

    When the site is deployed at this stage, no static files will be present, but this will be rectified later.

12. In order to allow your project to be viewed when deployed to Heroku, we need to add the Project URL to the `ALLOWED_HOSTS` section of settings.py
    ```
    ALLOWED_HOSTS = ['PROJECT_NAME_HERE.herokuapp.com', 'localhost', '127.0.0.1']
    ```
13. The changes can now be committed and pushed to Github. Once this has been done, we can push the changes to Heroku with the command:

        `git push heroku main'

[Back to top ⇧](#nibble-kitchen)

### AWS

Amazon's AWS platform us used to store all static and media files.

#### S3

1. An AWS account is required which can be created [here](https://aws.amazon.com/).
2. Once you have created an account and logged in, select the `Services` button in the top left corner of the page, scroll to the bottom and select `Storage` followed by `S3`.
3. Once on the S3 page we can create a new bucket by clicking the orange `Create bucket` button on the right side of the page.
4. Provide a name for the bucket and select the closest region to you.
5. Under `Object Ownership` select `ACLs enabled` and leave the Object Ownership as `Bucket owner preferred`.
6. Uncheck `Block all public access` checkbox and check the warning box to acknowledge that the bucket will be made public, then click `Create bucket` at the bottom of the page.
7. Once created, click your bucket's name and navigate to the `Properties` tab. Scroll to the bottom and under `Static website hosting` click the `Edit` button. Change the `Static website hosting` option to `Enable`. Type `index.html` into the `Index document` field. You can then scroll to the bottom of the page and click `Save Changes`.
8. Navigate to the `Permissions` tab, Scroll to the `Cross-origin resource sharing (CORS)` section, click the `Edit` button and paste in the following code:
   ```
   [
       {
           "AllowedHeaders": [
           "Authorization"
           ],
           "AllowedMethods": [
           "GET"
           ],
           "AllowedOrigins": [
           "*"
           ],
           "ExposeHeaders": []
       }
   ]
   ```
9. Scroll up to the `Bucket Policy` section. Click the `Edit` button and then `Policy generator`.
10. Select `S3 Bucket Policy` in the 'Select Type of Policy' dropdown menu. Inside the `Principal` field type `\*` to allow all principals.
11. Select `GetObject` from the `Actions` dropdown menu.
12. Head back to the previous tab and navigate to the `Properties` tab. Copy the value from the `Amazon Resource Name (ARN)` field, return to the `Policy Generator` tab and paste the value into the `Amazon Resource Name (ARN)` field .
13. Once this has been completed, click `Add statement`, then `Generate Policy`. Copy the generated policy and paste it into the `Bucket policy` editor.
14. Before saving, add a `/*` at the end of your resource key. This is to allow access to all resources in this bucket.
15. Next, scroll down to the `Access control list (ACL)` section and click the `Edit` button.
16. Next to `Everyone (public access)`, check the `List` checkbox. This will generate a warning which must be acknowledged. Once this is done click `Save changes`.

#### IAM (Identity and Access Management)

1. Now that the bucket has been created, we need to create a user to access it. In the search bar at the top of the page, type `IAM` and select it.
2. Once on the `IAM` page, click `User Groups` from the side bar on the left of the page, followed by `Create group` in the top right of the next page.
3. To make managing mulitple projects in the future a little easier, it's best to name your user group something like `manage-_your-project-name_`. Once you've selected a name, click `Create group` at the bottom of the page.
4. From the side bar on the left of the page, click `Policies`, then `Create policy`.
5. Select the `JSON` tab and click `Import managed policy`. Search for `S3` and select `AmazonS3FullAccess`. Click import.
6. Once imported this will need to be edited slightly. Return to your bucket and copy your ARN number. Back on the `Create polioy` page, update the Resource key to include your ARN, and another line with your ARN followed by a `/*`. It should look like the code below:
   ```
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Action": [
                   "s3:*",
                   "s3-object-lambda:*"
               ],
               "Resource": [
                   "YOUR-ARN-HERE",
                   "YOUR-ARN-HERE/*"
               ]
           }
       ]
   }
   ```
7. Click the `Next: Tags` button, click the `Next: Review` button. Enter your policy name into the `Name` field andclick `Create policy`.
8. Click on `User groups` in the side bar on the left of the page, and click the earlier created group. Go to the `Permissions` tab and click `Add permission` and select `Attach policies`.
9. Find the newly created policy, select it and click `Add permissions`.
10. Finally, we need to create a user. Select `Users` from the side bar on the left of the page and click `Add users`.
11. Give your user name related to your project, such as `project-name-static-user`, check `Access key - Programmatic access`, and click `Next: Permissions`.
12. Select your previously created group with the required policy attached and click `Next: Tags`, `Next: Review`, then `Create user`.
13. On the next page, download the CSV file. This contains the user's access key and secret access key which you will need later.

[Back to top ⇧](#nibble-kitchen)

#### Connecting AWS to Django

Now that AWS has been fully configured for our needs, we need to connect Django to AWS.

1. Firstly, we will need to install two packages. `Boto3` and `django-storages`, which can be done with the following commands:
   ```
   pip3 install boto3
   pip3 install django-storages
   ```
2. Add `storages` to the `INSTALLED_APPS` section of settings.py.
3. We also need to add some additional settings to let Django know which AWS bucket it will be communicating with.
4. At the bottom of settings.py add the following code:
   ```
   if 'USE_AWS' in os.environ:
       AWS_STORAGE_BUCKET_NAME = 'your-bucket-name-here'
       AWS_S3_REGION_NAME = 'insert-your-region-here'
       AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
       AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
   ```
5. We now need to return to Heroku. In the `Settings` tab, under `Config Vars`, we need to add the values from the CSV file we downloaded earlier.
6. Add the key `AWS_ACCESS_KEY_ID` with the value that was generated in the CSV file. Add the key `AWS_SECRET_ACCESS_KEY`, and add the value that was generated in the CSV file. Add the key `USE_AWS` and set the value to True.
7. We can now also remove the DISABLE_COLLECTSTAIC variable, as we now want static files to be collected and uploaded to AWS.
8. Return to the settings.py file and add the following code to the `USE_AWS` if statement created earlier:
   ```
   AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
   ```
9. We need to create a file to tell Django that we want to use S3 to store our static files. In the root directory of your project, create a file called `custom_storages.py`. Inside this file add the following code:
   ```
   from django.conf import settings
   from storages.backends.s3boto3 import S3Boto3Storage
   ```
10. Underneath the imports insert these two classes:

    ```
    class StaticStorage(S3Boto3Storage):
        location = settings.STATICFILES_LOCATION


    class MediaStorage(S3Boto3Storage):
        location = settings.MEDIAFILES_LOCATION
    ```

11. In settings.py, underneath the bucket config settings but still inside the if statement, add these lines:
    ```
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'
    ```
12. Next, you will also need to override and explicitly set the URLs for static and media files using your custom domain and new locations. To do this add these two lines inside the same if statement:
    ```
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
    ```
13. We can now save, add, commit and push the changes and files will b e added to the AWS S3 bucket. Inside the if statement add the code below which lets the browser know it can cache static files:
    `AWS_S3_OBJECT_PARAMETERS = { 'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT', 'CacheControl': 'max-age=94608000', }`
    14.In `S3` on `AWS`, go to your project bucket and click `Create folder`. Name the folder `media` and click `Save`.

14. Inside the media folder, click `Upload`, `Add files`, and then select all media files used in your project.
15. Under `Permissions`, select `Grant public-read access` and click `Upload`. You will need to acknowledge the displayed warning before you can do this.

[Back to top ⇧](#nibble-kitchen)

### Stripe

Stripe is used to handle the checkout process when a payment is made. A Stripe account is needed. You can sign up [here](https://stripe.com/en-gb).

#### Payments

1. To set up Stripe payments you can follow the guide available [here](https://stripe.com/docs/payments/accept-a-payment#web-collect-card-details).

#### Webhooks

1. To set up a webhook, sign into your Stripe account and click `Developers` located in the top right of the navbar.
2. In the side bar on the left of the page, click `Webhooks`, then `Add endpoint` on the right side of the page.
3. Enter your Heroku project name, checkout app name, followed by wh into the `Endpoint URL` field. It should look something like this:
   ```
   https://your-app-name.herokuapp.com/checkout/wh/
   ```
4. Click `+ Select events` and check `Select all events` at the top of the page. Click `Add events` at the bottom of the page, followed by `Add endpoint` on the next page.
5. The webhook has now been created and should have generated a secret key. We will need this to add to the Heroku Config Vars.
6. Open your app on Heroku and navigate to the `Config Vars` section under the `Settings` tab. You will need the secret key just generated for your webhook, in addition to your Publishable key and secret key that you can find on the [Stripe API keys page](https://dashboard.stripe.com/test/apikeys).
7. Add these values and key pairs to the Config Vars:
   ```
   STRIPE_PUBLIC_KEY = 'insert your stripe publishable key'
   STRIPE_SECRET_KEY = 'insert your secret key'
   STRIPE_WH_SECRET = 'insert your webhooks secret key'
   ```
8. In setting.py in your Django project, insert the following near the bottom of the file:
   ```
   STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
   STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
   STRIPE_WH_SECRET = os.getenv('STRIPE_WH_SECRET', '')
   ```

[Back to top ⇧](#nibble-kitchen)

## Credits

- [Delboy](https://github.com/Delboy) for the "Back to Top" idea in the readme.

- ### Media

  - All product images have been taken from the current website for [Nibble Kitchen](https://nibblekitchen.co.uk/), with permission from the owner.

  - The [main background image used on the 'Home' page](https://unsplash.com/photos/YpIKbBZtSWY) was made available via [Unsplash](https://unsplash.com/) by the user [Deva Williamson](https://unsplash.com/@biglaughkitchen) and is used under the Unsplash License.

  - The [image used on the 'About Us' page](https://unsplash.com/photos/5K5Nc3AGF1w) was made available via [Unsplash](https://unsplash.com/) by the user [American Heritage Chocolate](https://unsplash.com/@americanheritagechocolate) and is used under the Unsplash License.

- ### Languages

  - [Bootstrap](https://getbootstrap.com/)
  - [CSS](https://en.wikipedia.org/wiki/CSS)
  - [Django](https://www.djangoproject.com/)
  - [HTML5](https://en.wikipedia.org/wiki/HTML5)
  - [Javascript](https://en.wikipedia.org/wiki/JavaScript)
  - [JQuery](https://en.wikipedia.org/wiki/JQuery)
  - [Python](<https://en.wikipedia.org/wiki/Python_(programming_language)>)

- ### Libraries, Frameworks and Tools

  - [AllAuth](https://www.intenct.nl/projects/django-allauth/) - Django app used for local authentication.
  - [Am I Responsive](http://ami.responsivedesign.is/) - Used to verify responsiveness of website on different devices.
  - [Balsamiq](https://balsamiq.com/) - Used to generate Wireframe images.
  - [Browser Stack](https://www.browserstack.com/) - Used for Cross Site Browser Testing.
  - [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) - Used for overall development and tweaking, including testing responsiveness and performance.
  - [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - Django app to allow control over rendering behaviour of django forms.
  - [Django Quill Editor](https://github.com/LeeHanYeong/django-quill-editor) - WYSIWYG editor added for easy updating of text only content on the site.
  - [Favicon.io](https://favicon.io) - Used to generate Favicon image.
  - [Flake8](https://github.com/pycqa/flake8) - Linter used to check style and quality of code.
  - [Flake8 HTML](https://pypi.org/project/flake8-html/) - Tool to output Flake8 test report.
  - [Font Awesome](https://fontawesome.com/) - Used for icons on multiple pages.
  - [GitHub](https://github.com/) - Used for version control.
  - [Gunicorn](https://gunicorn.org/) - Python WSGI HTTP Server
  - [Heroku](https://heroku.com) - Used for deployment and hosting of the project.
  - [JQuery](https://en.wikipedia.org/wiki/JQuery) - Used to simplify definition of DOM elements, but used minimally with a preference for vanilla Javascript.
  - [JSHint](https://jshint.com/about/) - Linter used to flag errors, bugs and warnings in Javascript code.
  - [Pillow](https://pypi.org/project/Pillow/) - Python Imaging Library to add image processing capabilities to the project.
  - [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode) - Used for consistent code formatting.
  - [Slack](https://slack.com/) - Used for support and advice from the Code Insitute Community.
  - [Sorted M2M Filter Horizontal Widget](https://pypi.org/project/django-sortedm2m-filter-horizontal-widget/) - Django admin widget to allow horizontal sorting of products and ingredients.
  - [Stripe](https://stripe.com/) - Payment Processing Platform used to handle card details in the checkout app.
  - [Visual Studio Code](https://code.visualstudio.com/) - Application used for development of this site.
  - [W3C](https://www.w3.org/) - Used for HTML & CSS Validation.
  - [WAVE](https://wave.webaim.org/) - Used for Accessibility evaluation.
  - [Woosmap](https://www.woosmap.com/) - Provided address searching API for checkout app.

