import pypiserver
PACKAGES = '/absolute/path/to/packages'
HTPASSWD = '/absolute/path/to/htpasswd.txt'
application = pypiserver.app(root=PACKAGES, redirect_to_fallback=True, password_file=HTPASSWD)