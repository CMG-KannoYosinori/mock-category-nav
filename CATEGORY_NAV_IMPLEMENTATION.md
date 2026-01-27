# Category Navigation Slick 実装内容

## 概要

`mock-slick.html`のUIを`s/app_published/list_tamesu.html`の423行目の上に適用しました。既存のSlickスライダー（`.main_slider`）内に新しいCategory Navigation Slickを実装し、クラス名とIDに`category-`プレフィックスを付与することで競合を回避しています。

## 実装日

2026年1月27日

## 変更内容

### 1. CSSの追加（`</head>`タグの直前）

**位置**: 327行目（`<!-- //ページ固有 Style -->`の後）

**内容**: Category Navigation Slick用のスタイルを追加

```css
<!-- Category Navigation Slick Styles -->
<style>
  :root {
    --category-nav-h: 56px;
    --category-gap: 12px;
  }

  /* ナビ（タブ） */
  .category-nav-slick {
    height: var(--category-nav-h);
    margin-bottom: 12px;
  }

  .category-nav-slick .slick-slide {
    width: auto;
    /* important: 可変幅タブ */
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 0 5px;
    box-sizing: border-box;
  }

  .category-nav-btn {
    appearance: none;
    border: 1px solid rgba(255, 255, 255, 0.18);
    background: rgba(255, 255, 255, 0.06);
    color: #eaeaf0;
    border-radius: 999px;
    padding: 10px 14px;
    font-size: 14px;
    line-height: 1;
    cursor: pointer;
    white-space: nowrap;
    transition: transform 0.15s ease, background 0.15s ease,
      border-color 0.15s ease;
    user-select: none;
    -webkit-tap-highlight-color: transparent;
    width: 100%;
  }

  /* Slickが付与する active を利用して見た目変更 */
  .category-nav-slick .slick-center .category-nav-btn,
  .category-nav-slick .slick-active.slick-center .category-nav-btn {
    background: rgba(99, 102, 241, 0.22);
    border-color: rgba(99, 102, 241, 0.7);
    transform: scale(1.05);
  }

  /* メイン */
  .category-main-slick {
    border-radius: 16px;
    overflow: hidden;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.12);
  }

  .category-main-slick .slick-slide {
    height: 320px;
    display: grid;
    place-items: center;
    padding: 24px;
    box-sizing: border-box;
  }

  .category-card {
    width: 100%;
    height: 100%;
    border-radius: 14px;
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid rgba(255, 255, 255, 0.12);
    display: grid;
    place-items: center;
    text-align: center;
  }

  .category-card h2 {
    margin: 0 0 8px;
    font-size: 24px;
  }

  .category-card p {
    margin: 0;
    opacity: 0.85;
  }

  /* Slickのデフォルト矢印を非表示 */
  .category-nav-slick .slick-arrow,
  .category-main-slick .slick-arrow {
    display: none !important;
  }

  /* Slickのドットを非表示 */
  .category-nav-slick .slick-dots,
  .category-main-slick .slick-dots {
    display: none !important;
  }

  /* 端末が細い場合の高さ調整 */
  @media (max-width: 480px) {
    .category-main-slick .slick-slide {
      height: 260px;
    }
  }
</style>
<!-- //Category Navigation Slick Styles -->
```

### 2. HTMLの追加（423行目の上）

**位置**: 423行目（`<input type="hidden" name="event_name[]" value="tame_list" />`の直前）

**内容**: Category Navigation SlickのHTML構造を追加

```html
<!-- Category Navigation Slick -->
<div class="category-wrap" style="max-width: 960px; margin: 0 auto; padding: 16px; box-sizing: border-box;">
  <!-- ナビゲーション -->
  <div class="category-nav-slick" id="category-nav">
    <div><button class="category-nav-btn" type="button">Overview</button></div>
    <div><button class="category-nav-btn" type="button">Specs</button></div>
    <div><button class="category-nav-btn" type="button">Gallery</button></div>
    <div><button class="category-nav-btn" type="button">Reviews</button></div>
    <div><button class="category-nav-btn" type="button">FAQ</button></div>
    <div><button class="category-nav-btn" type="button">Support</button></div>
    <div><button class="category-nav-btn" type="button">Related</button></div>
  </div>

  <!-- メインコンテンツ -->
  <div class="category-main-slick" id="category-main">
    <div>
      <div class="category-card">
        <div>
          <h2>Overview</h2>
          <p>メインをスワイプしても、上のナビが同期して中央に来ます。</p>
        </div>
      </div>
    </div>
    <div>
      <div class="category-card">
        <div>
          <h2>Specs</h2>
          <p>ナビをスワイプしてタブ選択→メインがスライドします。</p>
        </div>
      </div>
    </div>
    <div>
      <div class="category-card">
        <div>
          <h2>Gallery</h2>
          <p>asNavFor 機能で完全同期（双方向）しています。</p>
        </div>
      </div>
    </div>
    <div>
      <div class="category-card">
        <div>
          <h2>Reviews</h2>
          <p>active なナビは常に中央寄せ（centerMode）。</p>
        </div>
      </div>
    </div>
    <div>
      <div class="category-card">
        <div>
          <h2>FAQ</h2>
          <p>タブは可変幅（variableWidth）。</p>
        </div>
      </div>
    </div>
    <div>
      <div class="category-card">
        <div>
          <h2>Support</h2>
          <p>クリックでもスワイプでも同期。</p>
        </div>
      </div>
    </div>
    <div>
      <div class="category-card">
        <div>
          <h2>Related</h2>
          <p>必要ならURL連動やHash連動も追加できます。</p>
        </div>
      </div>
    </div>
  </div>
</div>
<!-- //Category Navigation Slick -->
```

