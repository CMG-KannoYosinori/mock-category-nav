# GitHub Pages セットアップ手順

このリポジトリの `list_tamesu.html` をGitHub Pagesで公開するための手順です。

## セットアップ手順

### 1. GitHubリポジトリにプッシュ

変更をコミットしてプッシュしてください：

```bash
git add docs/
git commit -m "Add GitHub Pages setup"
git push origin main
```

### 2. GitHubでGitHub Pagesを有効化

1. GitHubリポジトリのページにアクセス
2. **Settings** タブをクリック
3. 左サイドバーから **Pages** を選択
4. **Source** セクションで：
   - **Branch** を選択
   - ブランチを `main` に設定
   - フォルダを `/docs` に設定
5. **Save** をクリック

### 3. 公開URLの確認

数分待つと、以下のようなURLでアクセスできるようになります：

```
https://<ユーザー名または組織名>.github.io/<リポジトリ名>/
```

例：
```
https://github-cmg.github.io/mock-category-nav/
```

## 注意事項

- GitHub Pagesの反映には数分かかる場合があります
- 初回の公開時は最大10分程度かかることもあります
- ブラウザのキャッシュをクリアして確認してください

## トラブルシューティング

### 404エラーが表示される場合

1. GitHub Pagesの設定で `/docs` フォルダが正しく選択されているか確認
2. `docs/index.html` ファイルが存在するか確認
3. 数分待ってから再度アクセス

### スタイルやスクリプトが読み込まれない場合

- HTMLファイル内の相対パスを確認してください
- 外部リソース（CDNなど）は問題なく読み込めるはずです
