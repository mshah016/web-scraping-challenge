from flask import Flask, render_template, redirect 
from flask_pymongo import PyMongo
import mission_to_mars

app = Flask(__name__)

# app.config["Mongo_URI"] = "mongodb://localhost:27017/mars_db"
# mongo = PyMongo(app)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")

@app.route("/")
def main():
    information = mongo.db.information.find_one()
    print(information)
    return render_template('index.html', information=information)


@app.route("/scrape")
def scraper(): 
    information = mongo.db.information
    information_data = mission_to_mars.scrape()
    # print(information_data)
    information.update({}, information_data, upsert=True)
    return redirect("/")


if __name__=="__main__":
    app.run(debug=True)
