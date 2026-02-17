# 実装チーム向け：original → swiper アップデート手順

**目的**: `list_tamesu--original.html`（元ファイル）を、`list_tamesu--swiper.html` と同様の UI（カテゴリナビ ＋ タブ）にアップデートする際の引き継ぎ資料です。

---

## 1. ファイルの役割

| ファイル | 役割 |
|----------|------|
| **list_tamesu--original.html** | 元ファイル。Slick による「タメせる／メディタメ」2タブのみ。カテゴリ（総合・食品・ドリンク…）はなし。 |
| **list_tamesu--swiper.html** | アップデート後の想定形。タメせる／メディタメはタブ、その内側に Swiper でカテゴリナビ（総合・食品・ドリンク…）＋ カテゴリ別カード一覧。 |
| **list_tamesu--swiper.css** | swiper 版専用スタイル（タブ・Swiper・グローバルナビ等）。HTML から相対パスで読み込み。 |
| **list_tamesu--swiper_運用注意点.md** | Swiper 運用時の注意（メニューとコンテンツの数・順序など）。**実装時も参照すること。** |

---


## 2. 既存 MD ファイルの位置づけと更新状況

| ファイル | 内容 | 更新状況 |
|----------|------|----------|
| **list_tamesu--swiper_運用注意点.md** | カテゴリナビ（Swiper）の運用注意（数・順序・HTML 構造・トラブル時確認項目） | 現在の swiper 実装に沿っている。**実装時は必ず参照。** |
| **REFACTORING.md** | Slick → タブナビへのリファクタリング内容（タブの HTML/CSS/JS、sessionStorage、GA 等） | タブ部分の経緯は有効。ただし **list_tamesu--swiper.html は現在 Slick ではなく Swiper でカテゴリナビを実装**しているため、「Slick 削除」の記述はタブまわり（タメせる／メディタメ）の話と理解すること。 |
| **README.md** | リポジトリ概要、Swiper 参考リンク（au モラタメ）、ファイルの役割（HTML/CSS・ドキュメント・スクリプト・PurgeCSS 等）。 | 現状に沿っている。 |

**注意**: 上記 MD は情報が古い・不足している可能性があります。実装時は **list_tamesu--swiper.html / list_tamesu--swiper.css の実装を正とし**、MD は補足として使ってください。

---

## 3. original と swiper の主な差分

### 3.1 ヘッダー・タブ（タメせる／メディタメ）

- **original**
  - Slick: `slick.css` / `slick.min.js` を読み込み。
  - ナビ: `.nav_slider`（中にタメせる・メディタメの 2 スライド）。
  - コンテンツ: `.main_slider`（2 スライド）。Slick の `asNavFor` で連動。
- **swiper**
  - Slick は使わない。タブは **クリックで切り替え**（`.tab-nav-item`, `.tab-content`, `data-tab`）。
  - タブ用クラス: `tab-nav-item`, `active`, `data-tab="0"` / `data-tab="1"`。
  - コンテンツ用: `tab-content`, `active`, `data-tab="0"` / `data-tab="1"`。
  - タブ切り替えは **Vanilla JS（jQuery 非依存）** で実装（sessionStorage・GA・検索/ソートアイコン制御など）。body 末尾付近にあり、REFACTORING.md に概要あり。

### 3.2 カードエリア（タメせる 1 タブ目の中身）

- **original**
  - カテゴリ分けなし。`<div class="container">` → `<ul class="list14 ..." id="content">` の **1 リスト**のみ。
- **swiper**
  - **カテゴリナビ**と**カテゴリ別カード**を Swiper で実装。
  - ラッパー: `.top-c-cards-container`。
  - メニュー用: `.mySwiper2`（`.swiper` > `.swiper-wrapper` > 複数 `.swiper-slide` ＝ 総合・食品・ドリンク…）。
  - コンテンツ用: `.mySwiper3`（`.swiper` > `.swiper-wrapper` > カテゴリ数だけ `.swiper-slide`。各スライド内に `<ul class="list14 ...">` のカードリスト）。
  - Swiper 8 の Controller で「タブ ⇔ コンテンツ」を双方向連動。ループ有効。`loopedSlides` はメニューのスライド数に合わせて設定。

### 3.3 読み込みアセット

- **original**
  - `slick.css`, `slick.min.js`（ヘッダー内）。
