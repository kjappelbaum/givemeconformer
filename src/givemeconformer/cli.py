# -*- coding: utf-8 -*-

"""Command line interface for :mod:`givemeconformer`.

Why does this file exist, and why not put this in ``__main__``? You might be tempted to import things from ``__main__``
later, but that will cause problems--the code will get executed twice:

- When you run ``python3 -m givemeconformer`` python will execute``__main__.py`` as a script.
  That means there won't be any ``givemeconformer.__main__`` in ``sys.modules``.
- When you import __main__ it will get executed again (as a module) because
  there's no ``givemeconformer.__main__`` in ``sys.modules``.

.. seealso:: https://click.palletsprojects.com/en/7.x/setuptools/#setuptools-integration
"""

from fire import Fire

from .api import create_conformer

__all__ = [
    "main",
]


def main():
    Fire(create_conformer)


if __name__ == "__main__":
    main()
