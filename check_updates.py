from os.path import dirname, sep
import sys
from urllib.request import Request, urlopen
from urllib.error import URLError
import re
f1 = open(dirname(sys.argv[0]) + sep + 'check_updates.txt', 'r', encoding='utf-8')
d1 = f1.read().splitlines()
f1.close()
buf = []
output = []
for line in d1:
    if len(line) > 0 and line[0] != '#':
        buf.append(line)
        if len(buf) == 4:
            r = Request(buf[0], headers={'User-Agent': "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"})
            try:
                responce=urlopen(r)
            except URLError as e:
                if hasattr(e, 'reason'):
                    output.append(buf[0] + '\n' + repr(e.reason))
                elif hasattr(e, 'code'):
                    output.append(buf[0] + '\n' + repr(e.code))
            d2=responce.read()
            responce.close()
            if buf[1] == '0':
                m = re.search(eval(buf[2]), d2)
                if not m:
                    output.append(buf[0] + '\nNot match')
                elif m[1] != eval(buf[3]):
                    output.append(buf[0] + '\n' + repr(m[1]))
            elif buf[1] == '1':
                exec(eval(buf[2]))
            buf = []
if len(output) > 0:
    f2 = open(dirname(sys.argv[0]) + sep + 'check_updates_result.txt', 'w', encoding='utf-8')
    for a in output:
        f2.write(a + '\n')
    f2.close()
    print('YOU HAVE UPDATES OR ERRORS, ' + dirname(sys.argv[0]) + sep + 'check_updates_result.txt')
    input()