- **swiper**
  - **Swiper**: `swiper-bundle.min.css`（head 内）, `swiper-bundle.min.js`（body 末尾）。
  - **専用 CSS**: `list_tamesu--swiper.css`（body 内で相対パス読み込み。タブ・Swiper・グローバルナビなど）。
  - Slick は読み込まない。

### 3.4 JavaScript

- **original**
  - `.nav_slider` / `.main_slider` の Slick 初期化、`slickGoTo`、`slickCurrentSlide`、`slick-center` のスタイル、高さ調整など。
- **swiper**
  - タブ: `.tab-nav-item` クリックで `switchTab(index)`、sessionStorage・GA・表示切替。
  - カテゴリ: `new Swiper(".mySwiper2", ...)` と `new Swiper(".mySwiper3", ...)`、`controller` で連動。`loopedSlides` は `.mySwiper2 .swiper-slide` の数。

---

## 4. original を swiper のようにアップデートする手順（実装チーム向け）

1. **タブ（タメせる／メディタメ）の置き換え**
   - Slick の読み込み（`slick.css` / `slick.min.js`）を削除。
   - `.nav_slider` を、`list_tamesu--swiper.html` と同様のマークアップに変更（`.p-global-nav__menu-list` と `tab-nav-item` / `data-tab`）。
   - `.main_slider` 内の 2 ブロックに `tab-content` / `data-tab` / `active` を付与。
   - タブ切り替え用の Vanilla JS を `list_tamesu--swiper.html` から移植（クリック、sessionStorage、GA、検索/ソートアイコン、必要ならスクロール）。

2. **カードエリアの構造変更（タメせる側）**
   - 「1 リストのみ」の `<div class="container">` を、`.top` > `.top-c-cards-container` に置き換え。
   - その中に `.mySwiper2`（カテゴリ名のスライド）と `.mySwiper3`（カテゴリごとのカードスライド）を追加。
   - カテゴリ名・順序は **list_tamesu--swiper_運用注意点.md** に従い、メニューとコンテンツの**数・順序を一致**させる。

3. **CSS の追加**
   - `list_tamesu--swiper.css` を同じ相対パスで読み込む（または内容を既存 CSS にマージ）。
   - タブ（`.tab-nav-item`, `.tab-content`）および Swiper 用のスタイルが含まれていることを確認。

4. **Swiper の読み込みと初期化**
   - head に `swiper-bundle.min.css`、body 末尾に `swiper-bundle.min.js` を追加。
   - `list_tamesu--swiper.html` 末尾の Swiper 初期化スクリプト（`.mySwiper2` / `.mySwiper3`、`controller`、`loopedSlides`）を移植。

5. **Slick 関連の削除**
   - `.nav_slider` / `.main_slider` の Slick 初期化・イベント・高さ調整などのコードをすべて削除。

---

## 5. 運用・トラブル時の参照

- **list_tamesu--swiper_運用注意点.md**  
  - メニューとコンテンツの数・順序、`.top-c-cards-container` / `.mySwiper2` / `.mySwiper3` の前提、ループ、確認項目。
- **REFACTORING.md**  
  - タブ部分（タメせる／メディタメ）の HTML/CSS/JS 変更内容。
- 実装の正本は **list_tamesu--swiper.html** と **list_tamesu--swiper.css**。MD と矛盾する場合は実装を優先すること。

---

## 6. 実装チェックリスト

- [ ] タメせる／メディタメを Slick からタブ（tab-nav-item / tab-content）に変更した
- [ ] タブ用 JS（クリック・sessionStorage・GA・アイコン制御）を移植した
- [ ] タメせる側に `.top-c-cards-container` ＋ `.mySwiper2` ＋ `.mySwiper3` を追加した
- [ ] カテゴリの数・順序をメニューとコンテンツで一致させた（運用注意点準拠）
- [ ] Swiper の CSS/JS を読み込み、初期化（controller / loopedSlides）を移植した
- [ ] list_tamesu--swiper.css を読み込んだ（または同等スタイルを適用）
- [ ] Slick の読み込み・初期化・関連コードをすべて削除した

---

*このドキュメントは、既存 HTML/CSS を確認したうえで作成しています。実装時は必ず list_tamesu--swiper.html / list_tamesu--swiper.css を正本として参照してください。*
