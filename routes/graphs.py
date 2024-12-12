from models import Sleep,Test
import plotly.graph_objects as go

def fetch_sleep_test_data():
    tests = Test.select()
    sleeps = Sleep.select()
    test_user = [test.user for test in tests]
    japanese_score = [test.japanese for test in tests]
    math_score = [test.math for test in tests]
    english_score = [test.english for test in tests]
    test_score = [japanese_score[i] + math_score[i] + english_score[i] for i in range(len(japanese_score))]
    
    sleep_user = [sleep.user for sleep in sleeps]
    
    sleep_start_times = [sleep.start for sleep in sleeps]
    
    
    sleep_end_times = [sleep.end for sleep in sleeps]
    
    
    sleep_dif = []
    for start, end in zip(sleep_start_times, sleep_end_times):
        # 数字文字列を整数に変換
        start_hour = int(start[:2])
        start_minute = int(start[3:])
        end_hour = int(end[:2])
        end_minute = int(end[3:])
        # 時間を分に換算
        if start_hour < end_hour:
            start = start_hour * 60 + start_minute
            end = end_hour * 60 + end_minute
        else:
            start = start_hour * 60 + start_minute
            end = (end_hour+24) * 60 + end_minute
        # 時間の差を計算
        duration = abs(start - end)

        
        sleep_dif.append(duration)
        

    #辞書型にする
    test_dict = dict(zip(test_user,test_score))
    sleep_dict = dict(zip(sleep_user,sleep_dif))
    #必要であれば、配列のキーが両方あることを確認し、どちらかしかないデータは除外する
    # 共通するキーを取得
    common_keys = set(test_dict.keys()).intersection(sleep_dict.keys())
    # 共通部分の辞書を作成
    test_data_dict = {key: test_dict[key] for key in common_keys}
    sleep_data_dict = {key: sleep_dict[key] for key in common_keys}
    #それぞれの配列の値のみを取り出して別の配列(test_data,sleep_data)に格納する
    test_data = list(test_data_dict.values())
    sleep_data = list(sleep_data_dict.values())
    #値を返す
    return test_data, sleep_data



def create_graph():
    """
    graph_path = os.path.join('static', 'graph.png')
    plt.figure(figsize=(6, 4))
    test_data, sleep_data = fetch_user_data()
    graph = plt.scatter(sleep_data, test_data, marker='o', s=5)
    plt.xticks(np.arange(0, 11, 1))  # x軸の目盛りを0～10まで1間隔に設定
    plt.yticks(np.arange(0, 100, 10))  # y軸の目盛りを-1～1まで0.5間隔に設定
    plt.title('Test Scores Transition')
    plt.xlabel('Sleep times')
    plt.ylabel('Score')
    plt.savefig(graph_path)  # グラフをファイルに保存
    plt.close()
    print(f"graph = {graph}")
    return graph_path
    """
    test_data, sleep_data = fetch_sleep_test_data()
    trance_data = go.Scatter(x=sleep_data, y=test_data, mode = 'markers')
    fig = go.Figure(data=trance_data)
    fig.update_layout(title="睡眠時間と点数", 
                    xaxis=dict(title="睡眠時間", tickmode = "array", tickvals = [i*100 for i in range(2401)]),
                    yaxis=dict(title="点数", tickmode = "array", tickvals = [i*30 for i in range(31)]),
                    width = 600,
                    height = 400)
    htmlstr = fig.to_html(full_html = False)
    return htmlstr
