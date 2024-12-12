from flask import Flask, render_template
from models import initialize_database
from routes import blueprints
from routes.score_distribution_histogram import ScoreDistributionHistogram
from routes.graphs import fetch_sleep_test_data, create_graph
import plotly.graph_objects as go
from routes.create_test_data import ScoreCounter


app = Flask(__name__)

# データベースの初期化
initialize_database()

# 各Blueprintをアプリケーションに登録
for blueprint in blueprints:
    app.register_blueprint(blueprint)


fetch_sleep_test_data()
create_graph()


# ホームページのルート
@app.route('/')
def index():

    #counts = [1, 2, 3, 4, 5, 6]
    score_counter = ScoreCounter()
    score_label, test_data = score_counter.count_scores()
    histogram = ScoreDistributionHistogram()
    histogram.create(test_data)

    graph = create_graph()
    return render_template('index.html', graph = graph)



if __name__ == '__main__':
    app.run(port=8080, debug=True)
