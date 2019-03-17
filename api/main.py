#!/usr/bin/python3
#

from datetime import date

from sanic import Sanic
from sanic.views import HTTPMethodView
from sanic_jinja2 import SanicJinja2

from api.databases import db, PersonInfo

app = Sanic(__name__)
jin = SanicJinja2(app, pkg_path='./templates')


# app.static('/static', '../static')


@app.route('/')
async def index(request):
    # print("init data")
    # db.connect()
    # print("connection ok")
    # lily = PersonInfo.create(name='lily', birthday=date(1996, 1, 1), location="china", info='is girl')
    # print("the name ", lily.name)
    # print('done')
    return jin.render('me.html', request, name='lily')


class People(HTTPMethodView):

    def get(self, request):
        db.connect()
        target = PersonInfo.get(name='lily')
        print(target.name)
        return jin.render('people.html', request)

    def post(self, request):
        """ adding people information """
        pass

    def patch(self, request):
        """ update people information """
        pass

    def delete(self, request):
        """ delete people information """
        pass


app.add_route(People.as_view(), '/pep')

app.run('0.0.0.0', 8000)
