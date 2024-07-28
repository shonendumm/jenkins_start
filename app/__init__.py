from flask import Flask, render_template
from flask_caching import Cache
from .blueprints import main

cache = Cache()

def create_app():
    app = Flask(__name__)


    app.config['CACHE_TYPE'] = 'FileSystemCache'
    app.config['CACHE_DIR'] = 'cache'
    cache.init_app(app)
    # app.extensions['cache'] = cache # this is not needed, will cause errors.

    app.register_blueprint(main)
    return app

app = create_app()




if __name__ == '__main__':
    app.run()


