![Code Institute Logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Welcome Code Institute Assessor, to Brandon's Bookshop!


[Final Deployment Available Here](https://project-5-books-44675354c311.herokuapp.com/)

---

### Table of Contents

1. [Brandon's Bookshop](#bookshop)
   - [Key Features](#key-features)
      - [News Aggregation and Sorting](#news-aggregation-and-sorting)
      - [User Profiles and Social Connectivity](#user-profiles-and-social-connectivity)
      - [Post Categorization](#post-categorisation)
      - [Content Creation and Management](#content-creation-and-management)
      - [Colour Palette](#colour-palette)
   - [Agile Development Approach](#agile-development-approach)
      - [Dynamic Adaptability and Continuous Improvement](#dynamic-adaptability-and-continuous-improvement)
   - [Deployment](#deployment)
      - [Local Deployment](#local-deployment)
      - [Heroku Deployment](#heroku-deployment)
      - [Forking](#forking)
   - [Features](#features)
      - [Navbar](#navbar)
      - [Post and Comment Functionality](#post-and-comment-functionality)
      - [Post Likes](#post-likes)
      - [User Profiles](#user-profiles)
      - [If-Else Authentication](#if-else-authentication)
   - [Testing](#testing)
      - [W3C Validator](#w3c-validator)
      - [Lighthouse](#lighthouse)
      - [Responsivity](#responsivity)
   - [Future Features](#future-features)
   - [Bugs](#bugs)
   - [Credits](#credits)

# Brandon's Bookshop

![image](https://github.com/BrandonPCollins/project-5-bookshop/assets/131177569/ce5e2dad-bef0-4a86-b256-6e0c10e6ec38)

Brandon's Bookshop offers a comprehensive e-commerce platform where users can browse, search, and purchase rare books online. The platform provides a seamless shopping experience, with intuitive navigation, secure transactions, and a user-friendly interface.

## Key Features

### Full E-Commerce Shopping Site

### Navbar

### Product Categorisation 

### Blog Post Creation and Management

### Comment Functionality

All users can comment on blog posts made by admins, and reply to other users comments, facilitating conversation and discussion.

### Like Functionality

In addition to the ability to comment on posts and reply to other user's comments, users can display their agreement with posts via the like system.

### Newsletters

Brandon's Bookshop offers newsletters to keep users informed about the latest updates, promotions, and events. Newsletter content could include but not be limited to acquisitions of new rare books by the store, important news regarding the store, exclusive offers, potential visits and events featuring famous authors, and more.

![image](https://github.com/BrandonPCollins/project-5-bookshop/assets/131177569/00857f0c-6e61-4bc7-bf87-5552e7636a93)

### Featured Books 

All products have a boolean value which when enabled add them to the featured books carousel on the site's index page. Scrolling carousel allows users to scroll through the books and allows me to know consistently that it will always appear as a single book on the main page no matter how many are added as "featured". Initially I didn't account for this and when I tested it all the featured books stacked on top of each-other leading to an incredibly bloated and long page, and thus made me adopt the carousel approach to featuring the products.  

### User Testimonials

To increase the trustworthiness of our site and thus elevate it within the SEO standings I've included a rotating carousel or User Testimonials at the foot of the home/index page. At the moment it's two static reviews written into the page itself, it serves as good practice in gaining user loyalty and SEO optimisation, and a proof of concept that can be expanded upon to include real and dynamically scripted user experience testimonials in the future.

![image](https://github.com/BrandonPCollins/project-5-bookshop/assets/131177569/7f910b41-5c68-429d-9094-c2b756f19f09)

### About and FAQ Page

Further increase the site's SEO standings.

![image](https://github.com/BrandonPCollins/project-5-bookshop/assets/131177569/f71a1700-8cfa-4f14-9972-a11f384d25aa)


### Favicon

Brandon's Bookshop features a custom favicon for brand recognition and visual identity. The favicon is prominently displayed in browser tabs, bookmarks, and shortcuts, helping users identify the site quickly and easily. Due to my complete lack of artistic talent, the favicon was created using Microsoft Bing Image Generator.

![favicon](https://github.com/BrandonPCollins/project-5-bookshop/assets/131177569/b978047b-9548-4ece-b52d-6c943867d7fa)

### Wireframes

### Colour Palette  

Used coolors.co to generate a colour palette for the site. It was important for me to have a clean black and white as the base for the site's colour schematic, bestowing the site a clean, professional look while calling to mind the simplicity of the written page. Another important aspect was the featuring of an ochre reddish brown colour, one often semantically associated with older books due to the wearing of their leather colours, which the palette generator graciously provided. The other two supplementary colours go unused in the current site's iteration to keep the colour scheme muted, but they complement the ambit well and could easily be integrated in the future.

![image](https://github.com/BrandonPCollins/project-5-bookshop/assets/131177569/8f4f872f-ecfd-43c9-8fce-6cde6ec57a79)

## Agile Development Approach

[Kanban Project Board](https://github.com/users/BrandonPCollins/projects/5)

Issues divided into [milestones](https://github.com/BrandonPCollins/project-5-bookshop/milestones)


## Custom Models
In concordance with the marking criteria, Brandon's Bookshop features several custom models completely distinct from those showcased within

### Rating System

### Admin Blogs

### Comment System & Like Functionality

Full CRUD functionality is implemented in the comment system for users. Create/ Read/ Update/ Delete

### Newsletters

---

## Business Model

---


## Deployment

This project was initialiased using the [Code Institute Gitpod Full Template](https://github.com/Code-Institute-Org/gitpod-full-template)

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


### W3C Validator 

![image](https://github.com/BrandonPCollins/project-5-bookshop/assets/131177569/59c4fa61-11e1-4e9c-82d3-c75ae6fb18a2)

![image](https://github.com/BrandonPCollins/project-5-bookshop/assets/131177569/a104055c-b278-405d-8ed0-fcad2d92a7d9)

### CSS

![image](https://github.com/BrandonPCollins/project-5-bookshop/assets/131177569/14bee55c-3d2d-42c8-beb3-31c4f267ee65)

### Python

Using https://pep8ci.herokuapp.com/ brought to my attention various formatting issues within the code so I used vscode's inbuilt auto-formatter to easily solve the majority of the errors. The ones that remain now are a warning of "missing whitespace around operator" which my auto-formatter was not addressing and doing it manually wouldn't have been worth the time as it has no effect on the functionality of my code.

![image](https://github.com/BrandonPCollins/project-5-bookshop/assets/131177569/9321fef5-77d8-47b9-908f-c73cac59ea60)

### Javascript 

https://jshint.com/

![image](https://github.com/BrandonPCollins/project-5-bookshop/assets/131177569/b450c495-95c1-46e6-8eec-1109358defb9)

### Lighthouse

Changed the body image from a .jpg to a .webp per lighthouse's suggest for superior image compression and thus improve performance.

![image](https://github.com/BrandonPCollins/project-5-bookshop/assets/131177569/c5555629-e3e4-491a-82c1-2c8daf34204b)


### Responsivity

---

## Future Features

* Full CRUD Functionality for the sending of Newsletters. Currently, it is performed exclusively through the Administration tab but in a future build having the ability to draft, view and send Newsletters integrated into the website, as the functionality to add Products from the page itself, would be a great feature for future superusers and clients.

* Expansion of the user review system to beyond  just a star rating. Potentially implementing a system of review comments where the user's star rating is logged alongside a text review and then displayed beneath the product, similar to how the comments are displayed beneath the blog posts.

* A way for customers to submit testimonials for display on the carousel at the bottom of the index page and thus allowing them to appear dynamically? {% for testimonial in testimonials %}

---

## Bugs
---

## Credits

- Codemy.com's YouTube channel, whose extensive tutorials on Django and Python were instrumental in completing this project. [Codemy.com on YouTube](https://www.youtube.com/@Codemycom) and their [tutorial on building a Django blog](https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi).
- The creators of [Responsive Viewer](https://chromewebstore.google.com/detail/responsive-viewer/inmopeiepgfljkpkidclfgbgbmfcennb?pli=1)
- Pexels for the Placeholder images. Google Image Search for the Images used in my test posts.
- Microsoft Bing Image Creator for the AI generate book covers.
- The endless threads on Stackoverflow
- Slack, my classmates, Muinteor Alan B, Tutor Support, and my Discord friends who actually know how to code for finally getting me over the line.
