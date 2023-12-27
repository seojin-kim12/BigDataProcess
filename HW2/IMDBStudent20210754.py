import sys

def count_movie(input):
    movie_count = {}

    with open(input, 'r', encoding='utf-8') as file:
        for line in file:
            _, _, genres = line.strip().split('::')
            for genre in genres.split('|'):
                movie_count[genre] = movie_count.get(genre, 0) + 1
    return movie_count

def write_output(outputfile, genre_count):
    with open(outputfile, 'w', encoding='utf-8') as file:
        file.writelines(f'{genre} {count}\n' for genre, count in genre_count.items())

write_output(sys.argv[2], count_movie(sys.argv[1]))