#!D:\Anaconda\envs\donkey\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'donkeycar','console_scripts','donkey'
__requires__ = 'donkeycar'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('donkeycar', 'console_scripts', 'donkey')()
    )
