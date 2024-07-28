from flask import Flask, render_template
from flask_caching import Cache
from .blueprints import main


app = Flask(__name__)

app.register_blueprint(main)

app.config['CACHE_TYPE'] = 'FileSystemCache'
app.config['CACHE_DIR'] = 'cache'
cache = Cache(app)




if __name__ == '__main__':
    app.run()


