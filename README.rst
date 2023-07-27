===============================
Flask-Meter
===============================

        Healthchecks for Flask_ Apps

.. _Flask: https://github.com/pallets/flask/

.. image:: https://img.shields.io/pypi/v/Flask-Meter.svg
        :target: https://pypi.python.org/pypi/Flask-Meter

.. image:: https://tc.spin-flip.com/app/rest/builds/buildType:id:FlaskMeter_TestPython310/statusIcon.svg
        :target: https://tc.spin-flip.com/project/FlaskMeter?mode=trends

.. image:: https://readthedocs.org/projects/flask-meter/badge/?version=latest
        :target: https://flask-meter.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://codecov.io/gh/Kartstig/flask-meter/branch/master/graph/badge.svg?token=NsmixA2iCH
        :target: https://codecov.io/gh/Kartstig/flask-meter

.. image:: https://img.shields.io/pypi/dm/Flask-Meter
        :alt: PyPI - Downloads

Flask-Meter is an add-on to the Flask web framework. Flask-Meter adds a
monitoring endpoint for consuming application metrics. It can be really simple
to set up. Flask-Meter modifies the Flask application to provide an enpoint
at `/_health` where you will get a JSON response of the system's uptime,
current git revision.

You can also add in extra checks by passing in a list of checks to the
constructor.

Installing
----------

Install and update using `pip`\:

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

* Free software: MIT license
* Documentation: https://flask-meter.readthedocs.io.


Features
--------

* Current Git Commit
* Current Version
* Accepts custom functions


Configuration
-------------

+---------------------+------------------------------+------+---------+
| Config Key          | Description                  | Type | Default |
+=====================+==============================+======+=========+
| FLASK_METER_ENABLE  | Enable/Disable Flask-Meter   | bool | True    |
+---------------------+------------------------------+------+---------+
| FLASK_METER_GIT     | Enable/Disable Git Stats     | bool | True    |
+---------------------+------------------------------+------+---------+
| FLASK_METER_VERSION | Enable/Disable Version Stats | bool | True    |
+---------------------+------------------------------+------+---------+


Sponsorship
-----------

Put your logo here! `Become a sponsor`_ and support this project!

.. _Become a sponsor: https://github.com/sponsors/Kartstig



Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

