#coding: utf-8

# Here goes the imports
import csv
import matplotlib.pyplot as plt

# Let's read the data as a list
print("Reading the document...")
with open(r"C:\Udacity\python\BikeShare\chicago_bikeshare_us\chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Let's check how many rows do we have
print("Number of rows:")
print(len(data_list))

# Printing the first row of data_list to check if it worked.
print("Row 0: ")
print(data_list[0])
gender_index = data_list[0].index("Gender")
# It's the data header, so we can identify the columns.


# Printing the second row of data_list, it should contain some data
print("Row 1: ")
print(data_list[1])

input("Press Enter to continue...")
# TASK 1
# TODO: Print the first 20 rows using a loop to identify the data.
print("\n\nTASK 1: Printing the first 20 samples")

# Let's change the data_list to remove the header from it.
data_list = data_list[1:]

# We can access the features through index
# E.g. sample[6] to print gender or sample[-2]
data_list_sub = data_list[0:20]
for x in range(20):
  print(data_list_sub[x])

input("Press Enter to continue...")
# TASK 2
# TODO: Print the `gender` of the first 20 rows

print("\nTASK 2: Printing the genders of the first 20 samples")
for i, line in enumerate(data_list[:20],start=1):
    print(f"Line : {i}\tGender: {line[-2]}")
#for x in range(20):
#  print(data_list_sub[x][gender_index])


# Cool! We can get the rows(samples) iterating with a for and the columns(features) by index.
# But it's still hard to get a column in a list. Example: List with all genders

input("Press Enter to continue...")
# TASK 3
# TODO: Create a function to add the columns(features) of a list in another list in the same order
def column_to_list(data, index):
    """
    Function to add a column values of a List in a new List.
    Args:
        param1: Full list that needs to get a specific column values.
        param1: Index value of the column to be created in a new List.
    Returns:
        List containing the Values of the Specific Column
    
    """
    column_list = []
    # Tip: You can use a for to iterate over the samples, get the feature by index and append into a list
    for y in range(len(data)):
        column_list.append(data[y][index])
  
    #for i in range(20):
    #    print(column_list[i])
    return column_list


# Let's check with the genders if it's working (only the first 20)
print("\nTASK 3: Printing the list of genders of the first 20 samples")
print(column_to_list(data_list, -2)[:20])

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(column_to_list(data_list, -2)) is list, "TASK 3: Wrong type returned. It should return a list."
assert len(column_to_list(data_list, -2)) == 1551505, "TASK 3: Wrong lenght returned."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TASK 3: The list doesn't match."
# -----------------------------------------------------

input("Press Enter to continue...")
# Now we know how to access the features, let's count how many Males and Females the dataset have
# TASK 4
# TODO: Count each gender. You should not use a function to do that.
male = 0
female = 0
genders_list = column_to_list(data_list, -2)
for gender in genders_list:
    if (gender == 'Male'):
        male += 1
    elif (gender == 'Female'):
        female += 1

#male = genders_list.count('Male')
#female = genders_list.count('Female')

# Checking the result
print("\nTASK 4: Printing how many males and females we found")
print("Male: ", male, "\nFemale: ", female)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert male == 935854 and female == 298784, "TASK 4: Count doesn't match."
# -----------------------------------------------------

input("Press Enter to continue...")
# Why don't we creeate a function to do that?
# TASK 5
# TODO: Create a function to count the genders. Return a list
# Should return a list with [count_male, counf_female] (e.g., [10, 15] means 10 Males, 15 Females)
def count_gender(data_list):
    """
    Function to count number of Male and Female of a list.
    Args:
        param1: List containing genders
    Returns:
        List with Male and Female count values. [Male, Female]
    """
    male = 0
    female = 0
    genders_list = column_to_list(data_list, -2)
    for gender in genders_list:
        if (gender == 'Male'):
            male += 1
        elif (gender == 'Female'):
            female += 1
    return [male, female]


print("\nTASK 5: Printing result of count_gender")
print(count_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(count_gender(data_list)) is list, "TASK 5: Wrong type returned. It should return a list."
assert len(count_gender(data_list)) == 2, "TASK 5: Wrong lenght returned."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TASK 5: Returning wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...")
# Now we can count the users, which gender use it the most?
# TASK 6
# TODO: Create a function to get the most popular gender and print the gender as string.
# We expect to see "Male", "Female" or "Equal" as answer.
def most_popular_gender(data_list):
    """
    Function to find the most popular gender in a list (Male or Female)
    Args:
        param1: List containing genders
    Returns:
        String value of most popular gender in the List
    """
    answer = ""
    male, female = count_gender(data_list)
    if male > female:
        answer = "Male"
    elif female > male:
        answer = "Female"
    else:
        answer = "Equal"
    return answer


print("\nTASK 6: Which one is the most popular gender?")
print("Most popular gender is: ", most_popular_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(most_popular_gender(data_list)) is str, "TASK 6: Wrong type returned. It should return a string."
assert most_popular_gender(data_list) == "Male", "TASK 6: Returning wrong result!"
# -----------------------------------------------------

# If it's everything running as expected, check this graph!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantity')
plt.xlabel('Gender')
plt.xticks(y_pos, types)
plt.title('Quantity by Gender')
plt.show(block=True)

input("Press Enter to continue...")
# TASK 7
# TODO: Plot a similar graph for user_types. Make sure the legend is correct.
print("\nTASK 7: Check the chart!")
user_types = column_to_list(data_list, -3)
unique_user_types = set(user_types)
print(unique_user_types)
def count_by_column(column_to_count, unique_val_column):
    """
    Function to calc how many values of a specific column in a List.
    Pass the column of the list that you want to count and the Set of this column.
    Function will return a List containing the Unique Values and the count value.
    Args:
        param1: List of values to count.
        param2: Set of unique values of the List that needs to be count.
    Returns:
        List with unique value and the count value.
    """
    quantities = []
    for value in unique_val_column: 
        quantity_value = 0  
        for column_value in column_to_count:
            if (column_value == value):
               quantity_value += 1 
        quantities.append(quantity_value)
    return [unique_val_column, quantities]

column_values, column_values_counts = count_by_column(user_types, unique_user_types)
print(column_values_counts)
print(column_values)
y_pos = list(range(len(column_values)))
plt.bar(y_pos, column_values_counts)
plt.ylabel('Quantity')
plt.xlabel('User Types')
plt.xticks(y_pos, column_values)
plt.title('Quantity by User Types')
plt.show(block=True)

input("Press Enter to continue...")
# TASK 8
# TODO: Answer the following question
male, female = count_gender(data_list)
print("\nTASK 8: Why the following condition is False?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "There are some empty values."
print("Answer:", answer)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert answer != "Type your answer here.", "TASK 8: Write your own answer!"
# -----------------------------------------------------

input("Press Enter to continue...")
# Let's work with the trip_duration now. We cant get some values from it.
# TASK 9
# TODO: Find the Minimum, Maximum, Mean and Median trip duration.
# You should not use ready functions to do that, like max() or min().
def calc_mean(trip_duration_list):
    """
    Function to calc Mean. This function receives a List of int and return the mean.
    Args:
        param1: List of int.
    Returns:
        Mean value of a List of Int
    """
    trip_sum = 0
    for trip_duration in trip_duration_list:
        trip_sum += trip_duration
    list_mean = float(trip_sum) / len(trip_duration_list)
    return list_mean

def calc_median(trip_duration_list):
    """
    Function to calc Median. This function receives a List of int and return the median.
    Args:
        param1: List of int.
    Returns:
        Median value of a List of Int
    """
    middle_index = (len(trip_duration_list) - 1) // 2
    if (middle_index % 2):
        return trip_duration_list[middle_index]
    else:
        return (trip_duration_list[middle_index] + trip_duration_list[middle_index + 1])/2.0

trip_duration_list = column_to_list(data_list, 2)
trip_duration_list = list(map(int, trip_duration_list))
#print(trip_duration_list[0])
#print(type(trip_duration_list))
trip_duration_list.sort()
#print(type(trip_duration_list))
min_trip = trip_duration_list[0]
max_trip = trip_duration_list[-1]
mean_trip = calc_mean(trip_duration_list)
median_trip = calc_median(trip_duration_list)


print("\nTASK 9: Printing the min, max, mean and median")
print("Min: ", min_trip, "Max: ", max_trip, "Mean: ", mean_trip, "Median: ", median_trip)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert round(min_trip) == 60, "TASK 9: min_trip with wrong result!"
assert round(max_trip) == 86338, "TASK 9: max_trip with wrong result!"
assert round(mean_trip) == 940, "TASK 9: mean_trip with wrong result!"
assert round(median_trip) == 670, "TASK 9: median_trip with wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...")
# TASK 10
# Gender is easy because usually only have a few options. How about start_stations? How many options does it have?
# TODO: Check types how many start_stations do we have using set()
user_types = set(column_to_list(data_list, -5))
print("\nTASK 10: Printing start stations:")
print(len(user_types))
print(user_types)



# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert len(user_types) == 582, "TASK 10: Wrong len of start stations."
# -----------------------------------------------------

input("Press Enter to continue...")
# TASK 11
# Go back and make sure you documented your functions. Explain the input, output and what it do. Example:
# def new_function(param1: int, param2: str) -> list:
     # """
     # Example function with annotations.
     # Args:
     #     param1: The first parameter.
     #     param2: The second parameter.
     # Returns:
     #     List of X values
     #
     # """

input("Press Enter to continue...")
# TASK 12 - Challenge! (Optional)
# TODO: Create a function to count user types without hardcoding the types
# so we can use this function with a different kind of data.
print("Will you face it?")
answer = "yes"

def count_items(column_list):
    """
    Fucntion to count the number items in a List.
    Returning Two list, the Set of Values (unique values) and other with the Count values.
    Args:
        param1: List to count.
    Returns:
        List with set() values to count , List with Count Values. 
    """
    item_types = []
    count_items = []

    item_types = set(column_list)
    for item in item_types:
        quantity = 0
        for column in column_list:
            if (column == item):
                quantity += 1
        count_items.append(quantity)
    return item_types, count_items


if answer == "yes":
    # ------------ DO NOT CHANGE ANY CODE HERE ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTASK 11: Printing results for count_items()")
    print("Types:", types, "Counts:", counts)
    assert len(types) == 3, "TASK 11: There are 3 types of gender!"
    assert sum(counts) == 1551505, "TASK 11: Returning wrong result!"
    # -----------------------------------------------------
