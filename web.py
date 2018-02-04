#!/usr/bin/env python
"""Interfaz web.

{
    "status": "OK",
    "ejemplo": { "ruta": "/ruta/parametro",
                 "valor": "{JSON: devuelto}"
    }
}
"""
import hug
import os

DIR_BASE = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), 'template')


@hug.get('/', output=hug.output_format.html)
def raiz(**kwargs):
    """Devuelve el archivo html."""
    with open(os.path.join(DIR_BASE, 'base.html')) as base:
        return base.read()


@hug.get('/status')
def status():
    """Return web status."""
    return {'status': 'OK'}


def main():
    port = str(os.environ.get('PORT', 5000))
    hug.API(__name__).http.serve(port)


if __name__ == "__main__":
    main()
