import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/jaswanth/amr/mechabot_ws/src/install/mechabot_scripts'
