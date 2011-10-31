from flask import Blueprint

blueprint = Blueprint('Pages', __name__)
db = None

from SmartboysSite.Plugins.Pages import View