### 3. JavaScriptの追加（既存のSlick初期化スクリプトの後）

**位置**: 5051行目（既存のSlick初期化スクリプトの`</script>`タグの後）

**内容**: Category Navigation Slickの初期化スクリプトを追加

```javascript
<script>
  // Category Navigation Slick 初期化
  $(document).ready(function() {
    // 既存のSlickが初期化された後に実行されるように、少し遅延させる
    setTimeout(function() {
      // 1) ナビ（タブ）
      $('#category-nav').slick({
        variableWidth: true,        // 可変幅タブ
        centerMode: true,            // アクティブを中央に寄せる
        centerPadding: '0px',       // 中央寄せ時のパディング
        slidesToShow: 1,            // 中央に1つ表示
        slidesToScroll: 1,
        infinite: true,
        speed: 300,
        asNavFor: '#category-main',          // メインと同期（ナビ→メイン）
        focusOnSelect: true,        // クリックでフォーカス移動
        swipe: true,
        touchMove: true,
      });

      // 2) メイン
      $('#category-main').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        infinite: true,
        speed: 420,
        asNavFor: '#category-nav',           // ナビと同期（メイン→ナビ）
        swipe: true,
        touchMove: true,
        arrows: false,              // 矢印非表示
        dots: false,                // ドット非表示
      });

      // クリック対象が button の場合でも確実に動くように補強
      $('#category-nav .category-nav-btn').on('click', function() {
        const index = $(this).closest('.slick-slide').data('slick-index');
        $('#category-main').slick('slickGoTo', index);
      });

      // 追加の補強：メインが変わった時、ナビを中央へ寄せる
      $('#category-main').on('afterChange', function(event, slick, currentSlide) {
        $('#category-nav').slick('slickGoTo', currentSlide);
      });
    }, 100);
  });
</script>
```

## 実装のポイント

### 1. クラス名・IDの命名規則

既存のSlickスライダー（`.main_slider`、`.nav_slider`）と競合しないよう、すべてのクラス名とIDに`category-`プレフィックスを付与：

- `nav-slick` → `category-nav-slick`
- `main-slick` → `category-main-slick`
- `nav` → `category-nav`
- `main` → `category-main`
- `nav-btn` → `category-nav-btn`
- `card` → `category-card`
- `wrap` → `category-wrap`

### 2. Slickのネスト対応

既存の`.main_slider`内に新しいSlickスライダーを配置するため、以下の対策を実施：

- **初期化タイミング**: 既存のSlick初期化後に実行されるよう、`setTimeout`で100msの遅延を設定
- **独立したID/クラス**: 既存のSlickと完全に分離されたID/クラス名を使用
- **asNavFor設定**: 新しいCategory Navigation Slick同士で同期（`#category-nav` ↔ `#category-main`）

### 3. 機能

- **双方向同期**: `asNavFor`を使用してナビゲーションとメインコンテンツを双方向で同期
- **可変幅タブ**: `variableWidth: true`でタブの幅を可変に
- **中央寄せ**: `centerMode: true`でアクティブなタブを中央に配置
- **クリック対応**: タブボタンのクリックでメインコンテンツを切り替え
- **スワイプ対応**: タッチデバイスでのスワイプ操作に対応

## 注意事項

1. **既存のSlickとの競合**: クラス名とIDを変更することで競合を回避していますが、既存のSlickの動作に影響がないか確認が必要です。

2. **初期化タイミング**: 100msの遅延を設定していますが、ページの読み込み速度によっては調整が必要な場合があります。

3. **コンテンツのカスタマイズ**: 現在はサンプルコンテンツ（Overview、Specs、Gallery等）が入っています。実際のコンテンツに合わせて変更してください。

4. **レスポンシブ対応**: 480px以下の端末では、メインスライダーの高さが260pxに調整されます。

## 参考ファイル

- 元のUI: `mock-slick.html`
- 実装先: `s/app_published/list_tamesu.html`
