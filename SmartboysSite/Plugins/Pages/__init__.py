from flask import Blueprint

blueprint = Blueprint('Pages', 'SmartboysSite.Plugins.Pages')

from SmartboysSite.Plugins.Pages import View