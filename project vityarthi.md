## ONLINE FOOD ORDERING SIMULATION SYSTEM

## A Project Report

B.Tech CSE ( AI & ML )

Course:

Program: B.Tech Computer Science & Engineering (AI & ML)

Institute: VIT Bhopal University

Submitted By:

Omkar Hatwar

Project Technology: Python

Project Type: Console-Based Application

GitHub Repository:

https://github.com/omkarhatwar/online-food-ordering-simulation-system.git

## Project Overview

The Online Food Ordering Simulation System is a Python-based application developed to simulate the basic operations of an online food ordering platform. The system allows users to register and log in, view available food items, search for food, add items to a shopping cart, remove items, calculate the total bill, select a payment method, place orders, and view order history.

The project demonstrates the practical application of Python programming concepts in developing a real-world software solution. It uses a modular approach with separate functions for user management, menu management, cart operations, checkout, and order management.

## PAGE 3 — ABSTRACT, INTRODUCTION & OBJECTIVES

## 1. Abstract

The Online Food Ordering Simulation System is designed to provide a simple simulation of an online food ordering platform using Python. The system provides


users with a convenient way to browse food items, select their desired items, add them to a cart, calculate the total amount, provide delivery information, select a payment method, and place an order.

The application is implemented as a console-based Python program and uses standard Python libraries. It demonstrates important programming concepts such as functions, dictionaries, loops, conditional statements, exception handling, data structures, and modular programming.

The system also maintains user and order information during program execution. Each order is assigned a unique order ID and contains information about the selected food items, quantities, total amount, delivery details, payment method, and order status.

This project provides a foundation for developing a more advanced food ordering application with features such as database storage, graphical user interfaces, online payments, restaurant management, and real-time delivery tracking.

## 2. Introduction

Online food ordering has become an important application of information technology. Customers can select food items, place orders, and receive food without visiting a restaurant physically.

The purpose of this project is to simulate the basic workflow of such a system using Python. Instead of connecting to real restaurants or payment services, the application demonstrates the ordering process in a controlled environment.

The system begins with user registration and login. After successful login, users can access the food menu and perform various operations. They can search for food, add items to their cart, modify quantities, and view the calculated bill. During checkout, the user provides delivery details and selects a payment method. After confirmation, the system generates an order ID and stores the order information.

## 3. Problem Statement

Traditional food ordering may require customers to visit a restaurant or communicate with restaurant staff directly. Managing food items, customer orders, cart information, and billing manually can be inefficient.

The proposed system solves this problem by simulating an automated food ordering process. It provides a structured workflow for selecting food, managing a cart, calculating the bill, and placing orders.

## 4. Objectives

The main objectives of the project are:

- To develop an online food ordering simulation using Python.


- To provide user registration and login functionality.

- To display an organized food menu.

- To allow users to search and select food items.

- To implement shopping cart functionality.

- To calculate the subtotal, delivery charge, and final bill.

- To simulate checkout and payment selection.

- To generate and manage order information.

- To demonstrate practical Python programming concepts.

## PAGE 4 — SYSTEM DESIGN & MODULES

## 5. System Requirements

## Hardware Requirements

- Computer or laptop

- Minimum 4 GB RAM

- Minimum 500 MB free storage

- Keyboard and display

## Software Requirements

- Python 3.x

- Any Python-compatible IDE or code editor

- Operating System: Windows/Linux/macOS

- Git and GitHub for version control

The application uses Python's standard library, so no external Python packages are required for the current version.

- 6. System Workflow

The overall workflow of the system is:

START

|

v

Main Menu


|

+--------+--------+

|

|

|

Register Login View Menu

|

v

User Dashboard

|

+-------+--------+

|

|

|

Menu Search Cart

|

v

Add / Remove

|

v

View Cart

|

v

Checkout

|

v

Delivery Details

|

v

Payment Selection

|

v

Place Order


```
|
v
Order Confirmation
|
v
END
```

## 7. Main Modules

## 7.1 User Registration Module

This module allows a new user to create an account by providing a username and password. The system checks whether the username already exists before creating the account.

## 7.2 Login Module

The login module verifies the username and password entered by the user. Only users with valid credentials can access the user dashboard.

## 7.3 Food Menu Module

The food menu contains different food items along with their categories and prices. Example food items include:

- Veg Burger

- Pizza

- French Fries

- Veg Biryani

- Paneer Butter Masala

- Masala Dosa

- Manchurian

- Cold Drink

- Ice Cream

## 7.4 Search Module

Users can search for a food item by entering its name. The system compares the search keyword with the available menu items and displays matching results.

## 7.5 Cart Module

The cart module allows users to:


- Add food items.

- Specify quantities.

- View selected items.

- Remove items.

- Update quantities.

- Calculate the total amount.

## 7.6 Checkout and Order Module

During checkout, the user enters delivery information and selects a payment method. The system creates an order containing an order ID, customer information, selected items, total amount, payment method, date, and order status.

## PAGE 5 — IMPLEMENTATION & TESTING

## 8. Implementation

The application is implemented using Python. The main source file is:

main.py

The program uses Python dictionaries to store the food menu, users, and orders during execution.

A sample food item is represented as:

```
FOOD_MENU = {
1: {
"name": "Veg Burger",
"category": "Fast Food",
"price": 80
}
}
```

