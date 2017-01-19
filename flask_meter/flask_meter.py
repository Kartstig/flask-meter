# -*- coding: utf-8 -*-

from __future__ import print_function

import subprocess

from flask import jsonify

class FlaskMeter(object):
  GIT_CMD = 'git log | head -3'

  def __init__(self, app=None):

    self.app = app

    if app is not None:
      self.init_app(app)

  def init_app(self, app):
    """
    Adds in hooks to Flask
    """

    self.app = app

    def _health():
      data = {}
      try:
        ret = subprocess.check_output([self.GIT_CMD], shell=True).split("\n")
        if len(ret) >= 3:
          commit = ret[0].split()[1]
          author = (" ").join(ret[1].split()[1:])
          date = (" ").join(ret[2].split()[1:])
          git_enable = True
        else:
          git_enable = False
      except subprocess.CalledProcessError:
        git_enable = False

      data = {
        "status":     "OK",
        "git_check":  git_enable,
        "commit":     commit,
        "author":     author,
        "date":       date
      }

      return jsonify(data)

    self.app.add_url_rule('/_health', '_health', _health)