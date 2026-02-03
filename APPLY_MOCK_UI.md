# mock/index.html UI の適用

`mock/index.html` の「Navigation 付き Slider（Swiper 同期）」UI を `s/app_published/list_tamesu--swiper.html` に挿入した際の適用内容を記録する。

## 概要

- **元ソース**: `mock/index.html`
- **適用先**: `s/app_published/list_tamesu--swiper.html`
- **挿入位置**: 「タメせる」タブ内の `<input type="hidden" name="event_name[]" value="tame_list" />` の直下（374 行目付近）
- **挙動**: タブ型ナビ（横スワイプ）とメインスライダーが双方向で同期する Swiper UI

## 変更内容

### 1. `<head>` 内の追加

- **場所**: `list_tamesu--swiper.css` の link の直前
- **追加**: Swiper 11 の CSS（CDN）

```html
<link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css"
/>
```

### 2. 本文への UI 挿入

- **場所**: `list_tamesu--swiper.html` 374 行目（`<input type="hidden" name="event_name[]" value="tame_list" />`）の直下
- **ラッパー**: `class="category-swiper-wrap"`（既存の `list_tamesu--swiper.css` のスタイルを利用）

挿入したブロックの構成:

| 要素                     | 役割                                                 |
| ------------------------ | ---------------------------------------------------- |
| `.category-swiper-wrap`  | ラッパー（スタイルスコープ）                         |
| `#nav` (`.nav-swiper`)   | タブ型ナビの Swiper（Overview, Specs, Gallery など） |
| `#main` (`.main-swiper`) | メインコンテンツの Swiper（各スライドの `.card`）    |

- ナビのタブ: Overview, Specs, Gallery, Reviews, FAQ, Support, Related（7 スライド）
- メインスライダー: 上記と 1 対 1 で対応する 7 枚のスライド

### 3. `</body>` 直前のスクリプト追加

- **Swiper JS**: `https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js`
- **初期化**: IIFE 内で以下を実行
  - `#nav` でナビ用 Swiper を生成（`slidesPerView: 'auto'`, `centeredSlides: true`, `watchSlidesProgress: true` 等）
  - `#main` でメイン用 Swiper を生成（`thumbs: { swiper: navSwiper }` でナビと連携）
  - ナビの `.nav-btn` クリックでメインを `slideTo(index)`
  - メインの `slideChange` でナビを `slideTo(mainSwiper.activeIndex)`

## 依存関係

| 種別 | 内容                                                              |
| ---- | ----------------------------------------------------------------- |
| CSS  | `list_tamesu--swiper.css` の `.category-swiper-wrap` 以下（既存） |
| JS   | Swiper 11（CDN）                                                  |
| HTML | 挿入ブロック内の `#nav` / `#main` がページ内で一意であること      |

## 元ソースとの対応

- UI の構造と見た目は `mock/index.html` の `<div class="wrap">` 内と同等。
- mock の `.wrap` は本適用では `.category-swiper-wrap` に置き換え、既存 CSS を流用。
- 初期化オプション（`slidesPerView`, `spaceBetween`, `thumbs` 等）は mock の設定を踏襲。

## 注意事項

- `#nav` と `#main` はページ内で他に使わないこと（id の重複を防ぐ）。
- タブやスライドの文言・枚数を変える場合は、ナビの `.swiper-slide` 数とメインの `.swiper-slide` 数を一致させること。
- Swiper のバージョンを変える場合は CDN の URL とオプション名の互換性を確認すること。
