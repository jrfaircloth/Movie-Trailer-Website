import media
import fresh_tomatoes


#Instantiation of movies for trailer website 
war_games = media.Movie("WarGames",
                        "David is a high school student with a talent for computers and gaming. His harmless intentions of hacking into the computer system to play a new unreleased video game result in a threat of a real nuclear war, after he un-intentionally connnects to a military supercomputer. An American thriller about the fear of a nuclear war from the early 1980's.",
                        "http://upload.wikimedia.org/wikipedia/en/2/29/Wargames.jpg",
                        "https://www.youtube.com/watch?v=hbqMuvnx5MU",
                        "PG",
                        "Matthew Broderick, Ally Sheedy, John Wood",
                        "3 June 1983")

pitch_perfect = media.Movie("Pitch Perfect",
                            "Beca, a freshman at Barton University, is cajoled into joining The Bellas, her school's all-girls singing group. Injecting some much needed energy into their repertoire, The Bellas take on their male rivals in a campus competition.",
                            "http://upload.wikimedia.org/wikipedia/en/b/b9/Pitch_Perfect_movie_poster.jpg",
                            "https://www.youtube.com/watch?v=F03N-ApQdmw",
                            "PG-13",
                            "Anna Kendrick, Brittany Snow, Rebel Wilson",
                            "5 October 2012")

gone_girl = media.Movie("Gone Girl",
                        "Based upon the global bestseller by Gillian Flynn -- unearths the secrets at the heart of a modern marriage. On the occasion of his fifth wedding anniversary, Nick Dunne (Ben Affleck) reports that his beautiful wife, Amy (Rosamund Pike), has gone missing. Under pressure from the police and a growing media frenzy, Nick's portrait of a blissful union begins to crumble. Soon his lies, deceits and strange behavior have everyone asking the same dark question: Did Nick Dunne kill his wife?",
                        "http://upload.wikimedia.org/wikipedia/en/0/05/Gone_Girl_Poster.jpg",
                        "https://www.youtube.com/watch?v=iJ5zKeMnQyM",
                        "R",
                        "Ben Affleck, Rosamund Pike, Neil Patrick Harris",
                        "3 October 2014")

star_wars = media.Movie("Star Wars Episode V: The Empire Strikes Back",
                        "After the rebels have been brutally overpowered by the Empire on their newly established base, Luke Skywalker takes advanced Jedi training with Master Yoda, while his friends are pursued by Darth Vader as part of his plan to capture Luke.",
                        "http://upload.wikimedia.org/wikipedia/en/3/3c/SW_-_Empire_Strikes_Back.jpg",
                        "https://www.youtube.com/watch?v=JNwNXF9Y6kY",
                        "PG",
                        "Mark Hamill, Harrison Ford, Carrie Fisher",
                        "20 June 1980")

imitation_game = media.Movie("The Imitation Game",
                             "In The Imitation Game, Benedict Cumberbatch stars as Alan Turing, the genius British mathematician, logician, cryptologist and computer scientist who led the charge to crack the German Enigma Code that helped the Allies win WWII. Turing went on to assist with the development of computers at the University of Manchester after the war, but was prosecuted by the UK government in 1952 for homosexual acts which the country deemed illegal.",
                             "http://ia.media-imdb.com/images/M/MV5BNDkwNTEyMzkzNl5BMl5BanBnXkFtZTgwNTAwNzk3MjE@._V1_SY317_CR0,0,214,317_AL_.jpg",
                             "https://www.youtube.com/watch?v=S5CjKEFb-sM",
                             "PG-13",
                             "Benedict Cumberbatch, Keira Knightley, Matthew Goode",
                             "25 December 2014")

robin_hood = media.Movie("Robin Hood: Men in Tights",
                         "A spoof of Robin Hood in general, and 'Robin Hood: Prince of Thieves' in particular.",
                         "http://upload.wikimedia.org/wikipedia/en/1/12/RobinHoodMeninTights_Poster.jpg",
                         "https://www.youtube.com/watch?v=dX4Ik-cyp-I",
                         "PG-13",
                         "Cary Elwes, Richard Lewis, Roger Rees",
                         "28 July 1993")


#Creates movies list to sent to fresh_tomatoes
movies = [war_games, pitch_perfect, gone_girl, star_wars, imitation_game, robin_hood]
fresh_tomatoes.open_movies_page(movies)

