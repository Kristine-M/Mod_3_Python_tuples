# Create a Python function that takes a list of tuples as an argument. 
# Each tuple contains information about a flight itinerary: (traveler_name, origin, destination). 
# The function should format and return a string that lists each itinerary. For example, 
# if the input is [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")], 
# the output should be a string formatted as:

# "Itinerary 1: Alice - From New York to London
#  Itinerary 2: Bob - From Tokyo to San Francisco"

def itinery(flight_tuple):
    result = ""
    name = ""
    begin = ""
    end = ""
    count = 0
    for tuple in flight_tuple:
        count += 1
        name = tuple[0]
        begin = tuple[1]
        end = tuple[2]
        result += "Itinerary " + str(count) + ": " + name + " - From " + begin + " to " + end + "\n"
    
    return result

res = itinery([("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")])
print(res)
            