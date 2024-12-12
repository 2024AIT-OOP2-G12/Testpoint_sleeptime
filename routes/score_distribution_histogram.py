import plotly.graph_objects as px

class ScoreDistributionHistogram:

    def __init__(self):
        pass

    def create(self, counts):
        scores = ["0-50", "51-100", "101-150", "151-200", "201-250", "251-300"]
        # x軸は成績区間、y軸は人数
        fig = px.Figure(data=[px.Bar(x=scores, y=counts)]) 

        # グラフ生成
        fig.update_layout(
            title="成績分布",
            xaxis_title="トータルの成績",
            yaxis_title="人数",
            template="plotly_white"
        )
        fig.write_image("static/graph_test.png")


if __name__ == "__main__":
    # サンプルデータ
    counts = [3, 9, 4, 4, 5, 1]

    # 表示及び出力
    histogram = ScoreDistributionHistogram.create(counts)
    histogram
