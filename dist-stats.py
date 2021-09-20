
import csv
import sys
import pandas as pd

def restaurantCategoryDist(filename, city):

    with open(filename, newline='', encoding="cp437", errors='ignore') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if (row['city'] == city):
                df1 = pd.DataFrame(reader, columns=['Restaurants','categories'])
                dist = df1.State.value_counts()
    return dist


def main():
    # getting input from the terminal
    file = sys.argv[1]
    city = sys.argv[2]

    # each part calls the respectative method
    resCatDist = restaurantCategoryDist(file, city)


    # printing each part in the required format
    print("resCatDist:", resCatDist, " in ", city)



if __name__ == "__main__":
    main()



