from SmartboysSite.Plugins.Pages import blueprint
#from SmartboysSite import cms
from flask import abort, render_template
from pymongo import Connection
from datetime import datetime

def connectToDb():
    return Connection('localhost', 27017).smartboyssite

@blueprint.route("/Test")
def renderManage():
    return "Ohai thar! This be a test!"

@blueprint.route("/", defaults={ "page": "Index" })
@blueprint.route("/<page>")
def renderPage(page):
    pages = connectToDb().pages
    page = pages.find_one({ 'id' : page })
    if page is None: abort(404)
    return render_template('Pages/basic_page.html',
                           PageTitle=page["title"],
                           PageContent=page["content"],
                           lastEditedDate=datetime.fromtimestamp(float(page["lastEdit"].keys()[-1])))

@blueprint.route("/<page>/Edit")
def editPage(page):
    pass

@blueprint.route("/<page>/Delete")
def deletePage(page):
    pass