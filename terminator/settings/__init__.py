from base import *

try:
    from local import *
except Exception:
    print('WARNING: Did you forgot to copy terminator/settings/local.py-dist to terminator/settings/local.py?')
