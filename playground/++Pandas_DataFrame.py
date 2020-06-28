import pandas as pd

table = {
    "Name": ["Daniel", "Wakanda", "Drisk", "Pamela", "King"],
    "Age": [12, 13, 17, 23, 57],
    "Prime": ["Wadanda", "Premium", "Gold", "Titanium", "Magdad"]
}

print(pd.DataFrame(table))

print()

table_plot = []

# Calculating number of rows in the Data Frame
for row in table:
    num_of_rows = len(table[row]) + 1
    break

# Adding the total number of rows to the table_plot
for row in range(num_of_rows):
    table_plot.append([])

# Adding the headings to the Table
for heading in table:
    table_plot[0].append(heading)

num_of_rows_minus_the_heading = num_of_rows - 1
# Populating the Data Frame with data for each row other than the heading:
for row in range(num_of_rows_minus_the_heading):
    for heading in table:
        row_locate = row + 1
        table_plot[(row_locate)].append(table[heading][row])

# Displaying the table (** The table is not yet justified)
for row in table_plot:
    print("     ".join(f"{item}" for item in row))