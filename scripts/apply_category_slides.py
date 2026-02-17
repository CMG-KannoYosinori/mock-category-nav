#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
category_slides_output.txt の内容で list_tamesu--swiper.html の
食品〜クーポン（全カテゴリ）のスライドを置き換える。
"""
import sys

def main():
    html_path = 's/app_published/list_tamesu--swiper.html'
    output_path = 's/app_published/category_slides_output.txt'

    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    with open(output_path, 'r', encoding='utf-8') as f:
        new_slides = f.read().strip()

    start_marker = '                    <!-- 食品 -->'
    start_alt = '<!-- 食品 -->'
    end_marker = '                    <!-- /クーポン -->'
    end_alt = '<!-- /クーポン -->'
    i0 = html.find(start_marker)
    if i0 == -1:
        i0 = html.find(start_alt)
    i1 = html.find(end_marker)
    if i1 == -1:
        i1 = html.find(end_alt)
    if i0 == -1:
        print('ERROR: start_marker (<!-- 食品 -->) not found in HTML', file=sys.stderr)
        sys.exit(1)
    if i1 == -1:
        print('ERROR: end_marker (<!-- /クーポン -->) not found in HTML', file=sys.stderr)
        sys.exit(1)
    # 終了位置は「<!-- /クーポン -->」の行末まで
    i1 = html.index('\n', i1) + 1

    html = html[:i0] + new_slides + html[i1:]
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print('Done. Replaced category slides in', html_path)


if __name__ == '__main__':
    main()
