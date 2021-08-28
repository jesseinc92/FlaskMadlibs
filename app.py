from flask import Flask, request, render_template
from stories import story

app = Flask(__name__)

@app.route('/home')
def get_words():
    prompt_words = story.prompts
    return render_template('home.html', words=prompt_words)

@app.route('/story')
def show_story():
    answers = request.args
    return render_template('story.html', filler=story.generate(answers))