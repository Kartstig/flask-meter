# -*- coding: utf-8 -*-

from __future__ import print_function

from flask import Flask, jsonify
from datetime import datetime

from .git import git_stats

class FlaskMeter(object):

  def __init__(self, app=None):
    self.app = app

    if app is not None:
      self.init_app(app)

  def init_app(self, app):
    if not isinstance(app, Flask):
      raise TypeError("Argument app is not of type Flask")

    self.app = app
    self.app.config['FM_GIT'] = self.app.config.get('FM_GIT', True)
    self.start_time = datetime.now()

    def _health():
      data = {
        "status":     "OK",
        "uptime":     str(datetime.now() - self.start_time),
        "app":        self.app.name,
      }

      if self.app.config['FM_GIT']:
        data.update({"git": git_stats()})

      return jsonify(data)

    self.app.add_url_rule('/_health', '_health', _health)
