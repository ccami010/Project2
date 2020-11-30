# Python looks under the initializer file for any needed attributes

from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = '2Pp54pInoMTYxc7LoxphWpzxRIMgWPnKcF7C43-g'

from project2_Flask import routes