import glob
import csv


negative_folder_names = glob.glob("./movie-reviews/negative/*.txt")
positive_folder_names = glob.glob("./movie-reviews/positive/*.txt")

with open('movie_reviews_long.csv', 'a') as out_file:
    writer = csv.writer(out_file)
    for folder_name in positive_folder_names:
        with open(folder_name, 'r') as in_file:
            review = in_file.readline().strip()
            writer.writerow([review, 1])
