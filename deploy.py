

import tornado.ioloop
import tornado.web
import time


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<h1>Hello, world!!!</h1>")
        self.write("<br>  {}".format(time.time()))


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8887)
    tornado.ioloop.IOLoop.current().start()


