#!/home/wtc/UI_Location/myenv/bin/python3
# -*- coding: utf-8 -*-
import re
import sys
from requires_io.commands import main
if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(main())
