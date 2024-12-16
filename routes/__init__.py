from .user import user_bp
from .test import test_bp
from .sleep import sleep_bp


# Blueprintをリストとしてまとめる
blueprints = [
  user_bp,
  test_bp,
  sleep_bp
]
