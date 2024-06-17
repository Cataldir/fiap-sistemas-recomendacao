import pandas as pd
from typing import List


from aula_02.schemas import UserInteractions, UserProfile


class Exploiter:
    def __init__(self, movies_metadata: pd.DataFrame, ratings: pd.DataFrame):
        self.movies_metadata = movies_metadata
        self.ratings = ratings  # Assume ratings are passed during initialization

    def get_popular_movies(self, top_n: int = 10) -> pd.DataFrame:
        popular_movies = self.movies_metadata.sort_values(
            by=["vote_count", "vote_average"], ascending=False
        )
        return popular_movies.head(top_n)

    def recommend_by_exploration(self, user_interactions: UserInteractions) -> List[int]:
        total_interactions = sum(user_interactions.interactions.values())
        weights = {item_id: count / total_interactions for item_id, count in user_interactions.interactions.items()}
        return list(weights.keys())

    def exploit_similar_profiles(self, user_profile: UserProfile, all_user_profiles: pd.DataFrame) -> List[int]:
        similar_users = all_user_profiles[
            (all_user_profiles["profession"] == user_profile.profession) &
            (abs(all_user_profiles["age"] - user_profile.age) <= 5)
        ]
        similar_user_ids = similar_users["user_id"].tolist()
        similar_user_ratings = self.ratings[self.ratings["user_id"].isin(similar_user_ids)]
        recommended_movies = similar_user_ratings.groupby("movie_id")["rating"].mean().reset_index()
        top_movies = recommended_movies.sort_values(by="rating", ascending=False).head(10)["movie_id"].tolist()
        return top_movies


def main():
    movies_metadata = pd.read_csv("movies_metadata.csv")
    ratings = pd.read_csv("ratings.csv")  # Ensure this is loaded appropriately
    recommender = Exploiter(movies_metadata, ratings)

    popular_movies = recommender.get_popular_movies()
    user_interactions = UserInteractions(user_id=1, interactions={101: 5, 102: 3, 103: 2})
    explored_recommendations = recommender.recommend_by_exploration(user_interactions)

    user_profile = UserProfile(user_id=1, age=25, gender="male", profession="engineer")  # Adjusted for correct type
    all_user_profiles = pd.DataFrame()  # Load or simulate user profiles DataFrame

    exploited_recommendations = recommender.exploit_similar_profiles(user_profile, all_user_profiles)

    print("Popular Movies:", popular_movies)
    print("Explored Recommendations:", explored_recommendations)
    print("Exploited Recommendations:", exploited_recommendations)

if __name__ == "__main__":
    main()
