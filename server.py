#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
import os
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.web import url
import tornado.websocket
from datetime import datetime
import urllib

class TopHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html', name='')

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        parsed_origin = urllib.parse.urlparse(origin)
        return parsed_origin.netloc == "192.168.33.13"
        #return True

    def on_message(self, message):
        now = datetime.now()
        now_str = now.strftime('%Y/%m/%d %H:%M:%S')

        self.write_message(now_str)

if __name__ == "__main__":
    application = tornado.web.Application(
        [
            url(r"/", TopHandler, name='index'),
            url(r"/ws", WebSocketHandler, name='ws'),
        ],
        template_path=os.path.join(os.path.dirname(os.path.abspath(__file__)),  "templates"),
        static_path=os.path.join(os.path.dirname(os.path.abspath(__file__)),  "static"),
    )

    server = tornado.httpserver.HTTPServer(application)
    server.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
