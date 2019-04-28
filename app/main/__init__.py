from flask import Blueprint

#decrale a blueprint name 'main'
main = Blueprint('main', __name__)

#. means the current directory/current package
# need to be imported at the BOTTOM due to circular dependencise
from . import views, errors 

