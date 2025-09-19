import smtplib # SMTPライブラリ
from email.mime.text import MIMEText # メール本文のMIMEタイプ設定
import ttkbootstrap as ttk # ttkbootstrapライブラリ
from ttkbootstrap.constants import * # ttkbootstrap定数
from tkinter import messagebox, Listbox, Text, Scrollbar, RIGHT, Y, END, BOTH, W, E # tkinterコンポーネント

# ----------------- 変数 -----------------
recipients = []  # 宛先リスト
history = []     # 送信履歴
ALLOWED_DOMAINS = ["gmail.com", "yahoo.co.jp"]  # 許可ドメイン

# ----------------- 関数 -----------------

# 宛先追加
def add_recipient():
    name = entry_name.get() # 名前取得
    email = entry_email.get() # メール取得
    if not (name and email): # 空欄チェック
        messagebox.showwarning("警告", "名前とメールアドレスを入力してください") 
        return
# ドメインチェック
    domain = email.split("@")[-1]
    if domain not in ALLOWED_DOMAINS: # 許可ドメインにない場合
        messagebox.showwarning("警告", f"{domain} は許可されていません")
        return
# 重複チェック
    recipients.append((name, email)) # リストに追加
    listbox.insert(END, f"{name} <{email}>") # リストボックスに表示
    entry_name.delete(0, END) # 入力欄クリア
    entry_email.delete(0, END) # 入力欄クリア

# 宛先削除
def remove_recipient(): # 選択された宛先を削除
    selected = listbox.curselection() # 選択されたインデックス取得
    if not selected: # 選択されていない場合
        messagebox.showwarning("警告", "削除する宛先を選択してください")
        return
    index = selected[0] # 最初の選択インデックス
    listbox.delete(index) # リストボックスから削除
    recipients.pop(index) # 宛先リストから削除

# 全員選択
def select_all(): # 全ての宛先を選択
    listbox.select_set(0, END) # 0から最後まで選択

# 選択解除
def deselect_all(): # 選択を解除
    listbox.select_clear(0, END) # 0から最後まで選択解除

# メール送信
def send_emails(): # 選択された宛先にメール送信
    sender = entry_sender.get() # 送信者メール取得
    password = entry_password.get() # 送信者パスワード取得
    subject = entry_subject.get() # 件名取得
    body = text_body.get("1.0", END).strip() # 本文取得
    selected_indices = listbox.curselection() # 選択されたインデックス取得
    selected_count = len(selected_indices)
    if not messagebox.askyesno("送信確認", f"{selected_count} 件のメールを送信します。よろしいですか？"):
        return  # 「いいえ」が選ばれたら送信を中止

    if not sender or not password: # 送信者情報チェック
        messagebox.showerror("エラー", "送信者情報を入力してください")
        return
    if not selected_indices: # 宛先選択チェック
        messagebox.showerror("エラー", "送信する宛先を選択してください")
        return

    try:  # SMTPサーバー接続とメール送信
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender, password)

            for i in selected_indices:
                name, email = recipients[i]
                msg = MIMEText(body.replace("{name}", name), "plain", "utf-8")
                msg["Subject"] = subject
                msg["From"] = sender
                msg["To"] = email
                server.send_message(msg)
                history.append(f"{name} <{email}>")

        # 送信履歴更新
        history_text.configure(state="normal")
        history_text.delete("1.0", END)
        history_text.insert(END, "\n".join(history))
        history_text.configure(state="disabled")

        messagebox.showinfo("成功", "選択した宛先に送信しました！")

    except Exception as e:
        messagebox.showerror("送信エラー", str(e))

    finally:
        # 安全性のためパスワードを破棄
        entry_password.delete(0, END)
        password = None

def execute_action(): # アクション実行
    choice = action_var.get() # 選択されたアクション取得
    if choice == "宛先追加":
        add_recipient() # 宛先追加
    elif choice == "宛先削除":
        remove_recipient()
    elif choice == "全員選択":
        select_all()
    elif choice == "選択解除":
        deselect_all()# 選択解除

