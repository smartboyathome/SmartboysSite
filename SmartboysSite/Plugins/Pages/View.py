from SmartboysSite.Plugins.Pages import blueprint, db
#from SmartboysSite import cms
from flask import abort, render_template

@blueprint.route("/Test")
def renderManage():
    return "Ohai thar! This be a test!"

@blueprint.route("/<page>")
def renderPage(page):
    pages = db.pages
    page = pages.find_one({ 'id' : page })
    if page is None: abort(404)
    return render_template('Pages/basic_page.html',
                           PageTitle=page["title"],
                           PageContent=page["content"],
                           lastEditedDate=page["lastEdit"].keys()[-1])