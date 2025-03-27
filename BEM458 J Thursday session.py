#######################################################################################################################################################
# 
# Name:Nikhil Kumar Mohanty
# SID:059061
# Exam Date:27/03/2025
# Module:BEM458
# Github link for this assignment:  https://github.com/UniversityExeterBusinessSchool/practiceassessment-thursday-nikhilmohanty-creator
#
# ######################################################################################################################################################
# Instruction 1. Read the questions and instructions carefully and complete scripts.

# Instruction 2. Only ethical and minimal use of AI is allowed. You might use AI to give advice on how to use a tool or programming language.  
#                You must not use AI to create the code. You might make use of AI to aid debugging of the code.  
#                You must indicate clearly how and where you have used AI.

# Instruction 3. Copy the output of the code and insert it as a comment below your code e.g # OUTPUT (23,45)

# Instruction 4. Ensure you provide comments for the code and the output to show contextual understanding.

# Instruction 5. Upon completing this test, commit to Git, copy and paste your code into the word file and upload the saved file to ELE.
#                There is a leeway on when you need to upload to ELE, however, you must commit to Git at 
#                the end of your session.

# ######################################################################################################################################################
# Question 1 - Loops
# Create a list and use a for loop to answer the following question:
# You are given a dictionary called key_comments. Your allocated keys are the first and last digit of your SID.
# Find the start and end position of each of the items in the sentence using the find command.
# Create and populate a list called my_list with a tuple of (start location, end location) for each value in comments 
 

customer_feedback = """Your recent order experience has been satisfactory overall. While there were some minor issues,
we appreciate the effort made to resolve them promptly."
"""

# List of words to search for
key_comments = {
    0: 'satisfactory',
    1: 'order',
    2: 'effort',
    3: 'issues',
    4: 'promptly',
    5: 'appreciate',
    6: 'experience',
    7: 'resolve',
    8: 'overall',
    9: 'minor'
}



# Write your search code here and provide comments. 

# Initialize an empty list to store (start, end) positions



# Define your allocated keys (First and last digit of your SID)
# Define the given dictionary
key_comments = {
    0: 'satisfactory',
    1: 'order',
    2: 'effort',
    3: 'issues',
    4: 'promptly',
    5: 'appreciate',
    6: 'experience',
    7: 'resolve',
    8: 'overall',
    9: 'minor'
}

# Given
customer_feedback = """Your recent order experience has been satisfactory overall. While there were some minor issues,
we appreciate the effort made to resolve them promptly."
"""

# words SID digits
allocated_words = [key_comments[0], key_comments[1]]  # ['satisfactory', 'order']

# Create the list
my_list = []

# start and end positions
for word in allocated_words:
    start = customer_feedback.find(word)
    if start != -1:
        end = start + len(word) - 1  # End pos
        my_list.append((start, end))

# Printing result
print(my_list)

# Output 

[(38, 49), (12, 16)]


##########################################################################################################################################################

# Question 2 - Functions
# Scenario - You are working in an e-commerce firm as a business analyst, and your manager has tasked you to generate weekly reports on financial metrics like 
# Operating Profit Margin, Revenue per Customer, Customer Churn Rate, and Average Order Value. Use Python functions 
# that will take the values and return the metric needed. Use the first two and last two digits of your ID number as the input values.

# Insert first two digits of ID number here:
# Insert last two digits of ID number here:

# Write your code for Operating Profit Margin

# Write your code for Revenue per Customer

# Write your code for Customer Churn Rate

# Write your code for Average Order Value

# Call your designed functions here
def op(revenue, operating_income):
    return (operating_income / revenue) * 100

def rpc(total_revenue, number_of_customers):
    return total_revenue / number_of_customers

def ccm(lost_customers, total_customers):
    return (lost_customers / total_customers) * 100

def aov(total_revenue, number_of_orders):
    return total_revenue / number_of_orders



print("Operating Profit Margin:", op(75000, 8700))
print("Revenue per Customer:", rpc(7500,87))
print("Customer Churn Rate:", ccm(75, 87))
print("Average Order Value:", aov(75000, 87))


