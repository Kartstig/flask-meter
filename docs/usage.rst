=====
Usage
=====

To use Flask-Meter in a project\:

.. code-block:: python

    from Flask import Flask
    from flask_meter import FlaskMeter

    app = Flask(__name__)

    FlaskMeter(app)


Or if you can use the *init_app* function\:

.. code-block:: python

    from Flask import Flask
    from flask_meter import FlaskMeter

    app = Flask(__name__)

    flask_meter = FlaskMeter()
    flask_meter.init_app(app)
