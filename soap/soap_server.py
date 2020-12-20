from spyne import Application, rpc, ServiceBase, Iterable, Integer, Unicode
from spyne.server.wsgi import WsgiApplication
from spyne.protocol.soap import Soap11


class HelloWorldService(ServiceBase):
    @rpc(Unicode, Integer, _returns=Iterable(Unicode))
    def say_hello(ctx, name, times):
        for i in range(times):
            yield 'Hello, %s' % name

application = Application([HelloWorldService],
                          tns='spyne.examples.hello',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11()
                          )

if __name__ == '__main__':
    # You can use any Wsgi server. Here, we choose
    # Python's built-in wsgi server but you're not
    # supposed to use it in production.
    from wsgiref.simple_server import make_server
    wsgi_app = WsgiApplication(application)
    server = make_server('192.168.31.25', 8000, wsgi_app)
    server.serve_forever()