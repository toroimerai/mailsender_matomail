## 30分でアプリ開発してみたシリーズです！

<h2>📩 まとメール（Matomail）</h2>
<p>複数の宛先に一括でメールを送信できる簡単なデスクトップアプリをsmtplibの学習も兼ねてChatGPTのみで作りました</p>
 GUIには ttkbootstrapを使用し、簡単・直感的に操作できます。
 <img width="424" height="819" alt="607abb27770f1c58c8b705a2ddfc1a10" src="https://github.com/user-attachments/assets/c5c93c8d-259e-494a-848a-74d6f5ce1787" />
 
<h2>🖥 主な機能</h2>

✏️ 宛先（名前＋メールアドレス）の登録・削除

✅ 全員選択 / 選択解除機能

📬 Gmail を使ったメール一括送信（アプリパスワード対応）

📜 送信履歴の表示

🛡️ 許可ドメイン（gmail.com）のみ登録可能

⚠️ 重複登録の防止

<h2>⚙️ 必要環境</h2>

**Python 3.10 以上**

**インターネット接続環境**

**Gmail のアプリパスワード
（※2段階認証を有効にして、アプリパスワードを発行
してください）**

<h2> 📦 インストール</h2>

**このリポジトリをクローンまたはZIPでダウンロード**

git clone https://github.com/toroimerai/mailsender_matomail.git
```bash
cd matomail
```

**必要なライブラリをインストール**

```cmd
pip install ttkbootstrap
```
<h2>🚀 使い方</h2>

- main.py を実行

```python
python main.py
```

- アプリが起動したら、以下を入力

- 送信元メール（Gmailアドレス）

- アプリパスワード（16桁の英数字）

- 宛先の「名前」「メールアドレス」を入力して「実行（宛先追加）」

- 宛先をリストから選択

- 件名・本文を入力（本文内で {name} を使うと、宛先名に自動置換されます）

- 「送信」ボタンを押すと選択した宛先に一括送信されます

<h2>⚡ 今後のアップデート予定</h2>
<details>
 <summary>次のバージョンで、以下の機能を追加予定です。</summary>
`追加順にチェックを付けていきます。`
<h3>📁 宛先管理の強化</h3>

CSVやテキストファイルから宛先を一括インポート／エクスポート

- [x] 重複チェック（同じメールアドレスを複数追加できないようにする）

- [ ] 宛先検索機能（名前やメールアドレスでフィルタリング）

<h3>📬 送信機能の強化</h3>

- [ ] BCC / CC 対応（選択宛先をTo以外でも送信）

- [ ] 添付ファイル対応（MIMEBaseを使ったファイル送信）

- [ ] 送信ステータス表示（成功／失敗をリストに表示）

- [ ] 本文プレビュー（{name} 置換後の表示を送信前に確認）

<h3>⚠️ ユーザー操作の安全性</h3>

- [ ] 送信前確認ダイアログ（「○件のメールを送信します。よろしいですか？」を表示）

- [ ] 送信キャンセル（送信中に中断できるように）

<h3>📝 ログ・履歴機能</h3>

- [ ] 日付付き送信ログ（いつ誰に送ったかを記録）

- [ ] 履歴の保存・読み込み（アプリを閉じても履歴を保持）

<h3>🐛 既知の問題（Known Issues）</h3>

- [ ] Gmail以外のSMTPサーバーには未対応です

- [ ] 宛先を大量に追加するとリスト操作がやや重くなることがあります

- [ ] 同じメールアドレスの重複登録を防止するチェックがまだ未実装です

- [ ] 添付ファイルやBCC/CCなどの機能はまだ利用できません（アップデート予定)

**プルリクエスト等是非お願いします！**
</details>

<h2>📚 使用ライブラリ</h2>

smtplib
（標準ライブラリ）: SMTPによるメール送信

email.mime.text.MIMEText
: メール本文作成

tkinter
（標準ライブラリ）: GUI

ttkbootstrap
: モダンなテーマを提供するGUI拡張です

<h2>🧑‍💻 開発者</h2>

作者: Orion/toroimerai

GitHub: @toroimerai

📄 ライセンス
<details>
<summary>クリックして展開</summary>
MIT License

Copyright (c) 2025 Orion

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

このプロジェクトは MIT ライセンスの下で公開されています。
</details>
