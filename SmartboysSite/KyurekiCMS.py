from flask import Flask
from pymongo import Connection
import yaml, Plugins
from Plugins.Pages import blueprint

class KyurekiCMS(object):
    def __init__(self):
        self.app = Flask(__name__)

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