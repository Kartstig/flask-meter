# -*- coding: utf-8 -*-

import subprocess

GIT_CMD = 'git log | head -3'

def git_stats():
  try:
    ret = subprocess.check_output([GIT_CMD], shell=True)\
      .decode('utf-8')\
      .split("\n")
    if len(ret) >= 3:
      commit = ret[0].split()[1]
      author = (" ").join(ret[1].split()[1:])
      date = (" ").join(ret[2].split()[1:])
      return {
        "commit": commit,
        "author": author,
        "date":   date
      }
    else:
      return {}
  except subprocess.CalledProcessError:
    return {}
