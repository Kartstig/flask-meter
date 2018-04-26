===============================
Flask-Meter
===============================

Flask-Meter is an add-on to the Flask web framework. Flask-Meter adds a
monitoring endpoint for consuming application metrics. It can be really simple
to set up. Flask-Meter modifies the Flask application to provide an enpoint
at `/_health` where you will get a JSON response of the system's uptime,
current git revision.

You can also add in extra checks by passing in a list of checks to the
constructor.

Installing
----------

Install and update using `pip`:
.. code-block:: text
  pip install -U Flask-Meter

Flask Configuration
-------------------

.. code-block:: python

  from Flask import Flask
  from flask_meter import FlaskMeter

  app = Flask(__name__)

  FlaskMeter(app)

Or if you can use the `init_app` function:

.. code-block:: python

    from Flask import Flask
    from flask_meter import FlaskMeter

    app = Flask(__name__)

    flask_meter = FlaskMeter()
    flask_meter.init_app(app)

.. image:: https://travis-ci.org/Kartstig/flask-meter.svg?branch=master
        :target: https://travis-ci.org/Kartstig/flask-meter

.. image:: https://img.shields.io/travis/KartStig/flask_meter.svg
        :target: https://travis-ci.org/Kartstig/flask-meter

.. image:: https://readthedocs.org/projects/flask-meter/badge/?version=latest
        :target: https://flask-meter.readthedocs.io
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/KartStig/flask_meter/shield.svg
     :target: https://pyup.io/repos/github/KartStig/flask_meter/
     :alt: Updates


Flask-Meter adds a monitoring endpoint for consuming application host metrics.


* Free software: MIT license
* Documentation: https://flask-meter.readthedocs.io.


Features
--------

* Current Git Commit
* Accepts custom functions

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

