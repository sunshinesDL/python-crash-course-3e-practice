# Created Time: 2026/07/09
# Author: sunshinesDL (sunshinesDL@163.com)

"""Test removesuffix() & removeprefix()."""


filename = "python_notes.txt"
dedao_ebook_url = 'https://www.dedao.cn/ebook/reader'

print(f'原始文件名为：{filename}')
print(f"去除后缀的文件名为：{filename.removesuffix('.txt')}")
print(f'原始网址为：{dedao_ebook_url}')
print(f'去除前缀后的网址为：{dedao_ebook_url.removeprefix('https://')}')
