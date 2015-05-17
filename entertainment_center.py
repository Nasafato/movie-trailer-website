import media
import fresh_tomatoes

if __name__ == "__main__":
    
    # Creating list of movies

    movie1 = media.Movie("Finding Nemo",
                         "https://www.youtube.com/watch?v=wZdpNglLbt8",
                         "http://img2.wikia.nocookie.net/__cb20130420022756/disney/images/b/ba/Finding_Nemo-_2003.jpg")
    movie2 = media.Movie("Wreck-it Ralph",
                         "https://www.youtube.com/watch?v=87E6N7ToCxs",
                         "http://www.impawards.com/2012/posters/wreckit_ralph_ver6.jpg")

    movie3 = media.Movie("Ex Machina",
                         "https://www.youtube.com/watch?v=bggUmgeMCdc",
                         "https://notjustpumpkinbread.files.wordpress.com/2015/01/ex-machina-poster-v02.jpg")

    movie4 = media.Movie("Cloud Atlas",
                         "https://www.youtube.com/watch?v=hWnAqFyaQ5s",
                         "http://www.impawards.com/2012/posters/cloud_atlas_ver2_xlg.jpg")

    movie5 = media.Movie("American Hustle",
                         "https://www.youtube.com/watch?v=ST7a1aK_lG0",
                         "http://cdn1.ssninsider.com/wp-content/uploads/2013/12/american-hustle-poster-2.jpg")

    movie6 = media.Movie("Star Trek: Into Darkness",
                         "https://www.youtube.com/watch?v=QAEkuVgt6Aw",
                         "http://www.ew.com/sites/default/files/i/2012/12/03/Star-Trek-Into-Darkness.jpg")

    movies = [movie1, movie2, movie3, movie4, movie5, movie6]

    # Creating webpage from movies
    fresh_tomatoes.open_movies_page(movies)
