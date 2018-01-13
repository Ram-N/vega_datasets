# Python 2/3 compatibility

try:
    from urllib.error import URLError, HTTPError
    from urllib.request import urlopen, urlretrieve
    from io import BytesIO
    def bytes_decode(bytes_, encoding='utf-8'):
        return bytes_.decode(encoding)
except ImportError:
    # Python 2.X
    from urllib2 import URLError, HTTPError, urlopen
    from urllib import urlretrieve
    from StringIO import StringIO as BytesIO
    def bytes_decode(bytes_, encoding='utf-8'):
        return bytes_

try:
    from functools import lru_cache
except ImportError:
    # Python 2.X: function not available
    def lru_cache(maxsize=128, typed=False):
        return lambda y: y
