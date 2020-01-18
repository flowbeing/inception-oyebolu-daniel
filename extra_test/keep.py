def pathway():
    for item in paths:
        for i in paths[item]:
            for it in paths[i]:
                for ite in paths[it]:
                    for itemm in paths[ite]:
                        for itemmm in paths[itemm]:
                            container.append(f'{item} => {i} => {it} => {ite} => {itemm} => {itemmm}')

pathway()
print(len(container))

for item in container:
    if len(set(item.split(" => "))) != len(item.split(" => ")):
        print(f"{item}                  :contains duplicate motion")
    else:
        print(item)

#    return [[[[[[
#        f'{item} => {i} => {it} => {ite} => {itemm} => {itemmm}'
#        for itemmm in paths[itemm]]
#        for itemm in paths[ite]]
#        for ite in paths[it]]
#        for it in paths[i]]
#        for i in paths[item]]
#        for item in paths]


# container = []

#for item in pathway():
#    for i in item:
#        for ii in i:
#            for iii in ii:
#                for iv in iii:
#                    for v in iv:
#                        container.append(v)

#print(container)
#for num, item in enumerate(paths, start=1):
#    print(f"{num}.  From [{item}], you can go to {paths[item]}")
#    for i in paths[item]:
#        print(f"    From [{i}], you can go to {paths[i]}")
#    print("")


#def path(paths):
    #return (f'    {item} gives you access to {paths[item]}\n' + "\n".join([f"    From [{i}], you can go to {paths[i]}"
    #        for i in paths[item]]) for item in paths)
#    return [value
#            for value in paths[i]
#            for i in paths[item]
#            for item in paths]

#for item in path(paths):
#    print(f'{item} \n')