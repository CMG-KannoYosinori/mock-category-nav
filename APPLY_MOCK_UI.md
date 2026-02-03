# mock/index.html UI の適用

`mock/index.html` の「Navigation 付き Slider（Swiper 同期）」UI を `s/app_published/list_tamesu--swiper.html` に挿入した際の適用内容と、その後の修正を記録する。

## 概要

- **元ソース**: `mock/index.html`
- **適用先**: `s/app_published/list_tamesu--swiper.html`
- **挿入位置**: 「タメせる」タブ内の `<input type="hidden" name="event_name[]" value="tame_list" />` の直下（374 行目付近）
- **挙動**: タブ型ナビ（横スワイプ）とメインスライダーが双方向で同期する Swiper UI。ループあり。ロード時は Overview が中央。

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

| 要素                     | 役割                                                   |
| ------------------------ | ------------------------------------------------------ |
| `.category-swiper-wrap`  | ラッパー（スタイルスコープ）                           |
| `#nav` (`.nav-swiper`)   | タブ型ナビの Swiper（Overview, Specs, Gallery など）   |
| `#nav-wrapper`           | ナビのスライドを JS で注入する空の `.swiper-wrapper`   |
| `#main` (`.main-swiper`) | メインコンテンツの Swiper（各スライドの `.card`）      |
| `#main-wrapper`          | メインのスライドを JS で注入する空の `.swiper-wrapper` |

- スライドは静的な HTML ではなく、スクリプト内の配列 `categorySwiperSlides`（`label`, `title`, `desc`）をループしてナビ・メインの HTML を生成し、`#nav-wrapper` / `#main-wrapper` に挿入している。
- タブ: Overview, Specs, Gallery, Reviews, FAQ, Support, Related（7 スライド）。メインスライダーは上記と 1 対 1 で対応。

### 3. CSS の追加（ナビを画面中央に）

- **ファイル**: `list_tamesu--swiper.css`
- **対象**: `.category-swiper-wrap .nav-swiper`
- **追加**: ナビのタブ群を画面中央に寄せるため、以下を指定。

```css
width: fit-content;
max-width: 100%;
margin-left: auto;
margin-right: auto;
```

### 4. `</body>` 直前のスクリプト追加

- **Swiper JS**: `https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js`
- **初期化**: IIFE 内で以下を実行
  1. **データ**: 配列 `categorySwiperSlides` で各スライドの `label` / `title` / `desc` を定義。
  2. **DOM 生成**: `categorySwiperSlides.map(...)` でナビ用・メイン用の HTML を組み立て、`#nav-wrapper` / `#main-wrapper` に `innerHTML` で挿入。
  3. **ナビ用 Swiper**: `#nav` で生成。`slidesPerView: 'auto'`, `centeredSlides: true`, `watchSlidesProgress: true`, **`loop: true`**, **`loopedSlides: slideCount`**, **`initialSlide: 0`**。
  4. **メイン用 Swiper**: `#main` で生成。`thumbs: { swiper: navSwiper }`, **`loop: true`**, **`loopedSlides: slideCount`**, **`initialSlide: 0`**。
  5. **ロード時の中央合わせ**: 生成直後に `navSwiper.slideToLoop(0, 0)` と `mainSwiper.slideToLoop(0, 0)` を実行（第 2 引数 0 で即時）。Overview（先頭）が中央に来る。
  6. **同期**: ナビの `.nav-btn` クリックで `mainSwiper.slideToLoop(index)`。メインの `slideChange` で `navSwiper.slideToLoop(mainSwiper.realIndex)`（ループ時は `realIndex` を使用）。

## 依存関係

| 種別 | 内容                                                                                            |
| ---- | ----------------------------------------------------------------------------------------------- |
| CSS  | `list_tamesu--swiper.css` の `.category-swiper-wrap` 以下（既存＋ナビ中央寄せ）                 |
| JS   | Swiper 11（CDN）                                                                                |
| HTML | 挿入ブロック内の `#nav` / `#main` / `#nav-wrapper` / `#main-wrapper` がページ内で一意であること |

## 元ソースとの対応

- UI の構造と見た目は `mock/index.html` の `<div class="wrap">` 内と同等。
- mock の `.wrap` は本適用では `.category-swiper-wrap` に置き換え、既存 CSS を流用。
- スライドはデータ駆動（配列ループ）に変更。ループ表示・ロード時 Overview 中央は本適用側の拡張。

## 注意事項

- `#nav` と `#main` はページ内で他に使わないこと（id の重複を防ぐ）。
- タブやスライドの文言・枚数を変える場合は、`categorySwiperSlides` の要素を編集すればナビ・メインが一致する。
- Swiper のバージョンを変える場合は CDN の URL とオプション名の互換性を確認すること。
- ループ時は `activeIndex` ではなく `realIndex` で「何枚目か」を判定すること。
