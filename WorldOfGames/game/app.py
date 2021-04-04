from flask import Flask
from WorldOfGames.game.MainGame import main_game_class
from WorldOfGames.game.MainScores import score_page

app = Flask(__name__)

if __name__ == '__main__':
    main_game_class().start_game()
    app.register_blueprint(score_page, url_prefix='')
    app.run()
