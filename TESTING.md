# Lettuce Eat - Testing 

[Main README.md file](/README.md)

[View live project](https://lettuce-eat-pp4.herokuapp.com/)

[View GitHub repository](https://github.com/Kat632/PP4-LettuceEat)

***
## Table of contents
1. [Testing User Stories](#Testing-User-Stories)
2. [Manual Testing](#Manual-Testing)
3. [Automated Testing](#Automated-Testing) 
     - [Code Validation](#Code-Validation)
     - [Browser Validation](#Browser-Validation)
4. [User Testing](#User-Testing)


***

## Testing User Stories

#### User Stories:
1. As a **user**, I can **view a summary page of recipes** so that **I can easily see if there is a recipe that I would like to view in more detail**.
  
    - The list of recipes on the home page has been paginated by eight. If there are more than eight recipes, the remainder moves to the next page. This will continue until there are eight or less recipe cards on the one page.

2. As a **user** I can **click on a recipe to open it** so that **I can see the full list of ingredients and the instructions**.
    
    - On each recipe card is a brief overview of the recipe and a button that, when clicked, redirects the user to the recipe page where they can see a full list of ingredients and the method to make the recipe.

3. As a **user** I can **view the number of likes a recipe has** so that **I can have an idea of what people think about it before I try it**.

    - On the recipe cards, the total number of likes on the recipe is displayed. This is also shown on the recipe page itself.

4. As a **user** I can **view comments that other user's have made about a recipe** so that **I can see what others think of it and maybe pick up some ideas or tips**.

    - A comments section has been added to the recipe pages, showing the author's username and the date/time the comment was left.

5. As a **user** I can **create my own account** so that **I can comment and like recipes**.

    - There is a sign in and sign up option, which advises the user on the home page to log in to access certain content. The user will be required to be signed in to access protected content, such as the like and comment features.

6. As a **user** I can **navigate around the site** so that **I can choose the things I want to read**.

    - The navigation bar is visible at the top of every page and there are navigation links in the footer at the bottom of every page. 

7. As a **logged-in user** I can **submit my own recipes** so that **I can share them on the site too**.

    - If the user is logged in, they can navigate to the Add Recipe page and fill in the form to add their own recipe.  If they are not logged in, they are given the option to log in or register.

8. As a **logged-in user** I can **leave a comment on a recipe so that I can share my thoughts and results with other people**.

    - The field to leave a comment is at the bottom of the Recipe Detail page.  Once the user submits a comment, the comment will need to be approved by the admin to then be displayed on the site.

9. As a **logged-in user** I can **like or unlike a recipe** so that **I can help other users to find out if a recipe is popular**.

    - If the user is logged in, the user will be able to like or remove their like from the recipe. The number of likes is automatically incremented and the change is visible both on the recipe page and the recipe card on the home page.

10. As a **logged-in user** I can **click a button** so that **I can edit a recipe I have previously submitted**.

    - When a user is logged in, they will be able to see two buttons on the Recipe Detail page if they are the author of the recipe.  Clicking the green "Edit" button will take the user to the Edit Recipe page where they can amend their recipe and re-submit it to the site.

11. As a **logged-in user** I can **click a button** so that **I can delete a recipe I have previously submitted**.

    - When a user is logged in, they will be able to see two buttons on the Recipe Detail page if they are the author of the recipe.  Clicking the red "Delete" button will delete the user's recipe.

[Back to top](#Lettuce-Eat---Testing)

## Manual Testing

### Common Elements Testing
Manual testing was conducted on the following elements that appear on every page:

- Test that Logo redirects to home screen.

- Test that Nav Links work.

- Test that Footer Links work.

- Test that Social Links work and open in a new page.

### Home Page
Manual testing was conducted on the following elements of the [Home Page](https://lettuce-eat-pp4.herokuapp.com/):
     
- Test that user welcome message displays username.

    - On logging in, there is a message alert at the top of the Home page which tells the user that they have successfully logged in.
    - Further down the Home page, there is a message which welcomes the user (by name) back to the site.

- Test that recipe cards redirect user to recipe pages.

    - The green View Recipe button at the bottom of each recipe card redirects the user to the Recipe Detail page for the recipe they have clicked on.

### Recipe Page/Edit Recipe Page
Manual testing was conducted on the following elements of the [Recipe Page](https://lettuce-eat-pp4.herokuapp.com/fig-and-goats-cheese-salad/) and [Edit Recipe Page](https://lettuce-eat-pp4.herokuapp.com/edit-recipe/fig-and-goats-cheese-salad):

- Test that recipes can be edited by author only.

- Test that recipes can only be deleted by author.

- Test that a warning is given before a user deletes a recipe.
     
- Test that recipes can be liked and unliked when logged in.
     
- Test that comments can be submitted and approved.

### Share Recipe Page
Manual testing was conducted on the following elements of the [Add Recipe Page](https://lettuce-eat-pp4.herokuapp.com/add-recipe/):

- Test that recipes create unique slugs, based on the title of the recipe.

- Test that recipes with the same title will throw an error and ask the user to rename the recipe to something unique.

- Test that recipes with an unrealistic prep or cook time will throw an error.
     
- Test that recipes are saved.
     
### Sign in/Sign Out/Sign Up Pages
Manual testing was conducted on the following elements of the [Sign In Page](https://lettuce-eat-pp4.herokuapp.com/accounts/login/), [Sign Out Page](https://lettuce-eat-pp4.herokuapp.com/accounts/logout/) and [Sign Up Page](https://lettuce-eat-pp4.herokuapp.com/accounts/signup/):

- Users can register, log in and logout.

### Pages are Responsive
- Manual testing was conducted for responsiveness on large, medium and small screens.

[Back to top](#Lettuce-Eat---Testing)

## Automated Testing

### Code Validation
The [W3C Markup Validator](https://validator.w3.org/ "Link to M£C Markup Validator Site") service was used to validate the `HTML` and `CSS` code used. The [PEP8 Python Validator](http://pep8online.com/ "Link to the PEP8 Python Validator Site") was used to validate the `Python` code used.

**Results:**

- HTML Pages - Code Validation

HTML validation - all pages clear.

- CSS stylesheet - Code Validation

CSS tested clear.

- Python Files - Code Validation

**Files tested**

lettuceeat - urls.py

lettuceeat - settings.py

blog - admin.py

blog - forms.py

blog - models.py

blog - urls.py

blog - views.py

All files tested clear.

### Browser Validation
- Chrome
- Edge
- Opera
- Firefox

## User testing 
My husband and the lovely people of Slack were asked to review the site and documentation to point out any bugs and/or user experience issues. Their helpful advice throughout the process led to a few small UX changes in order to create a better experience. 

[Back to top ⇧](#Lettuce-Eat---Testing)

***