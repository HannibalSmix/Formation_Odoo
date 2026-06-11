from db.database import Base, engine
from sqlalchemy.orm import sessionmaker
from models.user import Users
from models.usergame import UserGames
from models.review import Reviews
from models.publisher import Publishers
from models.gender import Genders, MyEnum
from models.game import EnumPegy, Games
from repository.user_repository import create_user, display_all_user_games_owned_hours_played, display_top_5_users_with_most_total_hours_played, get_all_user, get_all_user_own_games_more_than
from repository.game_repository import create_game, display_all_games_with_total_players_total_hours_played, display_average_rating_per_game, display_top_5_most_purchased_games, get_all_game, get_all_game_from_publisher, get_all_game_from_user, get_all_game_costing_more
from repository.usergames_repository import buy_game, display_number_of_pruchase_per_game, play_game, refund_game
from repository.review_repository import review_game, get_all_reviews_from_game
from repository.publisher_repository import get_all_publisher, display_all_publishers_with_total_games_average_game_price
from datetime import datetime


Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)

with SessionLocal() as session:
    
    print('hello')
    # user = create_user(session, "john_doe", "john@example.com", "USA", datetime(1990, 1, 1), MyEnum.MALE.value)
    # game = create_game(session, "The Legend of Zelda: Breath of the Wild", 59.99, datetime(2017, 3, 3), EnumPegy.PEGI_12, 1)
    # game2 = create_game(session, "Super Mario Odyssey", 49.99, datetime(2017, 10, 27), EnumPegy.PEGI_7, 1)
    # game3 = create_game(session, "Minecraft", 26.95, datetime(2011, 11, 18), EnumPegy.PEGI_7, 7)
    # print(user)
    # user_game = buy_game(session, 12, 33)
    # user_game = play_game(session, 12, 33, -5)
    # review = review_game(session, user_id=10, game_id=33, rating=0, comment="Great game yooo!")
    # is_refunded = refund_game(session, user_id=10, game_id=33)

    # print(is_refunded)

    # users = get_all_user(session)
    # for user in users:
    #     print(user)

    # games = get_all_game(session)
    # for game in games:
    #     print(game)

    # publishers = get_all_publisher(session)
    # for publisher in publishers:
    #     print(publisher)

    # games_from_publisher = get_all_game_from_publisher(session, "Ubisoft")
    # for game in games_from_publisher:
    #     print(game)
        
    # games_from_user = get_all_game_from_user(session, 1)
    # for game in games_from_user:
    #     print(game)

    # reviews = get_all_reviews_from_game(session, 21)
    # for review in reviews:
    #     print(review)
        
    # games_cost = get_all_game_costing_more(session, 60)
    # for game in games_cost:
    #     print(game)

    # users = get_all_user_own_games_more_than(session, 2)
    # for user in users:
    #     print(user.username)

    # display_number_of_pruchase_per_game(session)
    # display_average_rating_per_game(session)
    # display_top_5_most_purchased_games(session)
    # display_top_5_users_with_most_total_hours_played(session)
    # display_all_user_games_owned_hours_played(session)
    
    # display_all_games_with_total_players_total_hours_played(session)

    display_all_publishers_with_total_games_average_game_price(session)