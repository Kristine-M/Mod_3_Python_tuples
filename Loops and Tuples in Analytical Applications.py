#task 1

# You have been provided with stock market data, where each data point is a tuple 
# containing a company's stock symbol, the date, and the closing price. Your task 
# is to analyze this data to find the average closing price of a specified stock 
# over a given period.

# Sample Data:

stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("2021-01-01", 220.0)
    # More data...
]
# Create a function to calculate the average closing price of a specific stock symbol over all dates.
# Ensure your solution handles cases where the stock symbol does not exist in the data.

def stock_avg(stock_data):
    sum = 0
    for stock in stock_data:
        sum += stock[-1]
        
    return sum/len(stock_data)

print(stock_avg(stock_data))

#task 2

# Your goal is to manage an attendance system for various events. 
# Each attendee's data is stored as a tuple containing their name and 
# the event they attended.

# Develop a function to list all attendees of a specific event.
# Implement a feature to count the number of attendees for each event.
# Example Attendee Data:

attendees = [
    ("Alice", "Python Conference"),
    ("Bob", "Python Conference"),
    ("Charlie", "AI Summit")
    # More attendees...
]

def attendence(attendees, event):
    all_attendees = []
    num_attendees = 0
    
    for person in attendees:
        if person[-1] == event:
            num_attendees += 1
            all_attendees.append(person[0])
            
    return all_attendees, num_attendees

all_attendence, num_attendees = attendence(attendees, "Python Conference")

print(all_attendence)
print(num_attendees)
