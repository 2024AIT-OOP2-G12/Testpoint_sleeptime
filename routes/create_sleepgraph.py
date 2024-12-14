import plotly.graph_objects as go

def plot_sleep_histogram():
    # サンプルデータ（睡眠時間）
    sleep_hours = [
        7.0, 6.5, 8.0, 7.5, 6.0, 7.0, 8.0, 9.0, 7.5, 6.5,
        7.0, 8.5, 6.0, 7.0, 8.0, 7.5, 7.5, 6.5, 9.0, 7.0,
        6.0, 8.0, 8.5, 7.5
    ]

    # ヒストグラムデータを作成
    fig = go.Figure()

    # ヒストグラムを追加
    fig.add_trace(go.Histogram(
        x=sleep_hours,  # X軸データとして睡眠時間を指定
        nbinsx=10,      # ビンの数
        marker=dict(color='blue', line=dict(width=1, color='black'))  # 棒グラフのスタイル
    ))

    # レイアウトを調整（アスペクト比固定 + サイズ指定 + Y軸の範囲設定）
    fig.update_layout(
        title="睡眠時間の分布",
        xaxis_title="睡眠時間 (時間)",
        yaxis_title="人数",
        template="plotly_white",  # 背景スタイル
        bargap=0.1,  # 棒グラフの間隔
        autosize=False,  # 自動調整を無効化
        width=800,  # グラフの幅
        height=600,  # グラフの高さ
        yaxis=dict(range=[0, None])  # Y軸の最小値を0に固定（最大値は自動）
    )

    # グラフを表示
    fig.show()


