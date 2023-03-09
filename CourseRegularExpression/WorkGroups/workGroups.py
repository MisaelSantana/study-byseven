#*-* coding=utf-8 *-*
import re

name = 'Thomas William'

pattern = re.compile(r'(?P<first>\w+)\W+(?P<last>\w+)')
m = pattern.match(name)
if m:
    print(m.group('first'))
    print(m.group('last'))
    print(m.groupdict())
    d = m.groupdict()

    for t in d:
        print('key', t)
        print('value: ', d[t])
