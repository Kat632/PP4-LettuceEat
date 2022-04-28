# Lettuce Eat

![Lettuce Eat - Responsive](#)

[View the live project here](https://lettuce-eat-pp4.herokuapp.com/ "Link to deployed site - Lettuce Eat")

## Table of contents
1. [Introduction](#Introduction)
2. [UX](#UX)
    1. [User Stories](#User-Stories)
    2. [Development Planes](#Development-Planes)
    3. [Design](#Design)
3. [Features](#Features)
    1. [Design Features](#Design-Features) 
    2. [Existing Features](#Existing-Features)
    3. [Features to Implement in the future](#Features-to-Implement-in-the-future)
4. [Issues and Bugs](#Issues-and-Bugs)
5. [Technologies Used](#Technologies-Used)
     1. [Main Languages Used](#Main-Languages-Used)
     2. [Additional Languages Used](#Additional-Languages-Used)
     3. [Frameworks, Libraries & Programs Used](#Frameworks,-Libraries-&-Programs-Used)
6. [Testing](#Testing)
     1. [Testing.md](TESTING.md)
7. [Deployment](#Deployment)
     1. [Deploying on Heroku](#Deploying-on-Heroku)
     2. [Forking the Repository](#Forking-the-Repository)
     3. [Creating a Clone](#Creating-a-Clone)
8. [Credits](#Credits)
     1. [Content](#Content)
     2. [Media](#Media)
     3. [Code](#Code)
9. [Acknowledgements](#Acknowledgements)
***

## Introduction

This is the fourth of five Portfolio Projects that I must complete during my Full Stack Software Development program with Code Institute.

This was not the website that I intended to make for my fourth project, but I abandoned my first project with less than three weeks to go, in order to build something simpler, that I knew I could deliver on time.

The main requirements of this project were to build a Full Stack site based on business logic used to control a centrally-owned dataset. This also requires the developer to set up an authentication mechanism and provide role-based access to the site's data or other activities based on the dataset.

My project is a recipe blog dedicated to salad, called Lettuce Eat.  Users can register themselves in order to comment and like recipes.  They can also create their own recipes and upload images of their recipes.  A user can edit their own recipes, as well as delete them.  

[Back to top ⇧](#Lettuce-Eat)

## UX 

### User Stories
#### Users:
1.  As a **user**, I can **view a summary page of recipes** so that **I can easily see if there is a recipe that I would like to view in more detail**.

2.  As a **user** I can **click on a recipe to open it** so that **I can see the full list of ingredients and the instructions**.

3.  As a **user** I can **view the number of likes a recipe has** so that **I can have an idea of what people think about it before I try it**.

4.  As a **user** I can **view comments that other user's have made about a recipe** so that **I can see what others think of it and maybe pick up some ideas or tips**.

5.  As a **user** I can **create my own account** so that **I can comment and like recipes**.

6.  As a **user** I can **navigate around the site** so that **I can choose the things I want to read**.

7.  As a **logged-in user** I can **submit my own recipes** so that **I can share them on the site too**.

8.  As a **logged-in user** I can **leave a comment on a recipe so that I can share my thoughts and results with other people**.

9.  As a **logged-in user** I can **like or unlike a recipe** so that **I can help other users to find out if a recipe is popular**.

10. As a **logged-in user** I can **click a button** so that **I can edit a recipe I have previously submitted**.

11. As a **logged-in user** I can **click a button** so that **I can delete a recipe I have previously submitted**.

#### Site Admin:
1. As a **Site Admin**, I can **create, read, update and delete recipes** so that **I can manage my site content**.

2. As a **Site Admin**, I can **save my posts to draft** so that **I can come back and finish them later**.

3. As a **Site Admin** I can **approve or deny comments that have been left by other people before they are published** so that **I can filter out unwanted or irrelevant comments**.

### Development Planes
To create a comprehensive and appealing website, I researched other recipe based websites to discover what features and functionality would be required. This information created the above user stories and is developed further below.

#### Strategy
Broken into three categories, the website will attempt to focus on the following target audiences:
- **Roles:**
     - User
     - Admin

- **Demographic:**
     - Health conscious people
     - People looking for a more creative salad
     - Cooking enthusiasts
     - People who are curious about salad, but don't know where to start

- **Psychographics:**
     - Personality & Attitudes:
        - Creative
	     - Healthy

     - Values:
        - Interested in trying different things
     - Lifestyles:
        - Anyone interested in healthy, homemade food

The website needs to enable the **user** to:
- browse the recipes.
- comment on and like recipes.
- register and log in to enable them to upload their recipes.

The website needs to enable the **admin** to:
- approve recipe uploads and comments.
- create drafts so they can be completed later.

With the user stories in mind, I created the below strategy table to determine the trade-off of importance and viability with the following results:

![Strategy Table](static/site_images/readme/strategy.png 'Strategy Table')

#### Scope
A scope was defined to identify what needed to be done to align features with the strategy previously defined. This was broken into two categories:
- **Content Requirements**
     - The user will be looking for:
        - a comprehensive list of recipes.
	    - a comprehensive list of ingredients and steps to follow.
	    - a list of comments about others' attempts to replicate the meal on each recipe page.

- **Functionality Requirements**
     - The user will be able to:
        - Easily navigate the site to find the information they want.
	    - Be able to select recipes they wish to try.
	    - Comment on and like recipes.

#### Structure
The information architecture was organized in such a way as to ensure that users can navigate through the site easily.
![Site Map structure](static/site_images/readme/sitemap_p4.png 'Site Map')

Entity Relationship Diagram for the database models.
![ERD structure](static/site_images/readme/erd_lettuce_eat.png 'Entity Relationship Diagram')

#### Skeleton 
Wireframe mockups were created using [Balsamiq](https://balsamiq.com/ 'Balsamiq Website').

Home Page:
![Home Page Wireframe](static/site_images/readme/home.png 'Home Page - Wireframe')

About Page:
![About Page Wireframe](static/site_images/readme/about.png 'About Page - Wireframe')

Recipe Page:
![Recipe Page Wireframe](static/site_images/readme/recipe_view.png 'Recipe Page - Wireframe')

Create/Edit Recipe Page:
![Create/Edit Recipe Page Wireframe](static/site_images/readme/create.png 'Create/Edit Recipe Page - Wireframe')

### Design

#### Colour Scheme
I chose to use a clean white background, using green for the typography and flashes of orange, yellow and red which are typical salad colours.  I wanted the website to look fresh and convey a healthy feeling.

The white background allows the colours in the recipe images to look bright, appetising and attractive.

#### Logo
The Lettuce Eat logo was made with [Canva](https://www.canva.com/ 'Canva website').  I liked it because it depicts cooking implements.  I made it green to match the rest of the colour scheme and used Dancing Script to match the typography (see Typography below).

#### Typography

The font chosen for the logo was Dancing Script as it is elegant and classic.  The font has also been used throughout the website for sub-headings, to add some differentiation from the main font of the site. All instances of Dancing Script have also been styled green to make them stand out against the white background of the site.

The main font of the website is Poppins, which has been used for large headings, as well as all other text.  Poppins is a popular, versatile font and it ensures that the most important information on the site is readable.

Both fonts were chosen from [Google Fonts](https://fonts.google.com/ 'Google Fonts website')

#### Imagery
To match the colour scheme chosen, I chose an image of heads of lettuce for the hero image on the index page.  The site is called Lettuce Eat and therefore I didn't want to put a big image of a salad.  If the salad had ingredients in it that a user didn't like, there would be the potential of the user closing the site before scrolling down to the recipes.  That's why I thought it would be more fun to use the lettuce and have it tie in with the site name.

On each recipe page, an image of the finished meal is shown with the recipe to allow the user to visualise the end product.

All of the recipe images are from [Pixabay](https://pixabay.com/ 'Pixabay website').
The header image is from [Unsplash](https://unsplash.com/ 'Unsplash website').

[Back to top ⇧](#Lettuce-Eat)

## Features

### Design Features
Each page of the website features a consistent responsive navigational system:

- The **Header** contains a conventionally placed logo in the top left of the page (whereby clicking this will redirect users back to the home page) and a navigation bar in the centre of the header. On smaller screens, the navigation bar condenses into a dropdown with navigation options.

- There is a **Header Image** on most pages, depicting a selection of ingredients and utensils on a dark background. This image is used to keep the theme consistent and is only missing in the recipe pages where the focus is instead brought to an image of the recipe itself, or a placeholder if none is provided.

- The **Footer** is divided into five sections, four columns and a bottom row. The first column contains a short blurb, telling the user about the site. The second contains useful links to utensil shopping, budgeting ideas and more. The third has navigation links to the Student Rations site. The fourth has a list of contact information. Finally, the bottom row contains social links and copyright information. On smaller screens, this condenses into a single column, with each section moving underneath its neighbour on the left.

<dl>
  <dt><a href="https://student-rations.herokuapp.com/" target="_blank" alt="Home Page">Home Page</a></dt>
  <dd>The Home Page is laid out with a nav section on top, an image below the width of the screen, the content area containing the recipe cards, followed by the footer. The features are as follows:
     <ul>
          <li><strong>A Welcome Note or Login Request</strong> - On the home screen you will see, below the header image, either a request to log in or register to the site or a heading welcoming the user to the site, citing the user's username.
          </li>
          <li><strong>Recipe Cards</strong> - The main content has recipe cards that are four cards across on large screens, two across on medium screens and one across on small screens. This is paginated by eight so anything more than eight cards will be shown on the next page.
          </li>
          <li><strong>Next/Prev Page Link</strong> - If more than eight recipes are available, the remainder will be shown on the next page, with a max of eight cards on each of the following pages. To access these, there is a Next or Prev link that shows underneath the recipe cards.
          </li>
     </ul>
  </dd>

  <dt><a href="https://student-rations.herokuapp.com/about/" target="_blank" alt="About Page">About Page</a></dt>
  <dd>The about page shows a brief overview of the developer and their story:
     <ul>
          <li><strong>Content</strong> - There is information about the developer and their story on this page.
          </li>
     </ul>
  </dd>

  <dt><a href="https://student-rations.herokuapp.com/creamy-courgette-lasagne/" target="_blank" alt="Recipe Page - Creamy courgette lasagne">Recipe Page</a></dt>
  <dd>This page shows the details of each recipe. This page does not contain a header image but is instead divided into two sections on top, followed by a single column section and commenting section underneath. The features are as follows:
     <ul>
          <li><strong>Featured Image</strong> - The featured image shows the image the user uploaded, or the placeholder image if no image was uploaded by the user.
          </li>
          <li><strong>Like/Unlike Button</strong> - If the user is logged in, the like/unlike button will appear green and will allow the user to like the recipe. If they have already liked the recipe, clicking the button will remove the like.
          </li>
          <li><strong>Edit/Delete Buttons</strong> - If the user is logged in and is the author of the said recipe, clicking the edit button will bring the user to the edit page. The recipe details are populated into the form and the user can edit the information, upload a new image and save the information. Alternatively, clicking the delete button removes the recipe from the database and redirects the user back to the home page.
          </li>
          <li><strong>Comment Feature</strong> - If the user is logged in, the comment form is visible under the recipe on the right of the page. Entering a comment and submitting will then cause the form to disappear and a message will show advising the comment is awaiting approval. On approval, comments are displayed under the recipe on the left of the page, showing the user's name and date and time of commenting.
          </li>
     </ul>
  </dd>

  <dt><a href="https://student-rations.herokuapp.com/edit-a-recipe/creamy-courgette-lasagne" target="_blank" alt="Edit Recipe Page - Creamy courgette lasagne">Edit Recipe Page</a></dt>
  <dd>This page shows the form populated with the specific recipe's information which can be saved and edited:
     <ul>
          <li><strong>Edit Recipe Form</strong> - The form is prepopulated with all the recipe information. The user can edit this information, only if they are the author of the recipe. Saving this recipe redirects the user to the home page where they can then view the recipe list.
          </li>
     </ul>
  </dd>

  <dt><a href="https://student-rations.herokuapp.com/share-a-recipe/" target="_blank" alt="Share a Recipe Page">Share a Recipe Page</a></dt>
  <dd>This page has a form that allows the user to add a recipe, as well as upload an image:
     <ul>
          <li><strong>Share a Recipe Form</strong> - An empty form is displayed, allowing the user to enter the recipe details, as well as upload an image of the recipe. If no image is uploaded, the placeholder image is saved instead. Saving this recipe redirects the user to the home page where they can then view the recipe list.
          </li>
     </ul>
  </dd>

  <dt><a href="https://student-rations.herokuapp.com/accounts/login/" target="_blank" alt="Sign In Page">Sign In Page</a></dt>
  <dd>This page has a form allowing the user to enter their username and password to log in:
     <ul>
          <li><strong>Sign In Form</strong> - This form has two input fields, for the username and the password. A submit button at the end of the form login the user in, if the information was correct, and redirects the user to the home page.
          </li>
     </ul>
  </dd>
  
  <dt><a href="https://student-rations.herokuapp.com/accounts/logout/" target="_blank" alt="Sign Out Page">Sign Out Page</a></dt>
  <dd>The :
     <ul>
          <li><strong>Sign Out Button</strong> - This page asks the user if they are sure they want to log out. Clicking the Sign Out button will log the user out and redirect them to the home page.
          </li>
     </ul>
  </dd>
  
  <dt><a href="https://student-rations.herokuapp.com/accounts/signup/" target="_blank" alt="Sign Up Page">Sign Up Page</a></dt>
  <dd>This page has a form allowing the user to enter their username, email and password to register an account:
     <ul>
          <li><strong>Sign In Form</strong> - This form has four input fields, for the username, email address (optional), the password and repeat the same password. A submit button at the end of the form login the user in if the information was correct and has not been used by other users previously, and redirects the user to the home page.
          </li>
     </ul>
  </dd>
</dl>
 
### Existing Features
- **Header Logo** - Appearing on every page for brand recognition. Clicking the logo will return the users to the home page, as expected.
- **Header Navigation Bar** - Appearing on every page for a consistently easy and intuitive navigable system.
- **Header Image** - Appearing on almost every page, the image gives a consistent theme and style throughout the site.
- **Social Icons** - Appearing on every page, the icons are appropriate representations of the Social Media platforms, found in the footer.
- **Recipe Cards** - Appearing on the home page, the recipe cards give a brief overview of the recipe, showing the image, description, servings, prep and cook time, and the number of likes on the recipe.
- **Recipe Form** - Appearing on the share a recipe page and edit recipe page, the form allows the user to add or edit a recipe, including adding an image to display on the recipe page and recipe card.
- **Comment Form** - Appearing on the recipe page, the form submits the user's comment to be approved by the admin.
- **Comments Section** - Appearing on the recipe page, approved comments are displayed showing the author's username and the date and time of submission.
- **Like/Unlike Button** - Appearing on the recipe page when the user is logged in, the button allows the user to like or unlike a recipe. If the user is not logged in, they will simply see the number of likes on the page.
- **Home Page** - A home page that shows the user the site's available recipes, shown as recipe cards and paginated by eight. There is a next/prev button under the recipes allowing the user to explore all recipes. In addition, if the user is logged in, a welcome message appears on the home page with the user's username. Otherwise, a short message recommending the user logs in or registers an account is shown.
- **About Page** - An About Page gives the user information about the developer and their story.
- **Recipe Page** - A recipe page whose content changes with the recipe details of the chosen recipe. Includes features to like and comment as well as edit or delete.
- **Add/Edit Recipe Page** - A page designed to allow the user to add a recipe if logged in, and edit a recipe if they are logged in as the recipe's author. 
- **Sign In Page** - A page designed to allow the user to log in using previously created user details; a username and a password.
- **Sign Up Page** - A page designed to allow the user to create a user profile using a username, optional email address and a password that needs to be repeated to ensure it is correct.
- **Sign Out Page** - A page designed to confirm the user wishes to log out of their account. If the user clicks the sign out button, they are then redirected to the home page.

### Features to Implement in the future
- **Favourites Page**
     - **Feature** - This feature would have been used to display all the recipes a user would have liked so the user could find them easier.
     - **Reason for not featuring in this release** - The reason for not releasing this feature was that the developer ran out of time to implement the feature before the project's due date. This will be developed further in the future after grading is complete.
- **Sharing Images in Comments**
     - **Feature** - This feature would have allowed users to upload images of their attempts at the recipes in the comments section next to their comment.
     - **Reason for not featuring in this release** - Again, the developer ran out of time to implement this feature before the project's due date. This will also be developed further in the future after grading is complete.
- **Saving Drafts to a Profile Page**
     - **Feature** - This feature would have allowed users to create a draft of a recipe which would be saved on a profile page which would allow them to complete the draft at a later date and release the recipe onto the site.
     - **Reason for not featuring in this release** - Once again, the developer ran out of time to implement this feature before the project's due date. This will also be developed further in the future after grading is complete.
- **Search Recipes**
     - **Feature** - This feature would have allowed users to search recipes, either by typing the name of a recipe, or searching for a specific category of recipes e.g. Vegan.
     - **Reason for not featuring in this release** - Once again, the developer ran out of time to implement this feature before the project's due date. This will also be developed further in the future after grading is complete.
- **Categorise Recpies**
     - **Feature** - Recipes could be organised into categories, thus enabling users to search by categories.
     - **Reason for not featuring in this release** - In hindsight, this would have been very easy to implement at the beginning of the project when I was designing the models.  I will include this in the future, after grading is complete.

 
[Back to top ⇧](#Lettuce-Eat)

## Issues and Bugs 

**Bug** - I initially thought that since Summernote worked on the admin page, it would work on the main site also. Once I had implemented the form to add a recipe, it became apparent that I needed to find a solution to allow the user to create ordered and unordered lists for steps and ingredients.  Without this feature, the recipes would appear as an unformatted block of text. 
- ***Solution***: I looked at all the Summernote documentation on both their site and GitHub page. The Summernote text fields appeared on the create and edit recipe pages, but then the recipe would not save.  After discussing the issue with Andrew Dempsey, we discovered that the Summernote documentation was lacking in information, focussing mostly on admin implementation. The relevant code that I needed to put in was at the bottom of Summernote's readme on GitHub, in a section called 'Options'.  I worked through the information regarding settings and the forms then began to work correctly and the text is now able to be styled by the user.

**Bug** - I discovered that if a user tried to register with an email address, it would throw a Connection Refused Error, but a user was still able to log in anyway.
- ***Solution***: I checked for similar problems on the Code Institute Slack, and I also asked fellow student Patrik Osterljung who I know had a similar problem with his Project 4.  I needed to make some adjustments to my settings.py file.  Notably, ACCOUNT_EMAIL_VERIFICATION = 'none' allowed it to work.

**Issue** - The developer found while validating the site's html that the Summernote feature implemented in the forms threw up a large number of errors. Unfortunately this is not something the developer was able to rectify and as such was left in the code. It will be noted that these errors were not caused by the developer and as such should hopefully not count toward the final grade.

**Issue** - The developer found errors when validating the python files. This was found in the settings.py file where certain urls went beyond the character limit on a single line. This error can be ignored as there is no way to reduce the url length to conform to the character limit per line.

[Back to top ⇧](#Lettuce-Eat)

## Technologies Used
### Main Languages Used
- [HTML5](https://en.wikipedia.org/wiki/HTML5 "Link to HTML Wiki")
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets "Link to CSS Wiki")

### Additional Languages Used
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript "Link to JavaScript Wiki")
     - Used to implement the Summernote feature that allowed the user to add styling to the recipe in the form.
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language) "Link to Python Wiki")
     - Used to implement Django functionality, including building models, forms and views for the app.

### Frameworks, Libraries & Programs Used
- [Django](https://www.djangoproject.com/ "Link to Django Project website")
    - Django was used to build the models, forms and views of the app, and was the backbone of this project.
- [Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/ "Link to Bootstrap page")
     - Bootstrap was used to implement the responsiveness of the site, using bootstrap classes.
- [Cloudinary](https://cloudinary.com/ "Link to Cloudinary page")
     - Cloudinary was used as free cloud storage for images uploaded to the site through the recipe forms.
- [Summernote](https://summernote.org "Link to Summernote page")
     - Summernote was used to allow users to add styling when adding a recipe to the site. This is particularly useful for using bullet points for ingredients or numbering the steps for the recipe.
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/ "Link to the Crispy Forms documentation.
    - Crispy Forms was used to style the add and edit recipe forms, allowing more than one field to occupy a line on the form.
- [Google Fonts](https://fonts.google.com/ "Link to Google Fonts")
    - Google fonts were used to import the fonts "Roboto" and "Open Sans" into the style.css file. These fonts were used throughout the project.
- [Font Awesome](https://fontawesome.com/ "Link to FontAwesome")
     - Font Awesome was used on all pages throughout the website to import icons (e.g. social media icons) for UX purposes.
- [Git](https://git-scm.com/ "Link to Git homepage")
     - Git was used for version control by utilizing the GitPod terminal to commit to Git and push to GitHub.
- [GitHub](https://github.com/ "Link to GitHub")
     - GitHub was used to store the project after pushing
- [Am I Responsive?](http://ami.responsivedesign.is/# "Link to Am I Responsive Homepage")
     - Am I Responsive was used to see responsive design throughout the process and to generate mockup imagery to be used.

[Back to top ⇧](#Lettuce-Eat)

## Testing

Testing information can be found in a separate [testing file](TESTING.md "Link to testing file").

## Deployment

This project was developed using a [GitPod](https://gitpod.io/ "Link ot GitPod") workspace. The code was commited to [Git](https://git-scm.com/ "Link to Git") and pushed to [GitHub](https://github.com/ "Link to GitHub") using the terminal.

### Deploying on Heroku
To deploy this page to Heroku from its GitHub repository, the following steps were taken:

1. Create the Heroku App:
    - Select "Create new app" in Heroku.
    - Choose a name for your app and select the location.

2. Attach the Postgres database:
    - In the Resources tab, under add-ons, type in Postgres and select the Heroku Postgres option.

3. Prepare the environment and settings.py file:
    - In the Settings tab, click on Reveal Config Vars and copy the url next to DATABASE_URL.
    - In your GitPod workspace, create an env.py file in the main directory. 
    - Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
    - Add the SECRET_KEY value to the Config Vars in Heroku.
    - Update the settings.py file to import the env file and add the SECRETKEY and DATABASE_URL file paths.
    - Update the Config Vars with the Cloudinary url, adding into the settings.py file also.
    - In settings.py add the following sections:
        - Cloudinary to the INSTALLED_APPS list
        - STATICFILE_STORAGE
        - STATICFILES_DIRS
        - STATIC_ROOT
        - MEDIA_URL
        - DEFAULT_FILE_STORAGE
        - TEMPLATES_DIR
        - Update DIRS in TEMPLATES with TEMPLATES_DIR
        - Update ALLOWED_HOSTS with ['app_name.heroku.com', 'localhost']

4. Store Static and Media files in Cloudinary and Deploy to Heroku:
    - Create three directories in the main directory; media, storage and templates.
    - Create a file named "Procfile" in the main directory and add the following:
        - web: gunicorn project-name.wsgi
    - Go to Deploy tab on Heroku and connect to the GitHub, then to the required recpository.
    Click on Delpoy Branch and wait for the build to load. When the build is complete, the app can be opened through Heroku.


### Forking the Repository
By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log into [GitHub](https://github.com/login "Link to GitHub login page") or [create an account](https://github.com/join "Link to GitHub create account page").
2. Locate the [GitHub Repository](https://github.com/rebeccatraceyt/KryanLive "Link to GitHub Repo").
3. At the top of the repository, on the right side of the page, select "Fork"
4. You should now have a copy of the original repository in your GitHub account.

### Creating a Clone
How to run this project locally:
1. Install the [GitPod Browser](https://www.gitpod.io/docs/browser-extension/ "Link to Gitpod Browser extension download") Extension for Chrome.
2. After installation, restart the browser.
3. Log into [GitHub](https://github.com/login "Link to GitHub login page") or [create an account](https://github.com/join "Link to GitHub create account page").
2. Locate the [GitHub Repository](https://github.com/rebeccatraceyt/KryanLive "Link to GitHub Repo").
5. Click the green "GitPod" button in the top right corner of the repository.
This will trigger a new gitPod workspace to be created from the code in github where you can work locally.

How to run this project within a local IDE, such as VSCode:

1. Log into [GitHub](https://github.com/login "Link to GitHub login page") or [create an account](https://github.com/join "Link to GitHub create account page").
2. Locate the [GitHub Repository](repo url "Link to GitHub Repo").
3. Under the repository name, click "Clone or download".
4. In the Clone with HTTPs section, copy the clone URL for the repository.
5. In your local IDE open the terminal.
6. Change the current working directory to the location where you want the cloned directory to be made.
7. Type 'git clone', and then paste the URL you copied in Step 3.
```
git clone https://github.com/USERNAME/REPOSITORY
```
8. Press Enter. Your local clone will be created.

Further reading and troubleshooting on cloning a repository from GitHub [here](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository "Link to GitHub troubleshooting")

**UPDATE**


[Back to top ⇧](#Lettuce-Eat)

## Credits 

### Content
- Most recipes were taken from [BBC GoodFood](https://www.bbcgoodfood.com/ "Link BBC GoodFood website")'. The Aussie Christmas Salad was taken from [Love My Salad](https://www.lovemysalad.com/ "Link to Love My Salad website").  The Fig Salad recipe was taken from [Striped Spatula](https://stripedspatula.com/ "Link to the Striped Spatula website").

- The Fun Facts about Salad on the About page, plus the quote were taken from [Love My Salad](https://www.lovemysalad.com/ "Link to Love my Salad website").

### Media
- The images have been sourced from the [Pixabay](https://pixabay.com/) by the developer.  It was quite difficult to find free pictures of salad that fit with the recipes I wanted to include.

### Code 
References used:
- [Stack Overflow](https://stackoverflow.com/ "Link to Stack Overflow page")
- [Bootstrap](https://getbootstrap.com/ "Link to BootStrap page")
- [Colorlib](https://colorlib.com/ "Link to Colorlib page")
- [Django Docs](https://docs.djangoproject.com/en/3.2/ "Link to Django's Docs for Version 3.2")
- [Summernote GitHub Docs](https://github.com/summernote/summernote, "Link to Summernote's GitHub page")
- [Cripsy Forms Docs](https://django-crispy-forms.readthedocs.io/en/latest/ "Link to Crispy Forms documentation")

### Other
- [Visio](https://www.microsoft.com/en-gb/microsoft-365/visio/flowchart-software "Link to Visio on Microsoft's website")
     - Visio was used for the diagrams in this Readme document.

[Back to top ⇧](#Lettuce-Eat)

## Acknowledgements

- I would like to thank my husband for putting up with me during the process of design and development.  He makes sure I am fed, watered and taking regular breaks.
- I would also like to thank Andrew Dempsey, for his invaluable help and guidance in getting Summernote to work with my forms.
- Finally, I would like to thank the rest of my August 2021 Hackathon team - Helena, Patrik and Yorick.

[Back to top ⇧](#Lettuce-Eat)

***
