import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'cook-book'
app.config["MONGO_URI"] = 'mongodb+srv://iixshahinxii:Shahin1371@firstcluster-4kc0v.mongodb.net/cook-book?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
@app.route('/home_page')
def home_page():
    return render_template("index.html")


@app.route('/search_recipe', methods=['POST'])
def search_recipe():
    search_recipes = request.form.get("search_recipes")
    mongo.db.recipes.create_index([("$**", 'text')])
    recipe = mongo.db.recipes.find({"$text": {"$search": search_recipes}})
    return render_template('recipes.html', recipes=recipe, search=True)


@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())


@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html')


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    return render_template('editrecipe.html', recipe=the_recipe)


@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update({"_id": ObjectId(recipe_id)},
                   {
        'duration': request.form.get('duration'),
        'serving': request.form.get('serving'),
        'food_name': request.form.get('food_name'),
        'country': request.form.get('country'),
        'ingredients': request.form.get('ingredients'),
        'preparation': request.form.get('preparation')
    })
    return redirect(url_for('get_recipes'))


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=(os.environ.get('PORT')),
            debug=True)
