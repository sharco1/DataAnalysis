
import csv
import sys
import argparse

def get_data(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return reader

def numOfBus(city, filename):
    # Return an int with number of businesses in a city
    count = 0
    filereader = get_data(filename)
    for row in filereader:
        if(row['city'] == city):
            count = count + 1
    return count


# avgStars: the average number of stars of a business in the city
def avgStars(filename, city):
    sum = 0
    filereader = get_data(filename)
    for row in filereader:
            if (row['city'] == city):
                sum = sum + float(row['stars'])
    return sum


# numOfRestaurants: the number of restaurants in the city
def numOfRestaurants(filename, city):
    count = 0
    filereader = get_data(filename)
    for row in filereader:
            if (row['city'] == city):
                if "Restaurants" in row['categories']:
                    count += 1
    return count


# avgStarsRestaurants: the average number of stars of restaurants in the city
def avgStarsRestaurants(filename, city):
    sum = 0
    filereader = get_data(filename)
    for row in filereader:
            if (row['city'] == city):
                if "Restaurants" in row['categories']:
                    sum = sum + float(row['stars'])
    return sum


# avgNumOfReviews: the average number of reviews for all businesses in the city
def avgNumOfReviews(filename, city):
    sum = 0
    filereader = get_data(filename)
    for row in filereader:
            if (row['city'] == city):
                sum = sum + int(row['review_count'])
    return sum


# avgNumOfReviewsBus: the average number of reviews for restaurants in the city
def avgNumOfReviewsBus(filename, city):
    sum = 0
    filereader = get_data(filename)
    for row in filereader:
            if (row['city'] == city):
                if "Restaurants" in row['categories']:
                    sum = sum + int(row['review_count'])
    return sum


def main():
    filename = sys.argv[1]
    city = sys.argv[2]
    busCount = numOfBus(city, filename)
    return print(busCount, "in", city)


if __name__ == "__main__":
    main()
