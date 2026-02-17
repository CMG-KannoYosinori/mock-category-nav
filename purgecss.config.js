/**
 * PurgeCSS 設定
 * list_tamesu--swiper.html を解析し、list_tamesu--swiper.css から未使用のスタイルを削除する
 *
 * 実行: npm run purgecss
 * （初回は npm install を実行）
 */
module.exports = {
  content: ['s/app_published/list_tamesu--swiper.html'],
  css: ['s/app_published/list_tamesu--swiper.css'],
  output: 's/app_published/',
  // 出力で元ファイルを上書きする（同じファイル名で output ディレクトリに出力）
  defaultExtractor: (content) => content.match(/[^\s"'<>]*[^\s"'<>]/g) || [],
  // 動的クラスや JS で付与されるクラスを残したい場合は safelist に追加
  safelist: {
    standard: [
      /^active$/,           // .active（タブなど）
      /^swiper-/,           // Swiper が付与するクラス
      /^remodal/,
    ],
    greedy: [],
  },
};
