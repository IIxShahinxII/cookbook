
# EasyCook

## Data Centric Development Milestone Project-3

## Description

The EasyCook is an online cookbook, where a user can find recipes or share his/her recipes. User has the possibility of add, edit or delete all recipes.

# UX

### Target Audience

 The target audience of this web-application are people who are either in search of good cooking recipes or they want to share their recipes with the rest of the world. Besides, the web-application owner's goal is to create a cooking recipes database.

### Project Suitability

This project is suitable to perform **CRUD** operations;
- User has the ability to add, view and search for recipes in the database.
- User has the ability to edit or delete recipes.
- User can see recipes.

 ### User Stories

 1. As a user, I want to see a list of recipes.
 2. As a user, I want to search for recipes so that I can find recipes easily and quickly.
 3. AS a user, I want to store/add and share my recipes online with others.
 4. As a user, I want to see the details of the recipe.
 5. As a user, I want to edit existing recipes.
 6. As a user, I want to delete existing recipes.

 ## Design

 The website design is simple and responsive which allows the user to perform easily the CRUD functionality. The design
 inspiration is taken from the **Code Institute's Task Manager Mini Project**.

## Wireframes

I used [AdobeXD](https://creativecloud.adobe.com/apps/download/xd?promoid=B8NR3RT1&mv=other) to create wireframes which will provide an overview of how the website will look.

## Database

NoSql MONGODB is used to store data at the backend.

## Features
### Existing Features
- **Home** - when user come to the website he/she will see the home page which is consist of welcoming headline and a bit explanation of what all this website is about.
- **Recipes** - At this page user can see all the recipes and edit or delete them. To see the details of each recipes, user need to click on "Food Name" or "Country Name".
- **Create** - user can add/store to the database and also share it with others in recipes page.
- **Publish Button** - User needs to click on "Publish" Inorder to add/store to the database and also share it with others in recipes page.
- **Search** - User can search for any type of food through search bar, if any result found, he/she will see the recipe/recipes, otherwise he/she gets the message of "No Result Found".
- **Edit/Delete Buttons** - User can delete any recipe from the website and data base by clicking on "Delete". User can edite/update any recipe by clicking on "Edit".
- **Save Button** - User needs to click on "Save" after editing/updating a recipe in order to save and update the new details of the recipe in database.

### Features Left to Implement

- **Pagination** - In future I would like to add pagination so that a few number of recipes can be shown on **Recipes** page and remain on page 2 or 
page 3 etc.
- **Registration** - User will be able to create an account, login and logout.
- **Recipe Image** - User will be able to add an image for the recipe he/she created.
- **Recipe's ownership** - User will only be able to edit,delete his own recipes after login to his/her account.
## Technologies Used

- **HTML5**
- **CSS3**
- **JQuery**
- **[Materialize Framework](https://materializecss.com/)**
- **[Python](https://www.python.org/)**
- **[Flask](https://flask.palletsprojects.com/en/1.1.x/)**
- **[Jinja](https://jinja.palletsprojects.com/en/2.11.x/)**
- **[AdobeXD](https://creativecloud.adobe.com/apps/download/xd?promoid=B8NR3RT1&mv=other)**
- **[PyMongo](https://pymongo.readthedocs.io/en/stable/)**
- **[MongoDB](https://www.mongodb.com/)**
- **[Google Fonts](https://fonts.google.com/)**
- **[Git & Github](https://github.com/)**
- **[Heroku](https://www.heroku.com/#)**


## Testing

Google developers tool has been used to test the project constantly form the  beginning to identify any error or to see how the changes looks like on different screen sizes.

### User Stories

User stories from the UX section were tested to see if they all work as intended.
1. *As a user, I want to see a list of recipes.*
- Go to the **Recipes** Page.
2. *As a user, I want to search for recipes so that I can find easily and quickly.*
- Go to the **Recipes** Page
- Go to the search bar above the recipe's lists and write any key word to search for the recipe.
- Press Enter.
- A list of recipes will be displayed.
- If no recipe found then nothing will be displayed.
3. *AS a user, I want to store/add and share my recipes online with others.*
- Go to the **Create** Page.
- Fill out the form. All fields are required to fill in.
-  Click on **Publish** button. User will be redirected to the list of all recipes.
4. *As a user, I want to see the details of the recipe.*
- Find the recipe either by using **Search bar** or from list **Recipes**.
- Click on the "Food Name" or "Country Name" then the recipe tab will collapse adn you can see the details.
5. *As a user, I want to update existing recipes.*
- Go to the **Recipes** Page.
- Click on the **Edit** button and recipe details will open in a editable form.
- Edit the required field and click on save button.
- If user want to cancel the update and return to the previous page then just click on **Recipes** page. If user click on any other pages, he/she will be redirected to that page without updating/saving any of changes he has already made.
6. *As a user, I want to delete existing recipes.*
- Go to the **Recipes** Page.
- Click on **Delete** button on any of the recipes you wish to delete.

### Responsiveness on different browsers & Mobiles

The website looks fine and work properly on following web browsers and mobiles when tested on them.
- Google Chrome
- Microsoft Edge
- Firefox
- Opera
- All devices listed in responsive section of the DevTools on the google chrome. From "Moto G4" to "iPad Pro".

### Code Validation

The code has been validated by using;

- [W3C Markup Validation Service for HTML](https://validator.w3.org/)
- [W3C Markup Validation Service for CSS](https://jigsaw.w3.org/css-validator/)
- [Pep8 Online for Pyhton](http://pep8online.com/)

## Deployment to Heroku

- **[cook-book-milestone Live Page](https://cook-book-milestone.herokuapp.com/home_page)**

- **[cookbook Repository](https://github.com/IIxShahinxII/cookbook)**

1. Login to **[Heroko](https://www.heroku.com/)** account.
2. Click on **New** at the right top corner and click on **Create new app**.
3. Choose **App name** and a **region**. Then click on **Create app**.
4. Go to terminal window and create **requirements.txt** by running command **pip3 freeze --local > requirements.txt**
5. Then create **Procfile** by running command **echo web: python app.py > Procfile** **Remember P is capital**
6. Add these files to stagging area by running command **git add requirements.txt** & **git add Procfile**.
7. Then commit these file respectively by running command **git commit -m "Added requirements.txt** & **git commit -m "Added Procfile**.
8. Then push these files to **github** by running command **git push**
9. Go back to **Heroku** to your **App** and click on **Deploy** tab.
10. Then go to **Deployment Method** and click on **Github Connect to Github**.
11. Then make sure your **Github Profile** is displayed and add your **repository name** and click on **Search**.
12. Once it find your repository then click on **Connect**.
13. Now go to **Settings** at the top. Then click on **Reveal Config Vars**.
14. In **Config Vars** add **IP** with value **0.0.0.0** then add **PORT** as **5000** then add **SECRET_KEY** then add **MONGO_URI** and then add **MONGO_DBNAME** which is the name of database.
15. Now go back to **Deploy** tab and click on **Enable Automatic Deploys**.
16. Now click on **Deploy Branch**
17. It will take a minute and display a message that **Your app was successfully deployed**.
18. Click on **View** to launch your deployed app.

## Local Deployment

1. Go to [cookbook Repository](https://github.com/IIxShahinxII/cookbook)
2. Click on **Code** beside **Gitpod**.
3. A drop down menu open then click on **Download Zip**
4. Unzip the downloaded zip file.
5. Open app.py file and install requirements.txt by running command **pip3 install -r requirements.txt**.
6. Create a database in **MONGODB**.
7. Create env.py file and add **MONGO_URI** and **SECRET_KEY**.
8. Now run the app.py by running code **python3 app.py**.

## Credits
### Content

- Create button has been taken from [freefrontend](https://freefrontend.com/css-gradient-buttons/)

### Media

- The background image of home page has been taken from [Unsplash](https://unsplash.com/)

### Acknowledgements
- Code Institute's **Task Manager Application** I follow it to design and develop my **EasyCook** website.
- The project is based on **Materialize**, so the code is taken from [Materialize](https://materializecss.com/)
- A special thanks to my mentor **Maranatha** for his valuable feedback during mentoring sessions.
- [W3Schools](https://www.w3schools.com/)

## Disclaimer
This project is for educational purposes only.

