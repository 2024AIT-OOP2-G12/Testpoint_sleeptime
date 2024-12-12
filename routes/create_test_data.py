from models import Test

class ScoreCounter:
    def __init__(self):
        """
        ScoreCounterを初期化する。
        x_labels: 点数範囲を表す文字列のリスト ["0~50", "51~100", ...]。デフォルトは以下の通り。
        """
        self.x_labels = ("0~50", "51~100", "101~150", "151~200", "201~250", "251~300")
        self.score_counts = [0] * len(self.x_labels)  # 点数範囲ごとのカウントを格納するリスト

    def count_scores(self):
        """
        データベースからテストデータを取得し、点数範囲ごとのカウントを実行する。
        """
        # 全てのテストデータを取得
        tests = Test.select()

        # 各テストデータの合計点数を計算し、対応する範囲のカウントを増加
        for test in tests:
            total_score = test.japanese + test.math + test.english  # 3教科の合計点数

            # 合計点数がどの範囲に属するかを判断してカウント
            if 0 < total_score <= 50:
                self.score_counts[0] += 1
            elif 50 < total_score <= 100:
                self.score_counts[1] += 1
            elif 100 < total_score <= 150:
                self.score_counts[2] += 1
            elif 150 < total_score <= 200:
                self.score_counts[3] += 1
            elif 200 < total_score <= 250:
                self.score_counts[4] += 1
            elif 250 < total_score <= 300:
                self.score_counts[5] += 1

        return self.x_labels, self.score_counts