# ボタンの色をアクションに応じて変更
def update_button_color(event=None):
    # アクションに応じた色設定
    color_map = {
        "宛先追加": "primary",
        "宛先削除": "danger",
        "全員選択": "info",
        "選択解除": "secondary"
    }
    # ボタンの色を変更
    btn_execute.configure(bootstyle=color_map.get(action_var.get(), "primary"))

# ----------------- UI -----------------

# メインウィンドウ
root = ttk.Window(themename="cosmo") # テーマ設定
root.title("まとメール") # タイトル設定
root.geometry("424x788") # ウィンドウサイズ設定
root.resizable(False, False) # ウィンドウサイズ固定

# メインフレーム
frame = ttk.Frame(root, padding=15)
frame.pack(fill=BOTH, expand=True)

# 送信者情報
ttk.Label(frame, text="送信元メール:").grid(row=0, column=0, sticky=W, pady=5)
entry_sender = ttk.Entry(frame, width=40)
entry_sender.grid(row=0, column=1, pady=5)

# 送信者パスワード
ttk.Label(frame, text="アプリパスワード:").grid(row=1, column=0, sticky=W, pady=5)
entry_password = ttk.Entry(frame, show="*", width=40)
entry_password.grid(row=1, column=1, pady=5)

# 宛先登録
ttk.Label(frame, text="宛先名前:").grid(row=2, column=0, sticky=W, pady=5)
entry_name = ttk.Entry(frame)
entry_name.grid(row=2, column=1, pady=5)

ttk.Label(frame, text="宛先メール:").grid(row=3, column=0, sticky=W, pady=5)
entry_email = ttk.Entry(frame)
entry_email.grid(row=3, column=1, pady=5)

# ボタンフレーム
button_frame = ttk.Frame(frame)
button_frame.grid(row=4, column=0, columnspan=2, pady=5, sticky=W)

# ドロップダウン
action_var = ttk.StringVar(value="宛先追加")
action_menu = ttk.Combobox(button_frame, textvariable=action_var,
values=["宛先追加", "宛先削除", "全員選択", "選択解除"],
state="readonly", width=12)
action_menu.pack(side="left", padx=2)
action_menu.bind("<<ComboboxSelected>>", update_button_color)

# 実行ボタン
btn_execute = ttk.Button(button_frame, text="実行", bootstyle="primary", command=execute_action)
btn_execute.pack(side="left", padx=2)

# 宛先リスト + スクロールバー
listbox_frame = ttk.Frame(frame)
listbox_frame.grid(row=5, column=0, columnspan=2, pady=5)
scrollbar = Scrollbar(listbox_frame)
scrollbar.pack(side=RIGHT, fill=Y)
listbox = Listbox(listbox_frame, width=60, height=6, yscrollcommand=scrollbar.set, selectmode="extended")
listbox.pack(side="left", fill=BOTH)
scrollbar.config(command=listbox.yview)

# 件名
ttk.Label(frame, text="件名:").grid(row=6, column=0, sticky=W, pady=5)
entry_subject = ttk.Entry(frame, width=50)
entry_subject.grid(row=6, column=1, pady=5)

# 本文
ttk.Label(frame, text="本文:").grid(row=7, column=0, sticky=W, pady=5)
text_body = Text(frame, width=50, height=10)
text_body.grid(row=7, column=1, pady=5)

# 送信ボタン
ttk.Button(frame, text="送信", bootstyle="success", command=send_emails).grid(row=8, column=1, sticky=E, pady=15)
# 送信履歴
ttk.Label(frame, text="送信履歴:").grid(row=9, column=0, sticky=W, pady=5)
history_text = Text(frame, width=60, height=8, state="normal")
history_text.grid(row=10, column=0, columnspan=2, pady=5)
history_text.configure(state="disabled")

root.mainloop()
