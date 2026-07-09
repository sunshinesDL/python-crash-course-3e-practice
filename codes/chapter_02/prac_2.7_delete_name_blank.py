# Created Time: 2026/07/09
# Author: sunshinesDL (sunshinesDL@163.com)

"""Test strip() & lstrip() & rstrip()."""


cats = "\tMimi\t&\tXiaomi\n"

print(cats)
print(f'消除左空白后：\n{cats.lstrip()}')
print(f'消除右空白后：\n{cats.rstrip()}')
print(f'消除两端空白后：\n{cats.strip()}')
