![Code Institute Logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Welcome Code Institute Assessor, to Brandon's Bookshop!


## [Final Deployment Available Here](https://books-project-5-992c27c88b5c.herokuapp.com/) 

---

### Table of Contents
## Table of Contents

1. [Brandon's Bookshop](#brandons-bookshop)
   - [Key Features](#key-features)
      - [Full E-Commerce Shopping Site](#full-e-commerce-shopping-site)
      - [Navigation](#navigation)
      - [Product Categorisation](#product-categorisation)
      - [Blog Post Creation and Management](#blog-post-creation-and-management)
      - [Comment and Reply Functionality](#comment-and-reply-functionality)
      - [Like Functionality](#like-functionality)
      - [Rating System](#rating-system)
      - [Newsletters](#newsletters)
      - [Featured Books](#featured-books)
      - [User Testimonials](#user-testimonials)
      - [About and FAQ Page](#about-and-faq-page)
      - [Favicon](#favicon)
      - [Wireframes](#wireframes)
      - [Colour Palette](#colour-palette)
   - [Agile Development Approach](#agile-development-approach)
      - [Kanban Project Board](#kanban-project-board)
      - [Milestones](#milestones)
      - [Continuous Feedback and Iteration](#continuous-feedback-and-iteration)
      - [Dynamic Adaptability and Continuous Improvement](#dynamic-adaptability-and-continuous-improvement)
2. [Business Model](#business-model)
   - [Marketing](#marketing)
3. [Deployment](#deployment)
   - [Local Deployment](#local-deployment)
   - [Heroku Deployment](#heroku-deployment)
   - [Forking](#forking)
4. [Testing](#testing)
   - [Manual Testing]{#manual-testing)
   - [W3C Validator](#w3c-validator)
   - [CSS](#css)
   - [Python](#python)
   - [Javascript](#javascript)
   - [Lighthouse](#lighthouse)
   - [Responsivity](#responsivity)
5. [Future Features](#future-features)
6. [Bugs](#bugs)
7. [Credits](#credits)


# Brandon's Bookshop

![image](https://github.com/BrandonPCollins/project-5-bookshop/assets/131177569/ce5e2dad-bef0-4a86-b256-6e0c10e6ec38)

Brandon's Bookshop offers a comprehensive e-commerce platform where users can browse, search, and purchase rare books online. The platform provides a seamless shopping experience, with intuitive navigation, secure transactions, and a user-friendly interface.

## Key Features

Brandon's Bookstore contains all the key features one would expect from an e-commerce store as a user, while also providing back-end functionality for the administrative side. In concordance with the marking criteria, Brandon's Bookshop features several custom models completely distinct from those showcased within

### Full E-Commerce Shopping Site

As an e-commerce platform, Brandon's Bookstore operates primarily through its online storefront. Customers can browse through the extensive collection of books, conveniently place orders, and securely complete transactions without leaving the comfort of their homes.

### Navigation

Embedded via an includes template onto the head of every page is a responsive Navbar element which provides the user quick and easy access to every page on the Brandon's Book site. The Navbar dynamically resizes and alters its layout depending on the screen's size to provide users with a seamless and effortless navigation experience. This navigation bar includes a search bar to quickly browse the site's products via their names and descriptions, links to the user's profile and cart, and a variety of list items and drop-down menus providing access to the site's pages.

![image](https://github.com/BrandonPCollins/project-5-bookshop/assets/131177569/2312a287-eec3-47a0-a7eb-f69108ab6976)

### Product Categorisation 

Products are categorized for easy navigation and search. This feature enhances the user experience by allowing users to quickly find the books they are interested in. Further the 'Category' dropdown menu in the site's Navbar is updated dynamically from the current categories, meaning site admins won't have to update any HTML if they add further categories in the site's admin.

### Blog Post Creation and Management

Admins can create and manage blog posts from the site itself rather than having to enter the Django admin, providing a platform for sharing news, updates, and interesting content with the user community. These blog posts were designed with full CRUD functionality, thus allowing the admin to create new posts, read other existing posts, update older posts and delete ones that are no longer necessary. By moving this full functionality from the admin to an integrated series of pages it creates a seamless blogging experience for the site admin.

### Comment and Reply Functionality

All users can comment on blog posts made by admins, and reply to other users comments, facilitating conversation and discussion. The comments were created with full CRUD functionality in mind from the user's point of view, allowing them to create their comments, read other user's comments, update their comments and delete them.

### Like Functionality

In addition to the ability to comment on posts and reply to other user's comments, users can display their agreement with posts via the like system.

### Rating System

Users have the ability to rate products using an integrated and dynamically visual star-rating system.

![image](https://github.com/BrandonPCollins/project-5-bookshop/assets/131177569/9fb6c98b-6f54-4c00-93a0-0b58c1307c3e)

### Newsletters

Brandon's Bookshop offers newsletters to keep users informed about the latest updates, promotions, and events. Newsletter content could include but not be limited to acquisitions of new rare books by the store, important news regarding the store, exclusive offers, potential visits and events featuring famous authors, and more.

![image](https://github.com/BrandonPCollins/project-5-bookshop/assets/131177569/00857f0c-6e61-4bc7-bf87-5552e7636a93)

### Featured Books 

All products have a boolean value which when enabled add them to the featured books carousel on the site's index page. Scrolling carousel allows users to scroll through the books and allows me to know consistently that it will always appear as a single book on the main page no matter how many are added as "featured". Initially I didn't account for this and when I tested it all the featured books stacked on top of each-other leading to an incredibly bloated and long page, and thus made me adopt the carousel approach to featuring the products.  

### User Testimonials

To increase the trustworthiness of our site and thus elevate it within the SEO standings I've included a rotating carousel or User Testimonials at the foot of the home/index page. At the moment it's two static reviews written into the page itself, it serves as good practice in gaining user loyalty and SEO optimisation, and a proof of concept that can be expanded upon to include real and dynamically scripted user experience testimonials in the future.

![image](https://github.com/BrandonPCollins/project-5-bookshop/assets/131177569/7f910b41-5c68-429d-9094-c2b756f19f09)

### About and FAQ Page

The About and FAQ pages provide additional information about the bookstore and answer common questions. These pages not only enhance the user experience but also contribute to the site's SEO standings.

![image](https://github.com/BrandonPCollins/project-5-bookshop/assets/131177569/f71a1700-8cfa-4f14-9972-a11f384d25aa)

### Favicon

Brandon's Bookshop features a custom favicon for brand recognition and visual identity. The favicon is prominently displayed in browser tabs, bookmarks, and shortcuts, helping users identify the site quickly and easily. Due to my complete lack of artistic talent, the favicon was created using Microsoft Bing Image Generator.

![favicon](https://github.com/BrandonPCollins/project-5-bookshop/assets/131177569/b978047b-9548-4ece-b52d-6c943867d7fa)

### Wireframes

The structure of the site followed the basic use of a base.html file and the inclusion of the navbar at the top of each page and the footer at the bottom to provide consistency across the user experience. Sandwiched between the navbar and the footer on each page was the content of the page itself, be it the product list, product details, the blog page or the FAQ section. This repeated layout provides the user with familiarity upon visiting each page. The only exception to the rule was the landing page which is slightly different due to the various calls-to-actions featured including the banner and the featured product carousel.

All Wireframes were created using wireframe.cc The wireframe presented here for the Product List page is broadly representative of all other pages featured on the site.

![image](https://github.com/BrandonPCollins/project-5-bookshop/assets/131177569/9150e750-3cd3-453d-8365-969730dd5a9d)

![image](https://github.com/BrandonPCollins/project-5-bookshop/assets/131177569/1482d143-e52f-427c-a57c-f30f7dbf000f)


### Colour Palette  

Used coolors.co to generate a colour palette for the site. It was important for me to have a clean black and white as the base for the site's colour schematic, bestowing the site a clean, professional look while calling to mind the simplicity of the written page. Another important aspect was the featuring of an ochre reddish brown colour, one often semantically associated with older books due to the wearing of their leather colours, which the palette generator graciously provided. The shade of English violet provided by the generator was then used on the site's banner as there were some issues with the legibility of the text situated atop the background image. By placing the text atop a card of a complimentary colour to the brown it ensured that the text would immediately grab the user's attention. The final colour of Engineering Orange goes unused in the current site's iteration to keep the colour scheme muted, but they complement the ambit well and could easily be integrated in the future.

![image](https://github.com/BrandonPCollins/project-5-bookshop/assets/131177569/8f4f872f-ecfd-43c9-8fce-6cde6ec57a79)


## Agile Development Approach

Throughout the development process of Brandon's Bookshop, an Agile Development approach was adopted to ensure flexibility, collaboration, and iterative improvement. Agile methodologies were employed to manage tasks, track progress, and adapt to evolving requirements effectively.

### Kanban Project Board

A Kanban Project Board was utilized as a central tool for managing the project's development. This board provided a visual representation of tasks, allowing the tracking of the project's status and progress. The board was organized into different columns representing various stages of development, including "To Do," "In Progress," and "Completed." By using this board, I could easily prioritize tasks, allocate resources efficiently, and monitor the overall progress of the project.

- [Kanban Project Board](https://github.com/users/BrandonPCollins/projects/5)

### Milestones

To facilitate better organization and tracking of the project's progress, milestones were established to mark significant achievements or phases in the development lifecycle. These milestones served as checkpoints for the team, helping to ensure that key objectives were met within specified timelines. Each milestone was associated with specific goals and deliverables and composed of the various User Stories, providing clear direction and focus for the development efforts.

- [Milestones](https://github.com/BrandonPCollins/project-5-bookshop/milestones)

### Continuous Feedback and Iteration

A key aspect of Agile development is the continuous feedback loop, which allows for ongoing refinement and improvement of the product. Continuous testing and feedback from mentors, our cohort leader and fellow students was used to identify areas for improvement, address issues, and make necessary adjustments to meet user needs and contribute to creating new User Stories. 

### Dynamic Adaptability and Continuous Improvement

Agile methodologies emphasize adaptability and responsiveness to change, allowing the development to adjust its approach based on evolving requirements and feedback. As such, the development process for Brandon's Bookshop was characterized by dynamic adaptability and continuous improvement. The development process remained flexible and open to change, making adjustments as needed to accommodate shifting priorities, emerging challenges, and new opportunities. By continuously refining and enhancing the product, the team was able to deliver a solution that effectively addressed user needs and delivered value to stakeholders.

---

## Business Model

Brandon's Bookstore operates as a business-to-customer (B2C) e-commerce platform, offering a specialized selection of rare and valuable books to discerning customers. The core objective of the platform is to provide a seamless and convenient online shopping experience for individuals seeking unique and tangible luxury products.

The bookstore focuses exclusively on curating a collection of rare, antique, and valuable books. This specialization allows Brandon's Bookstore to distinguish itself in the market and cater to a niche audience of book enthusiasts, collectors, and connoisseurs.

The primary revenue stream for Brandon's Bookstore comes from the sale of rare and valuable books through its online platform. Additional future revenue opportunities would arise from value-added services such as appraisals, restoration services, and subscription-based memberships offering exclusive benefits to customers, all of which can be integrated into the site at a future date.

### Marketing

The development of the Brandon's Bookstore website took careful consideration of SEO optimisation in its design. The meta tags are incorporated into the base.html and thus featured on every page of the site, and to increase the trustworthiness of the site within search engine algorithms a FAQ page and a customer testimonial carousel were implemented.

Further, the site has been equipped with a Robots.txt and a Sitemap.xml file to enable Google to efficiently trawl and scrape the site.

As per the marking criteria, I have created a dummy Facebook page by editing the provided mock-up via paint.net in order to show what the site's Facebook page may look like if somebody were to create one. I also want to make it known I appreciate the option was given to complete the task this way due to my own misgivings surrounding Facebook and reticence to create any kind of account, even a dummy one for a hypothetical e-commerce site.

![image](https://github.com/BrandonPCollins/project-5-bookshop/assets/131177569/58e1a0f1-92d8-40bd-ba35-8233422d9140)


---


## Deployment

This project was initialised using the [Code Institute Gitpod Full Template](https://github.com/Code-Institute-Org/gitpod-full-template)

### Local Deployment:

1. **Set up Virtual Environment:**
   - Create a virtual environment using virtualenv to isolate the project dependencies.
   - Install required packages such as Django, Gunicorn, and Cloudinary within the virtual environment.

2. **Project Initialization:**
   - Create the project by running `django-admin startproject project_name` inside the virtual environment.
   - Similarly, create the app by running `python3 manage.py startapp app_name`. For this project, two separate apps were created: 'myblog' for handling the Gamesworld blog and 'members' for managing membership and registration.

3. **Database Configuration:**
   - Utilize a database for storing migrations. In this project, Elephant SQL was used under a free tiny turtle plan. Import the database configuration into the project through the `env.py` file.
   - Ensure the connection is operational by pushing migrations to the database and ensuring they have migrated correctly.
  
4. **Cloudinary:**
   - Cloudinary is utilized in this project in this project as online storage for static files such as images users may use as their profile pictures, or as header images for their posts.
   - Set up a free Cloudinary account and add the CLOUDINARY_URL as an environment variable in the env.py file.
   - Hook up Cloudinary in settings.py by configuring STATICFILES_STORAGE, STATICFILES_DIRS, STATIC_ROOT, MEDIA_URL, DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage',

5. **Deployment:**
   -In the ROOT directory create a Procfile containing "web: gunicorn myblog.wsgi"
   -Run pip3 freeze to get the requirements and copy them into a requirements.txt file in the project's main directory.
   
### Heroku Deployment:

1. **Create Heroku App:**
   - Create a new Heroku app and link it to the Git repository for the project under the Deploy tab. If desired enable automatic deployment.

2. **Heroku Configurations:**
   - Set up Heroku Config Vars to account for necessary variables such as Cloudinary URL, the Database URL and the Secret Key. Also, add DISABLE_COLLECTSTATIC with a value of 1 until final deployment.

3. **Cloudinary and Database:**
   - Ensure Cloudinary configurations are set up correctly to handle media files.
   - The database used in this project (Elephant SQL) should be configured in Heroku.

4. **Deployment:**
   - Deploy the project to Heroku by pushing the code to the Heroku remote repository, setting Debug=True to Debug=False in your settings.py before final deployment. Run  heroku run python manage.py migrate to ensure the migrations for the project's models are correctly running on the Heroku app.
   - The project should now be accessible through the provided Heroku app URL.

This deployment process ensures a smooth transition from local development to a live Heroku environment, providing a scalable and accessible platform for users.

### Forking:

1. **Forking on Github:**
   - A user can create a copy of this site to view or alter without affecting the original repository.
   - This is easily done by going to the project's GitHub page with an account, and clicking the "Fork" button on the right side of the page.
   - This will create a copy of the repository within the user's repository.

     
---

## Testing

Testing was accomplished manually via continuous and determined experimentation of functionality on both Desktop and Mobile Phone.

### Manual Testing

The site was tested by using various web browsers including Google Chrome, Edge, and Firefox. Likewise, the site was viewed on various devices such as desktops, laptops, smartphones and tablets.
In order to confirm the successful implementation of the User Stories manual testing was accomplished.

Organised into milestones etc. etc.

### User Stories Testing

i) As a shopper I can view a list of products so that select some to purchase

ii) As a shopper I can view individual product details so that identify the price, description, product rating and product image.

iii) As a shopper I can easily view the total of my purchases at any time so that avoid spending too much

iv) As a shopper I can be presented with featured books so that I can take advantage of offers or limited time pieces with the store's collection

v) As a site user I can easily register for an account so that I can have a personal account and be able to view my profile

vi) As a site user I can easily login and logout of the site so that I can access my personal account information and then logout when I have completed my business on the site

vii) As a site user I can easily recover a lost password so that I can recover access to my personal account

viii) As a site user I can receive a confirmation email after registering so that I can verify that my account registration was successful.

ix) As a site user I can have a personalised user profile so that view my personal order history and order confirmations, and save my payment and checkout information so I am not required to re-enter my details upon every purchase

x) As a shopper I can sort the list of available products so that easily identify the best rated, best price, and categorically sorted products

xi) As a shopper I can sort a specific category of product so that find the best-rated or best-priced product within a specific category or sort the products within that category name

xii) As a shopper I can search for a product by name of description so that find a specific product that I would like to purchase

xiii) As a shopper I can sort multiple categories of product simultaneously so that find the best-priced or best rated products across broad or narrow categories, allowing me to refine m search as a desire

xiv) As a shopper I can easily see what I've searched for and the number of results so that quickly decide whether the product I want is available.

xv) As a shopper I can easily select the quantity of a product while selecting it so that I can easily buy multiple of a product if I desire

xvi) As a shopper I can view the items in my bag to be purchased so that I can identify the total cost of my purchase and inventory all the items I will be receiving.

xvii) As a shopper I can adjust the quantity of individual items in my bag so that I can easily make changes to the number of items I am purchasing in my cart before committing to the purchase.

xviii) As a shopper I can easily enter my payment information so that check out quickly and efficiently with minimal barriers

xix) As a shopper I can feel that my personal and payment information is safe and secure so that I can confidently provide the needed information to make a purchase

xx) As a shopper I can view an order confirmation after checkout so that I can verify that I haven't made any mistakes

xxi) As a shopper I can receive an email confirmation after checking out so that I can keep the confirmation fo what I've purchased for my own records

xxii) As a store owner I can add a product so that add new items to my store

xxiii) As a store owner I can edit and update products so that change product prices, descriptions, images and other information relevant to the product

xxiv) As a store owner I can delete a product so that I can delete products that are no longer for sale

xxv) As a store owner I can display select products on a carousel on the home page so that I can display products I am looking to showcase or those which are more likely to sell to users immediately

xxvi) As a user I can access an FAQ page so that I can have my common and pressing questions answered and addressed

xxvii) As a store owner I can create blog posts to display on the website so that I can create unique posts to inform users of special events, deals or news pertaining to the store.

xxviii) As a store owner I can display user testimonials on the main page so that Google's SEO will view the site as more trustworthy while informing new users that we are a reliable and responsible service.

xxix) As a authenticated user I can comment on the store owner's blog post so that I can express my opinion on the matters being discussed within the post, having my voice heard.

xxx) As an authenticated user I can like comments left by other users on the admin team's blog posts so that I can express my agreement with the sentiment expressed within the comment

xxxi) As a user I can sign up to a newsletter so that I can receive updates pertaining to the site

xxxii) As an autheticated user I can reply to comments left by other users so that I can discuss topics and subjects with them.

xxxiii) As a user I can add rate a product out of 5 stars so that I can inform other users of the quality of that product

### W3C Validator 

HTML was tested with the W3C Markup Validation Service and I fixed the errors which it returned.

![image](https://github.com/BrandonPCollins/project-5-bookshop/assets/131177569/59c4fa61-11e1-4e9c-82d3-c75ae6fb18a2)

![image](https://github.com/BrandonPCollins/project-5-bookshop/assets/131177569/a104055c-b278-405d-8ed0-fcad2d92a7d9)

### CSS

CSS was tested using the W3C CSS Validation Service - Jigsaw and returned no errors.

![image](https://github.com/BrandonPCollins/project-5-bookshop/assets/131177569/14bee55c-3d2d-42c8-beb3-31c4f267ee65)

### Python

Using https://pep8ci.herokuapp.com/ brought to my attention various formatting issues within the code so I used vscode's inbuilt auto-formatter to easily solve the majority of the errors. The ones that remain now are a warning of "missing whitespace around operator" which my auto-formatter was not addressing and doing it manually wouldn't have been worth the time as it has no effect on the functionality of my code.

![image](https://github.com/BrandonPCollins/project-5-bookshop/assets/131177569/9321fef5-77d8-47b9-908f-c73cac59ea60)

### Javascript 

Javascript was tested manually using the console to view the logs when the script was run, and also using https://jshint.com/. All script on the site is functional and fit for purpose.

![image](https://github.com/BrandonPCollins/project-5-bookshop/assets/131177569/b450c495-95c1-46e6-8eec-1109358defb9)

### Lighthouse

Changed the body image from a .jpg to a .webp per Lighthouse's suggestion for superior image compression and thus improved performance. My main issue with Lighthouse is the performance which takes a hit on the products page due to the number of uncompressed images. I'm not entirely sure how to combat this at this current stage in my coding journey.

![image](https://github.com/BrandonPCollins/project-5-bookshop/assets/131177569/c5555629-e3e4-491a-82c1-2c8daf34204b)


### Responsivity

The responsivity of the site was tested using manual screen resizing, viewing the site in various browsers and devices, and through the use of the Responsive Viewer Google Chrome Extension.

---

## Future Features

* Full CRUD Functionality for the sending of Newsletters. Currently, it is performed exclusively through the Administration tab but in a future build having the ability to draft, view and send Newsletters integrated into the website, as the functionality to add Products from the page itself, would be a great feature for future superusers and clients.

* Expansion of the user review system to beyond  just a star rating. Potentially implementing a system of review comments where the user's star rating is logged alongside a text review and then displayed beneath the product, similar to how the comments are displayed beneath the blog posts.

* A way for customers to submit testimonials for display on the carousel at the bottom of the index page and thus allowing them to appear dynamically? {% for testimonial in testimonials %}

* A model for customers to submit their own rare books for appraisal that the site can then offer to either purchase the book from the customer or offer a quote on a restoration service.

* Pagination will be required as the site continues to grow, on both the product and blog listing pages.

---

## Bugs

* There are currently no outstanding bugs that the developers are aware of.
---

## Credits

- Codemy.com's YouTube channel, whose extensive tutorials on Django and Python were instrumental in completing this project. [Codemy.com on YouTube](https://www.youtube.com/@Codemycom) and their [tutorial on building a Django blog](https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi).
- The creators of [Responsive Viewer](https://chromewebstore.google.com/detail/responsive-viewer/inmopeiepgfljkpkidclfgbgbmfcennb?pli=1)
- Pexels for the Placeholder images. Google Image Search for the Images used in my test posts.
- Microsoft Bing Image Creator for the AI generate book covers.
- The endless threads on Stackoverflow
- Slack, my classmates, Muinteor Alan B, Tutor Support, and my Discord friends who actually know how to code for finally getting me over the line.
