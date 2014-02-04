from .base import *  # NOQA

try:
    from .local import *  # NOQA
except ImportError as exc:
    exc.args = tuple(
        ['%s (did you rename settings/local.py-dist?)' % exc.args[0]]
    )
    raise exc
