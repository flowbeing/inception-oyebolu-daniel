paths = {
    "Home": ["Store A", "Store B", "Intersection"],
    "Store A": ["Store B", "Home"],
    "Store B": ["School"],
    "School": ["Intersection", "Store B"],
    "Intersection": ["Home", "School"]
}



def shortest_path():
    container = []
    home = "Home"
    school = "School"

    # This it is stressing searching through each elements of items for "School". Even more stressing is searching
    # within the elements themselves to find if "School" exists within their elements and so on.
    # It would be awesome if I could find a way to crawl through elements of the starting point "Home"
    # and their elements with the ability to specify not to repeat already crawled elements until it gets to the end
    # point "School"

    for items in paths:
        for item in paths[items]:
            if item == school:
                container.append(f'{items} => {item}')

            if item != school:
                for i in paths[item]:
                    if i == school:
                        container.append(f"{items} => {item} => {i}")

                    elif i != school:
                        for involved in paths[i]:
                            if involved == school:
                                container.append(f"{items} => {item} => {i} => {involved}")

                            #elif involved != school:
                            #    for involvedd in paths[involved]:
                            #        if involvedd == school:
                            #           container.append(f"{items} => {item} => {i} => {involved} => {involvedd}")

    return sorted(container, key=len)


print("\n".join(item for item in shortest_path() if item.startswith("Home") and item.count("=>")
                == min(item.count("=>") for item in shortest_path() if item.startswith("Home"))))