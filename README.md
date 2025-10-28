# YOLO Streamlit

Ultralytics YOLOv8とStreamlitで簡単に物体検出を試せるアプリです。

## セットアップ

依存パッケージが未インストールの場合は、任意の仮想環境で以下を実行してください。

```bash
pip install -e .
```

もしくは `uv` を利用している場合は `uv sync` を実行します。

## 使い方

```bash
streamlit run main.py
```

ブラウザで表示されるアプリ上で、画像をアップロードするかサンプル画像を読み込み、検出結果を確認してください。信頼度やIoUの閾値はサイドバーで調整できます。
