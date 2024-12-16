from models import Sleep

# モックデータを取得する関数
def fetch_sleep_data():
    # 仮の睡眠データ (ユーザーごとの睡眠時間: 開始時間と終了時間)
    """mock_sleep_data = [
        {"user": "User1", "start": "23:00", "end": "07:00"},
        {"user": "User2", "start": "22:30", "end": "06:30"},
        {"user": "User3", "start": "00:00", "end": "10:00"},
        {"user": "User4", "start": "01:00", "end": "10:00"},
        {"user": "User5", "start": "23:30", "end": "10:30"},
    ]"""
    sleeps = Sleep.select()
    sleep_start = [sleep.start for sleep in sleeps]
    sleep_end = [sleep.end for sleep in sleeps]

    sleep_durations = []
    for start_list, end_list in zip(sleep_start, sleep_end):
        start_hour = int(start_list[:2])
        start_minute = int(start_list[3:])
        end_hour = int(end_list[:2])
        end_minute = int(end_list[3:])

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