import glob
import csv


# get all text files
negative_folder_names = glob.glob("./movie-reviews/negative/*.txt")
positive_folder_names = glob.glob("./movie-reviews/positive/*.txt")

with open('movie_reviews.csv', 'a') as out_file:
    writer = csv.writer(out_file)
    for folder_name in positive_folder_names:
        with open(folder_name, 'r') as in_file:
            review = in_file.readline().strip()
            review_word_length = len(review.split())
            if (review_word_length < 512):
                writer.writerow([review, 1])
