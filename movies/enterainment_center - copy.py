import fresh_tomatoes
import media
toy_story = media.Movie("Toy story", " A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/ar/thumb/a/ac/ToyStoryARA.png/221px-ToyStoryARA.png",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print (toy_story.storyline)

avatar = media.Movie("Avatar", " A marine on an alien planet",
                        "https://upload.wikimedia.org/wikipedia/ar/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=uZNHIU3uHT4")
#print (avatar.storyline)

#toy_story.show_trailer()

school_of_rock = media.Movie("School of Rock",
                             "Using rock music to learn",
                             "https://upload.wikimedia.org/wikipedia/en/thumb/1/11/School_of_Rock_Poster.jpg/220px-School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")
ratatouille = media.Movie("Ratatouille",
                           "A rat is a chef in paris",
                           "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                           "https://www.youtube.com/watch?v=uVeNEbh3A4U")
midnight_in_paris = media.Movie("Midnight in paris",
                                "going back in time to meet authors",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=BYRWfS2s2v4")

hunger_games = media.Movie("Hunger games",
                           "A relley reet relly show",
                           "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=mfmrPu43DF8")
movies = [toy_story,avatar,school_of_rock,ratatouille,midnight_in_paris,hunger_games]
fresh_tomatoes.open_movies_page(movies)
#print (media.Movie.valid_ratings)
#print (media.Movie.__doc__)
