"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

import Photo_Album2.views
