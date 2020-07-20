# -*- encoding: utf-8 -*-
import click
from delivery.ext.db import db
from delivery.ext.db import models


def init_app(app):

    @app.cli.command()
    def create_db():
        """Este comando inicializa o banco de dados"""
        try:
            db.create_all()
        except Exception as err:
            print('Deu ruim... :('+err)

    @app.cli.command()
    def listar_pedidos():
        # TODO usar tabulate
        click.echo('lista de pedidos')

