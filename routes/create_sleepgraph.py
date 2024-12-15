from flask import Flask, render_template_string
import plotly.graph_objects as go
"""
from routes.create_sleepdata import fetch_sleep_data
"""

app = Flask(__name__)

# 睡眠時間のヒストグラムを作成
def create_sleepgraph():
    """
    sleep_data = fetch_sleep_data()
    """
    """if not sleep_data:
        return """
    
    sleep_data = [6.5, 7.0, 8.0, 5.5, 7.5, 6.0, 8.5, 9.0, 6.5, 7.0, 5.0, 6.0, 7.5, 8.0, 5.5]
    # ヒストグラムの作成
    bin_size = 1  # 1時間ごとのビン
    #bins = [i for i in range(int(min(sleep_data)), int(max(sleep_data)) + 2, bin_size)]

    # ヒストグラムデータをプロット
    fig = go.Figure(
        data=go.Histogram(
            x=sleep_data,
            xbins=dict(
            start=0,  # ヒストグラムの開始値
            size=1    # ビン幅（1時間）
        ),
            marker=dict(color="blue"),
        )
    )

    # グラフのレイアウト設定
    fig.update_layout(
        title="睡眠時間と人数のヒストグラム",
        xaxis=dict(title="睡眠時間（時間）"),
        yaxis=dict(
            title="人数",
            tickmode="linear",  # 線形な目盛り設定
            dtick=1,           # Y軸の刻み幅を 1 に設定
        ),
        bargap=0.1,
        width=800,
        height=600,
    )

    # グラフをHTML文字列として返す
    htmlstr = fig.to_html(full_html=False)
    return htmlstr


# Flask ルート
@app.route("/")
def index():
    graph_html = create_sleepgraph()
    # HTML テンプレート
    template = """
    <!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta charset="UTF-8">
        <title>睡眠時間ヒストグラム</title>
    </head>
    <body>
        <h1>睡眠時間と人数のヒストグラム</h1>
        <div>{{ graph | safe }}</div>
    </body>
    </html>
    """
    return render_template_string(template, graph=graph_html)


if __name__ == "__main__":
    app.run(debug=True, port=8080)