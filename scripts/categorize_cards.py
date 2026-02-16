#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
総合リストのカードをキーワードでカテゴリに振り分ける。
"""
import re
import sys

# カテゴリ別キーワード（含まれたらそのカテゴリに分類。先にマッチした方を優先）
CATEGORY_KEYWORDS = {
    'ペット用品': [
        'c-label-2--pet', 'ペット', '愛犬', '愛猫', 'アイシア', 'i CARE', '避妊', '去勢',
        'まぐろペースト', 'かつおスティック', 'アレルギーケア', '冷凍ペットフード', 'ペットフード'
    ],
    'ドリンク/お酒': [
        'ビール', 'サッポロ', 'アサヒビール', 'サッポロビール', '梅酒', '鍛茶', '彩香',
        'フィーバーツリー', 'エルダー', 'トニック', '抹茶ラテ', 'ネスカフェ', 'コーヒー',
        '紅茶ハイ', '緑茶ハイ', 'ドリンク', '飲料', 'お酒にプラス', '果実ほおばる', 'グレフル'
    ],
    '食品': [
        '明治', '辻利', 'ベビースター', 'ラーメン', 'にゅーみん', 'オットギ', '白米どうぞ',
        '味の素', 'パン粥', 'カルビー', '菓子', '鶏白湯', 'こんがりパン', 'コーンポタージュ',
        'ブレンディ', 'スティック', '牛乳', '白米', '銀だこ', 'お濃い抹茶'
    ],
    'ダイエット/健康': [
        'エクオール', 'ノコギリヤシ', 'ヘルプ', 'ディアナチュラ', '高麗人参', '健脳',
        'サラシア', '熟成黒酢', '黒にんにく', 'プロテイン', '亜鉛', '免疫', '酢酸菌',
        'セサミン', 'ルテイン', 'ミニタス', 'マルチミネラル', '深海鮫', 'キオクリア',
        'リコピン', 'ピクノ', 'ナイシヘルプ', 'キトサン', '青汁', 'プラセンタ', 'NMN',
        'アスタキサンチン', 'DHA', 'EPA', 'ヒルズラボ', 'ダイエットコラーゲン', 'スリムアップ',
        '機能性表示食品', 'URUSUYA', 'ウルスヤ', 'スリムウォーク', '中脂ヘルプ'
    ],
    '化粧品関連': [
        'クリーム', 'シャンプー', 'スキンケア', 'ファンデーション', 'リップ', 'エッセンス',
        'ローション', 'カラミー', 'スピラ', 'ビタバランス', 'ハーバニエンス', 'スカルプ',
        'トリートメント', '白髪染め', 'アイブロウ', 'アイラッシュ', '涙袋', 'パウティ',
        'コンシーラー', 'BBクリーム', 'クレンジング', '化粧水', 'モイスチャー', 'ピール',
        'セラム', 'ジェル', 'エイジング', 'ウォーター', '美容', 'コスメ', 'COSMURA',
        'グランジュール', 'イビサ', 'ヘアーリムーバル', 'ユンケル', '滋養液', 'ベルタ',
        'スカルプシャンプー', 'ルナパッチ', 'ピコモンテ', 'ビューティフル', 'コンシー',
        'フェイスリー', 'マスク', 'Ukima', 'EYELASH', 'ブリリアントピール', 'Uhue',
        'スウィーツ', 'アイブロウワックス', 'ヘッドスクラブ', 'AGARISM', '檸檬', 'ハトムギ',
        'HADAOMOI', 'レチノ', '目元', 'Lavit', 'BB', 'ナイアシン', 'ローズ', 'アピュー',
        'NARTH', 'ビタミンC', 'labo', 'ヘッドスパ', 'ラクブラ', 'PINKROSA', '絹しずく',
        'スラっと発酵', 'DearDoer', 'ボディスクラブ', 'ダイアンボヌール', 'STボタニカ',
        'キレイファクトリー', 'ラッシュ', 'カルテメイド', 'MILY', 'Re\'senza', 'HOUSE OF FLORENCE',
        'アカラン', 'バランシング', 'ROSA BLU', 'ナイトブラ', 'W・VC', 'ミラブル', 'エクソソーム',
        'CICA', 'ディアボーテ', 'スパニスト', 'スカルプ', 'アパティア', 'ホワイトニング',
        'KAMIKA', '乙女のしおり', '馬油', 'グランメリア', 'SECRET SCIENCE', 'フェイスマスク',
        'MEスマートエピ', 'VDL', 'パーフェクティング', 'ザイエル', 'コラーゲン', 'ステムセル',
        'ビタブリッド', 'ティアレラ', 'カナデル', 'マリンボーテ', 'グロスカラー', 'hairju',
        'ピコモンテ', 'ナイアシンアミド', 'アクティブチャコール', 'ユンケルローヤル'
    ],
    '家具/インテリア': [
        '家具', 'インテリア', 'ソファ', 'テーブル', '椅子', 'ランプ', '照明', 'カーテン',
        '絨毯', '収納', 'デスク', 'ベッド', 'フォトフレーム', 'ランプシェード', 'ワイン保存',
        'Vie-de Vin', 'パウチ'
    ],
    '家電': [
        '家電', '電気', '冷蔵', '洗濯機', 'テレビ', 'エアコン', '掃除機', 'ドライヤー',
        '炊飯', '電子レンジ', '加湿器', '空気清浄', 'スチーマー', 'フェイススチーマー',
        'ディスペンサー', '歯磨き粉'
    ],
    'クーポン': [
        'クーポン', '割引', 'お買い得', '定期便専用', '円お買い', 'お試し', 'キャンペーン'
    ],
    '日用品/生活雑貨': [
        '掃除', '洗剤', '花王', 'スコッチ', '網戸', 'ワイパー', 'メリット', '詰め替え',
        'フック', 'コマンド', 'お風呂', 'ととのえる', '歯磨き',
        'アースノーマット', 'アタックZERO', 'ジット', '温泡', 'ONPO', '乾燥が気になる',
        '刀剣'
    ],
    'ベビー/キッズ': [
        'おくち育', 'まほうハブラシ', 'ベビー', 'キッズ', '子供'
    ],
}


def categorize_card(card_html):
    """1枚のカードHTMLをキーワードでカテゴリ判定。最初にマッチしたカテゴリを返す。"""
    for cat, keywords in CATEGORY_KEYWORDS.items():
        for kw in keywords:
            if kw in card_html:
                return cat
    return None  # どれにも当てはまらない場合は総合のみ


def main():
    html_path = sys.argv[1] if len(sys.argv) > 1 else 's/app_published/list_tamesu--swiper.html'
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 総合の <ul> 内のみ抽出（最初の list14 で id="content" の ul）
    ul_start = '<ul class="list14 clearfix p-project-lists c-grid--row c-grid--row--no-gutter" id="content">'
    ul_end = '</ul>'
    i0 = html.find(ul_start)
    if i0 == -1:
        print('UL not found', file=sys.stderr)
        sys.exit(1)
    i0 += len(ul_start)
    i1 = html.find(ul_end, i0)
    if i1 == -1:
        print('UL end not found', file=sys.stderr)
        sys.exit(1)
    ul_content = html[i0:i1]

    # 各 <li class="c-grid--col grid-col-tame post">...</li> を抽出
    li_pattern = re.compile(
        r'<li class="c-grid--col grid-col-tame post">(.*?)</li>',
        re.DOTALL
    )
    cards = []
    for m in li_pattern.finditer(ul_content):
        full_li = '<li class="c-grid--col grid-col-tame post">' + m.group(1) + '</li>'
        cards.append(full_li)

    # カテゴリごとに振り分け
    by_cat = {cat: [] for cat in CATEGORY_KEYWORDS}
    by_cat['その他'] = []
    for card in cards:
        cat = categorize_card(card)
        if cat:
            by_cat[cat].append(card)
        else:
            by_cat['その他'].append(card)

    # 各カテゴリスライド用の HTML を生成（食品〜クーポンまで10カテゴリ）
    category_order = [
        '食品', 'ドリンク/お酒', 'ダイエット/健康', '化粧品関連',
        '日用品/生活雑貨', 'ベビー/キッズ', 'ペット用品',
        '家具/インテリア', '家電', 'クーポン'
    ]
    out_lines = []
    for cat in category_order:
        lis = by_cat.get(cat, [])
        if lis:
            out_lines.append(
                '                    <div class="swiper-slide">\n'
                '                      <ul class="list14 clearfix p-project-lists c-grid--row c-grid--row--no-gutter">\n'
                + '\n'.join('                        ' + li for li in lis) +
                '\n                      </ul>\n                    </div>'
            )
        else:
            out_lines.append(
                '                    <div class="swiper-slide">\n'
                '                      <ul class="list14 clearfix p-project-lists c-grid--row c-grid--row--no-gutter">\n'
                '                      </ul>\n                    </div>'
            )

    # 1つのブロックとして出力（食品〜クーポンまで10スライド分）
    print('\n                    <!-- 食品 -->\n' + out_lines[0] + '\n                    <!-- /食品 -->')
    print('                    <!-- ドリンク/お酒 -->\n' + out_lines[1] + '\n                    <!-- /ドリンク/お酒 -->')
    print('                    <!-- ダイエット/健康 -->\n' + out_lines[2] + '\n                    <!-- /ダイエット/健康 -->')
    print('                    <!-- 化粧品関連 -->\n' + out_lines[3] + '\n                    <!-- /化粧品関連 -->')
    print('                    <!-- 日用品/生活雑貨 -->\n' + out_lines[4] + '\n                    <!-- /日用品/生活雑貨 -->')
    print('                    <!-- ベビー/キッズ -->\n' + out_lines[5] + '\n                    <!-- /ベビー/キッズ -->')
    print('                    <!-- ペット用品 -->\n' + out_lines[6] + '\n                    <!-- /ペット用品 -->')
    print('                    <!-- 家具/インテリア -->\n' + out_lines[7] + '\n                    <!-- /家具/インテリア -->')
    print('                    <!-- 家電 -->\n' + out_lines[8] + '\n                    <!-- /家電 -->')
    print('                    <!-- クーポン -->\n' + out_lines[9] + '\n                    <!-- /クーポン -->')


if __name__ == '__main__':
    main()
