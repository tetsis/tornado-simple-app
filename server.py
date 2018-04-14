#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
import os
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.web import url

class TopHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html', name='')

if __name__ == "__main__":
    application = tornado.web.Application(
        [
            url(r"/", TopHandler, name='index'),
        ],
        template_path=os.path.join(os.path.dirname(os.path.abspath(__file__)),  "templates"),
        static_path=os.path.join(os.path.dirname(os.path.abspath(__file__)),  "static"),
    )

    server = tornado.httpserver.HTTPServer(application)
    server.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
