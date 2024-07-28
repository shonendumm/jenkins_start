from flask import Blueprint, render_template, current_app

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/add/<request>')
def add(request):
    from app import cache
    # cache = current_app.extensions['cache']
    # breakpoint()
    cache.set("value", request)
    return f"value added: {request}"

@main.route('/get')
def getvalue():
    from app import cache
    # cache = current_app.extensions['cache']
    value = cache.get("value")
    return f"hello, value is {value}"