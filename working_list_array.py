states_of_america = ["Delaware","Pennsylvannia","New York","Connecticut","Massachusetts","Mississippi","Utal"]

# print(states_of_america)  # print all
# print (states_of_america[-1])   # print the last item

# states_of_america.append("Taxes")
# print(states_of_america)               # add to the last position : Taxes

# states_of_america.extend(["Hawai","Alaska","New Mexico"])
# print (states_of_america)           # add 3 states to the end of the list

num_of_america = len(states_of_america)
#print ( states_of_america[num_of_america])

city_name = [" San Jose"," Austin", " Boston", "Atlanta"," Dallas","Colorado", "Los Angeles"]

city_name[-1] = "San Francisco"   # replace the last index Los Angeles = San Fransico
city_name.append(" Houston")  # add Houston after San Franciso

print (city_name)


combination_items = [states_of_america,city_name] # combine 2 arrays States_of_america and City_nam into 1 array 2 dimentions

#print(combination_items)   # print 2 arrays into 1
#print (combination_items[1][1])   # print Austin