#output

Operating Profit Margin: 11.600000000000001
Revenue per Customer: 86.20689655172414
Customer Churn Rate: 86.20689655172413
Average Order Value: 862.0689655172414


# as a businness analyts i understand that this all metrics and data can help me find out key stats of ecommerce and i can generate more profits and make the business efficient.
##########################################################################################################################################################

# Question 3 - Regression
# A retail store has collected data on seasonal sales and price changes. The table below shows different price levels and their corresponding demand.
# Develop a linear regression model and determine:
# 1. The price at which the store can maximize revenue
# 2. The demand when the price is set at £52

"""
Price (£)    Demand (Units)
---------------------------
20           300
25           280
30           260
35           240
40           210
45           190
50           160
55           140
60           120
65           100
70           85
"""


import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Data
price = np.array([20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]).reshape(-1, 1)
demand = np.array([300, 280, 260, 240, 210, 190, 160, 140, 120, 100, 85])

# Training  Linear Regression Model
model = LinearRegression()
model.fit(prices, demand)

# Predicting  demand at price £52
price_52 = np.array([[52]])
demand_52 = model.predict(price_52)[0]

#  Revenue = Price * Demand
optimal_price = np.linspace(20, 70, 100).reshape(-1, 1)
predicted_demand = model.predict(optimal_price)
revenue = optimal_price.flatten() * predicted_demand
max_revenue_index = np.argmax(revenue)
best_price = optimal_price[max_revenue_index][0]

# Print results
print(f"demand: {demand_52:.2f} units")
print(f"optimal price: £{best_price:.2f}")

# As a analyst i get a lot of major insights throught this analysis which will help me maintain the stocks of my store during festive seasons and can predict the demand too.

#output

demand: 158.17 units
optimal price: £43.74
    
# Write your code here
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Data
price = np.array([20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]).reshape(-1, 1)
demand = np.array([300, 280, 260, 240, 210, 190, 160, 140, 120, 100, 85])

# Training  Linear Regression Model
model = LinearRegression()
model.fit(prices, demand)

# Predicting  demand at price £52
price_52 = np.array([[52]])
demand_52 = model.predict(price_52)[0]

#  Revenue = Price * Demand
optimal_price = np.linspace(20, 70, 100).reshape(-1, 1)
predicted_demand = model.predict(optimal_price)
revenue = optimal_price.flatten() * predicted_demand
max_revenue_index = np.argmax(revenue)
best_price = optimal_price[max_revenue_index][0]

# Print results
print(f"demand: {demand_52:.2f} units")
print(f"optimal price: £{best_price:.2f}")

# As a analyst i get a lot of major insights throught this analysis which will help me maintain the stocks of my store during festive seasons and can predict the demand too.

#output

demand: 158.17 units
optimal price: £43.74

##########################################################################################################################################################

# Question 4 - Debugging; Plotting and data visualization chart

import random
import matplotlib.pyplot as plt

# Generate 100 random numbers between 1 and student id number
max-value = integer(input("Enter your Student ID: "))
random_numbers = [random.randint(1, max_value) for i in range(0,100)]

# Plotting the numbers in a line chart
plt.plot(random_numbers, marker='O', markercolor='green', markeredgcolor='red', linestyle='--', lable='Random Numbers', color='blue');
plt.title(Line Chart of 100 Random Numbers)
plt.xlabel="Index"
plt.ylabel="Random Number"
plt.legend('---')
plt.grid(True)
plt.show()


#answers


Variable Naming:
max-value → hyphen(-) # max_value should be used

function incorrect Usage:
integer(input(...)) → int(input(...)) 


ERROR in plt.plot():
markercolor and markeredgcolor =>  markerfacecolor and markeredgecolor.
lable => label.


String Formatting in plt.title():
'Line Chart of 100 Random Numbers' should be enclosed in quotes.


Assignment Issue:

plt.xlabel="Index" → plt.xlabel("Index") parentheses should be used


plt.legend('---') should be plt.legend(),labels are defined.