The application uses functions to divide the system into manageable components. Important functions include:

```
register()
login()
display_menu()
```


search_food()

add_to_cart()

view_cart()

remove_from_cart()

checkout()

order_history()

view_order()

user_dashboard()

main()

This modular structure makes the program easier to understand, test, and maintain.

- 9. Billing Process

The system calculates the bill based on the selected quantity and food price.

The calculation follows:

Item Total = Food Price × Quantity

Subtotal = Sum of all Item Totals

Total Amount = Subtotal + Delivery Charge

The current implementation applies a delivery charge of ₹40 when the cart contains

items.

- 10. Payment Methods

The application simulates three payment options:

- 1. Cash on Delivery

- 2. UPI

- 3. Card

No real payment transaction is performed because this is a simulation project.

- 11. Order Management

After successful checkout, the system generates a unique order ID. The order contains:

- Order ID


- Customer name

- Phone number

- Delivery address

- Food items

- Quantity

- Total amount

- Payment method

- Order date and time

- Order status

The initial order status is set to Confirmed.

## 12. Testing

The application can be tested using the following test cases:

## Test Case Input Expected Result

User Registration New username/password Registration successful

Duplicate Registration Existing username

Login

Invalid Login

View Menu

Search Food

Add to Cart

Remove Item

Empty Checkout

Valid Checkout

Order History

- 13. Sample Output

A typical application flow is:

Error message displayed

Correct credentials

User dashboard displayed

Wrong credentials

Login rejected

Menu option

Food menu displayed

Food name

Matching food displayed

Food ID and quantity Item added to cart

Food ID

Item removed/quantity updated

Empty cart

Checkout rejected

Delivery details

Order created

Logged-in user

Previous orders displayed

## ============================================


ONLINE FOOD ORDERING SIMULATION SYSTEM

============================================

1. Register

2. Login

3. View Food Menu

4. Exit

Enter your choice: 2

===== USER LOGIN ===== Enter username: Omkar Hatwar

Enter password: ********

Welcome, Omkar !

1. View Food Menu

2. Search Food

3. Add Food to Cart

4. View Cart

5. Remove Food from Cart

6. Checkout / Place Order

7. Order History

8. View Order

9. Logout

After checkout:

============================================

ORDER PLACED SUCCESSFULLY!

============================================

Order ID : 1001


Customer

Omkar Hatwar

Customer

: Omkar Hatwar

Total Amount : ₹270

Payment Method : UPI

Order Status : Confirmed

============================================

## PAGE 6 — RESULTS, FUTURE SCOPE & CONCLUSION

## 14. Results

The Online Food Ordering Simulation System successfully demonstrates the basic

workflow of an online food ordering application.

The implemented system allows users to:

Create an account.

Log in securely within the application session.

View the available food menu.

Search for food items.

Add food items to a cart.

Change or remove quantities.

Calculate the order amount.

Provide delivery information.

Select a simulated payment method.

Place an order.

- View order history and order details.

The project demonstrates how Python can be used to develop a functional

application by combining multiple programming concepts.

## 15. Advantages

Simple and easy-to-use interface.

Clear food ordering workflow.

- Reduces manual calculation of bills.

- Provides organized cart management.

Generates unique order IDs.


- Demonstrates modular Python programming.

- Easy to extend with additional functionality.

## 16. Limitations

The current version is a simulation and has some limitations:

- User and order data are stored only during program execution.

- No real database is connected.

- No real payment gateway is integrated.

- No real restaurant or delivery service is connected.

- The application currently uses a console interface.

- Real-time delivery tracking is not available.

## 17. Future Scope

The system can be improved in several ways:

- Integration with SQLite or MySQL for permanent data storage.

- Development of a graphical user interface using Tkinter.

- Development of a web interface using Flask or Django.

- Integration of real payment gateways.

- Restaurant management functionality.

- Delivery partner management.

- Real-time order tracking.

- Food ratings and reviews.

- Discount and coupon functionality.

- Email and SMS notifications.

- Mobile application development.

- REST API integration.

## 18. Conclusion

The Online Food Ordering Simulation System is a Python-based project developed to simulate the essential operations of an online food ordering platform. The system provides functionality for user registration, login, food browsing, searching, cart management, billing, checkout, payment selection, and order management.


The project demonstrates practical application of Python programming concepts

such as functions, dictionaries, loops, conditional statements, exception handling,

and modular programming.

Although the current system is designed as a simulation and does not process real

payments or deliveries, it provides a strong foundation for developing a complete

online food ordering application in the future.

19. Repository

GitHub Repository Name:

online-food-ordering-simulation-system

https://github.com/omkarhatwar/online-food-ordering-simulation-system.git

Repository URL:

https://github.com/omkarhatwar/online-food-ordering-simulation-system.git

20. References

Python Documentation  Python programming language concepts and

standard library.

GitHub Documentation  Repository and version-control concepts.

General software engineering concepts related to system design, modular

programming, and software testing.

## STUDENT DETAILS

Name: Omkar Hatwar

Program: B.Tech Computer Science & Engineering ( AI & ML )

Course:

B.Tech CSE ( AI & ML )

Institute: VIT Bhopal University

Submission Type: Flipped Course Evaluation – Build Your Own Project

Project Title: Online Food Ordering Simulation System

Technology: Python

Repository: online-food-ordering-simulation-system
