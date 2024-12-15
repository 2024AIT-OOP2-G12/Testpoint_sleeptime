import plotly.graph_objects as go

def fetch_sleep_data():
    """
    仮の睡眠データを取得し、睡眠時間（時間単位）を計算して返します。
    """
    mock_sleep_data = [
        {"user": "User1", "start": "23:00", "end": "07:00"},
        {"user": "User2", "start": "22:30", "end": "06:30"},
        {"user": "User3", "start": "00:00", "end": "10:00"},
        {"user": "User4", "start": "01:00", "end": "10:00"},
        {"user": "User5", "start": "23:30", "end": "10:30"},
    ]

    sleep_durations = []
    for sleep in mock_sleep_data:
        start_hour = int(sleep["start"][:2])
        start_minute = int(sleep["start"][3:])
        end_hour = int(sleep["end"][:2])
        end_minute = int(sleep["end"][3:])

        # 時間を分に換算
        start = start_hour * 60 + start_minute
        if end_hour < start_hour:
            end = (end_hour + 24) * 60 + end_minute
        else:
            end = end_hour * 60 + end_minute

        # 睡眠時間（分）を計算して時間に変換
        duration = abs(end - start) / 60
        sleep_durations.append(duration)

    return sleep_durations


def create_sleep_histogram():
    """
    ヒストグラムを作成し、HTML形式で返します。
    """
    sleep_data = fetch_sleep_data()

    # ヒストグラムの作成
    bin_size = 1  # 1時間ごとのビン
    bins = [i for i in range(int(min(sleep_data)), int(max(sleep_data)) + 2, bin_size)]

    # ヒストグラムデータをプロット
    fig = go.Figure(
        data=go.Histogram(
            x=sleep_data,
            xbins=dict(start=min(bins), end=max(bins), size=bin_size),
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
    return fig.to_html(full_html=False)
