import os
import sys
import click
import connexion

from swagger_server import encoder

app = connexion.App(__name__, specification_dir='./swagger_server//swagger/')
app.app.json_encoder = encoder.JSONEncoder
app.add_api('swagger.yaml', arguments={'title': 'Swagger Demo'})
application=app.app
