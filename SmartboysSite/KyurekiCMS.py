from flask import Flask
from pymongo import Connection
import yaml, Plugins
from Plugins.Pages import blueprint
from datetime import datetime

class KyurekiCMS(object):
    def __init__(self):
        self.app = Flask(__name__)
        self.app.jinja_env.filters['datetimeformat'] = self.datetimeformat
        self.app.jinja_env.filters['todaysdate'] = self.todaysdate
        self.app.jinja_env.filters['int'] = self.int

    def datetimeformat(self, value, format='%Y-%m-%d %I:%M:%S %p'):
        return value.strftime(format)
    
    def todaysdate(self, format):
        return datetime.today().strftime(format)
        
    def int(self, num):
        return int(num)

    def loadConfig(self, conffile):
        f = open(conffile)
        config = yaml.load(f)
        f.close()
        for key in config:
            self.app.config[key] = config[key]
        self.loadDB()
        self.loadPlugins()

    def loadPlugins(self):
        for plugin in self.app.config["plugins"]:
            plugin_class = __import__('SmartboysSite.Plugins.%s' % plugin, fromlist="blueprint")
            plugin_class.db = self.connection.smartboyssite
            self.app.register_blueprint(blueprint, url_prefix=self.app.config["plugins"][plugin]["prefix"])

    def loadDB(self):
        self.connection = Connection(self.app.config['database']['host'], self.app.config['database']['port'])

    def run(self, host='127.0.0.1', port='5000'):
        self.app.run(host=host, port=port)