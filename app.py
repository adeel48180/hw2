import random
from flask import Flask
from flask import jsonify

app = Flask(__name__)

jokes = [
    "Whats the best thing about Switzerland?I dont know, but the flag is a big plus.",

    "I invented a new word! Plagiarism!",

    "Did you hear about the mathematician whos afraid of negative numbers? Hell stop at nothing to avoid them.",

    "Why don't skeletons fight each other? They don't have the guts!",

    "Helvetica and Times New Roman walk into a bar.Get out of here!” shouts the bartender. We dont serve your type",

    "What do you call a bear with no teeth? A gummy bear!",

    "What did one wall say to the other wall? Ill meet you at the corner!",

    "How do all the oceans say hello to each other? They wave!",

    "How do you talk to a giant? Use big words!",

    "Where do cows go for entertainment? To the moo-vies!"
]

@app.route('/myJoke')

def gJoke():

    random_joke = random.choice(jokes)

    return jsonify(random_joke)

if __name__ == '__main__':

    app.debug = True

    app.run(port=8000)

