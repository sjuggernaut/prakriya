import sys
sys.path.insert(0, '/var/www/html/sanskritworldflask')
sys.path.append('/usr/local/lib/python3.5/dist-packages')
sys.path.append('/usr/lib/python3/dist-packages')
# from dhatu import app as application
# from dhatu_restplus import app as application
from prakriya_restplus import app as application
