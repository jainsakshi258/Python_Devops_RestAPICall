import requests
class MovieRatings:
    @staticmethod
    def get_movie_rating_by_name(movie_name):
        url = f'http://www.omdbapi.com/?t={movie_name}&plot=full&apikey=cf59f550'

        response = requests.get(url, ).json()

        for rating in response['Ratings']:
            if rating['Source'] == 'Rotten Tomatoes':
                return rating['Value']
        return "No Rating Found"

    @staticmethod
    def get_movie_rating():
        movie_name = input()
        movie_rating = MovieRatings.get_movie_rating_by_name(movie_name)
        print(movie_rating)
if __name__ == '__main__':
        MovieRatings.get_movie_rating()

