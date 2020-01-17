# This program calculates the total amount to be spent on GymingFood.
# A future version will auto update my inventory based on speed of consumption

gymingFoodsAndTheirPrices = {
    "Salad": 1000,
    "Spaghetti[3]": 550,
    "Butter": 450,
    "Tomato & Pepper": 100,
    # "Spice | Condiment": "",
    "Beans[One Kongo]": 500,
    "Dodo Plantain[6]": 500,
    "Oat": 1700,
    # "Milk Carton[36]": "",
    "Bottled watter": 1500,
    "Egg[Crate]": 1200,
    # "Tilapia | Sardine": "",
    "Irish potato[1kg]": 500,
    "Lipton tea[100 bags]": 3500,
    "1 Pack of Sugar": 500,
    "Heinz Mayonnaise": 1200,
    "Heinz Tomato Ketchup": 700
}

for item in gymingFoodsAndTheirPrices:
    print("Length of '" + item + "' is " + str(len(item)))

# 1. Calculating the total value for items in gymingGoodsAndTheirPrices
# 2a. Determining the longest item in gymingGoodsAndTheirPrices and it's length
# 2b. Determining length difference between longest item and other items in gymingFoodsAndTheirPrices
# 3. and assigning tabs and | or spaces to items in gymingFoodsAndTheirPrices

# 1. Total Value
total_container = 0;

# 2a. Determining the longest item and its length
longest_item = ""
# 2a paused

for item in gymingFoodsAndTheirPrices:
    total_container += gymingFoodsAndTheirPrices[item]

    # Statement to determine longest item [2a]
    if len(item) > len(longest_item):
        longest_item = item
        print(longest_item)

# 2a contd.
# Determining the length of the longest item
print("")
print("Longest item = " + str(longest_item))
length_of_longest_item = len(longest_item)
print("Length of longest item = " + str(length_of_longest_item))

# 3 started
tab = "    "
space = " "
length_of_tab = len(tab)
length_of_space = len(space)
# 3 paused

print("New era")
for item in gymingFoodsAndTheirPrices:
    print("Length of current item = " + str(len(item)))

    # 2b. Determining length difference between longest item and other items
    diff_in_length = length_of_longest_item - len(item)

    print("Difference in length = " + str(diff_in_length))

    # 3.i. How to react if the difference in length of longest item current item is greater than 4 and can be
    # fully concealed with tabs only

    if diff_in_length % len(tab) == 0:
        number_of_tabs_to_apply = int((diff_in_length / len(tab)))
        apply_tab = tab * number_of_tabs_to_apply
        print(item + apply_tab + " - " + str(gymingFoodsAndTheirPrices[item]))

    # 3.ii. How to react if the difference in length of longest item and current item is greater than
    # the length of a tab i.e 4 but can't be fully concealed with tabs only but with tabs and space(s)

    elif diff_in_length % len(tab) != 0 and diff_in_length > len(tab):
        from math import floor

        number_of_tabs_in_diff_in_length = floor(diff_in_length / len(tab))
        print("Number of tabs in length difference = " + str(number_of_tabs_in_diff_in_length))

        apply_tab = tab * number_of_tabs_in_diff_in_length
        number_of_space_to_apply = (diff_in_length - (len(tab) * number_of_tabs_in_diff_in_length))
        print("Number of spaces to apply = " + str(number_of_space_to_apply))

        apply_space = space * number_of_space_to_apply

        print(item + apply_tab + apply_space + " - " + str(gymingFoodsAndTheirPrices[item]))

    # 3.iii. What to do if the difference in length of longest item
    # and current item doesn't allow for application of tab(s)

    elif diff_in_length < 4:
        apply_space = space * diff_in_length
        print(item + apply_space + " - " + str(gymingFoodsAndTheirPrices[item]))

print("Total funds required = " + str(total_container))