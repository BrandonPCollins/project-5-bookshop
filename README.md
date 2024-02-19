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
   - [Features](#features)
      - [Navbar Customization](#navbar-customization)
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

An online book retailer blah balh.

## Key Features

### Full E-Commerce Shopping Site

### Post Categorisation 

### Content Creation and Management

### Wireframes



### Colour Palette  

## Agile Development Approach


### Dynamic Adaptability and Continuous Improvement


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
   -Run pip3 freeze to get the requirements and copy them into a requirements.txt file.
### Heroku Deployment:

1. **Create Heroku App:**
   - Create a new Heroku app and link it to the Git repository for the project.

2. **Heroku Configurations:**
   - Set up Heroku Config Vars to account for necessary variables such as Cloudinary URL, the Database URL and the Secret Key. Also, add DISABLE_COLLECTSTATIC with a value of 1 until final deployment.

3. **Cloudinary and Database:**
   - Ensure Cloudinary configurations are set up correctly to handle media files.
   - The database used in this project (Elephant SQL) should be configured in Heroku.

4. **Deployment:**
   - Deploy the project to Heroku by pushing the code to the Heroku remote repository, setting Debug=True to Debug=False before final deployment.
   - The project should now be accessible through the provided Heroku app URL.

This deployment process ensures a smooth transition from local development to a live Heroku environment, providing a scalable and accessible platform for users.

---

## Features

### Navbar Customization

### Post and Comment Functionality

### Newsletters

### Featured Books 

All products have a boolean value which when enabled add them to the featured books carousel on the site's index page. Scrolling carousel allows users to scroll through the books and allows me to know consistently that it will always appear as a single book on the main page no matter how many are added as "featured". Initially I didn't account for this and when I tested it all the featured books stacked on top of each-other leading to an incredibly bloated and long page, and thus made me adopt the carousel approach to featuring the products.  

### User Testimonials

To increase the trustworthiness of our site and thus elevate it within the SEO standings I've included a rotating carousel or User Testimonials at the foot of the home/index page. At the moment it's two static reviews written into the page itself, it serves as good practice in gaining user loyalty and SEO optimisation, and a proof of concept that can be expanded upon to include real and dynamically scripted user experience testimonials in the future.

### Favicon

Used Microsoft Bing Image Generator to create a favicon for the site

![favicon](https://github.com/BrandonPCollins/project-5-bookshop/assets/131177569/b978047b-9548-4ece-b52d-6c943867d7fa)


---

## Custom Models
In concordance with the marking criteria, Brandon's Bookshop features several custom models completely distinct from those showcased within

### Rating System

### Admin Blogs

### Comment System

Full CRUD functionality is implemented in the comment system for users. Create/ Read/ Update/ Delete

### Newsletters

---

## Testing

Testing was accomplished manually via continuous and determined experimentation of functionality on both Desktop and Mobile Phone.

python3 manage.py test name-of-app 

coverage run --source=name-of-app manage.py test

coverage report

coverage html

python3 -m http.server



### W3C Validator 

### CSS

https://jigsaw.w3.org/css-validator/

### Python

https://pep8ci.herokuapp.com/

### Javascript 

https://jshint.com/

### Lighthouse

### Responsivity

---

## Future Features

* Full CRUD Functionality for the sending of Newsletters. Currently, it is performed exclusively through Administration tab but in a future build having the ability to draft, view and send Newsletters integrated into the website, as the functionality to add Products from the page itself, would be a great feature for future superusers and clients.

* The adding of a pdf selection to the products model allowing users to choose between the purchase of physical or pdf versions of their purchases, which will then be sent to their email.

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
