#!/usr/bin/env python3

from flask import Flask, render_template
import Util
import Score

app = Flask('Scores')

@app.route('/')
def index():
    #score = Score.get_score(Util.SCORES_FILE_NAME)
    return render_template('Scores.html', score = Score.get_score(Util.SCORES_FILE_NAME)
)




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090)
