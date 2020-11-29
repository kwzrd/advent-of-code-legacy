import logging

# Basic logging setup
# All messages that reach the root log are written to stdout
root = logging.getLogger()
root.setLevel(logging.DEBUG)
root.addHandler(logging.StreamHandler())
