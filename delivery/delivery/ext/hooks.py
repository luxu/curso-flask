def init_app(app):

    @app.before_first_request
    def init_everythings():
        print('Antes do primeiro requests!')
