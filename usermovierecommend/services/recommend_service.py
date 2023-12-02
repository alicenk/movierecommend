from usermovierecommend.models import Movie
from usermovierecommend.models import User
from usermovierecommend.models import UserMovie


class RecommendService:
    @classmethod
    def recommend_movies_to_users(cls):
        try:
            usermovie = UserMovie.objects.values_list('movie_id', 'user_id') #Daha sonra elasticsearch'den getirilecek
            movie = Movie.objects.all() #Daha sonra elasticsearch'den getirilecek
        except UserMovie.DoesNotExist:
            raise CustomNotFoundException(detail='User not found with the given ID.')
        except Movie.DoesNotExist:
            raise CustomNotFoundException(detail='Movie not found with the given ID.')

        movie_ids = [item[0] for item in movie]
        movie_names = [item[1] for item in movie]
        movie_types = [item[2] for item in movie]

        df_movies = pd.DataFrame({
            'movie_id': movie_ids,
            'name': movie_names,
            'type': movie_types
        })

        movie_ids = [item[0] for item in usermovie]
        user_ids = [item[1] for item in usermovie]

        df_user_movie = pd.DataFrame({
            'user_id': user_ids,
            'movie_id': movie_ids
        })

        reader = Reader(rating_scale=(1, 5))
        data = Dataset.load_from_df(df_user_movie[['user_id', 'movie_id']], reader)

        trainset, testset = train_test_split(data, test_size=0.25)

        model = SVD()
        model.fit(trainset)

        user_movie_types = df_movies[df_movies['movie_id'].isin(df_user_movie[df_user_movie['user_id'] == 1]['movie_id'])][
                'type'].tolist()

        filtered_movies = df_movies[df_movies['type'].isin(user_movie_types)]

        recommendations = []
        for movie_id in filtered_movies['movie_id']:
            if movie_id not in df_user_movie[df_user_movie['user_id'] == 1]['movie_id'].tolist():
                predicted_rating = model.predict(1, movie_id).est
                recommendations.append((movie_id, predicted_rating))

        # En yüksek puan alan 3 filmi seçme
        recommendations.sort(key=lambda x: x[1], reverse=True)
        top_recommendations = recommendations[:3]

        return True
