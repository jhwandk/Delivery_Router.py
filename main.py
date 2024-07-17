# Student ID: 005838884
# Student Name: Jinhwan Kim
"""
This program includes packages_data which is inserted into a hash table object with a hash method and insert method.
The program also includes distances_data consisting distance in miles from each delivery address to another.
The simulation function will use nearest neighbor algorithm to determine the route.
The nearest neighbor algorithm uses lookup method and distance_data to retrieve data about the packages.
These data are used to calculate  the distance and time required and spent.
The Interface allows user input to call the simulation function to a certain time of a day.
Then the interface, with the help of the lookup method, outputs the package_id, truck_number, delivery_status,
delivery time, and total distance traveled by all trucks.
"""


# Data set of packages
# package id, delivery address, delivery deadline, delivery city, delivery zip code, package weight, delivery status, truck number
packages_data = [
    (1, "195 W Oakland Ave", "10:30 AM", "Salt Lake City", 84115, 21, "At the hub", 3),
    (2, "2530 S 500 E", "EOD", "Salt Lake City", 84106, 44, "At the hub", 3),
    (3, "233 Canyon Rd", "EOD", "Salt Lake City", 84103, 2, "At the hub", 2),
    (4, "380 W 2880 S", "EOD", "Salt Lake City", 84115, 4, "At the hub", 3),
    (5, "410 S State St", "EOD", "Salt Lake City", 84111, 5, "At the hub", 3),
    (6, "3060 Lester St", "10:30 AM", "West Valley City", 84119, 88, "At the hub", 3),
    (7, "1330 2100 S", "EOD", "Salt Lake City", 84106, 8, "At the hub", 3),
    (8, "300 State St", "EOD", "Salt Lake City", 84103, 9, "At the hub", 3),
    (9, "300 State St", "EOD", "Salt Lake City", 84103, 2, "At the hub", 3),
    (10, "600 E 900 South", "EOD", "Salt Lake City", 84105, 1, "At the hub", 3),
    (11, "2600 Taylorsville Blvd", "EOD", "Salt Lake City", 84118, 1, "At the hub", 3),
    (12, "3575 W Valley Central Station bus Loop", "EOD", "West Valley City", 84119, 1, "At the hub", 2),
    (13, "2010 W 500 S", "10:30 AM", "Salt Lake City", 84104, 2, "At the hub", 1),
    (14, "4300 S 1300 E", "10:30 AM", "Millcreek", 84117, 88, "At the hub", 1),
    (15, "4580 S 2300 E", "9:00 AM", "Holladay", 84117, 4, "At the hub", 1),
    (16, "4580 S 2300 E", "10:30 AM", "Holladay", 84117, 88, "At the hub", 1),
    (17, "3148 S 1100 W", "EOD", "Salt Lake City", 84119, 2, "At the hub", 1),
    (18, "1488 4800 S", "EOD", "Salt Lake City", 84123, 6, "At the hub", 2),
    (19, "177 W Price Ave", "EOD", "Salt Lake City", 84115, 37, "At the hub", 1),
    (20, "3595 Main St", "10:30 AM", "Salt Lake City", 84115, 37, "At the hub", 1),
    (21, "3595 Main St", "EOD", "Salt Lake City", 84115, 3, "At the hub", 1),
    (22, "6351 South 900 East", "EOD", "Murray", 84121, 2, "At the hub", 1),
    (23, "5100 South 2700 West", "EOD", "Salt Lake City", 84118, 5, "At the hub", 1),
    (24, "5025 State St", "EOD", "Murray", 84107, 7, "At the hub", 1),
    (25, "5383 S 900 East #104", "10:30 AM", "Salt Lake City", 84117, 7, "At the hub", 3),
    (26, "5383 S 900 East #104", "EOD", "Salt Lake City", 84117, 25, "At the hub", 1),
    (27, "1060 Dalton Ave S", "EOD", "Salt Lake City", 84104, 5, "At the hub", 1),
    (28, "2835 Main St", "EOD", "Salt Lake City", 84115, 7, "At the hub", 3),
    (29, "1330 2100 S", "10:30 AM", "Salt Lake City", 84106, 2, "At the hub", 2),
    (30, "300 State St", "10:30 AM", "Salt Lake City", 84103, 1, "At the hub", 2),
    (31, "3365 S 900 W", "10:30 AM", "Salt Lake City", 84119, 1, "At the hub", 2),
    (32, "3365 S 900 W", "EOD", "Salt Lake City", 84119, 1, "At the hub", 3),
    (33, "2530 S 500 E", "EOD", "Salt Lake City", 84106, 1, "At the hub", 3),
    (34, "4580 S 2300 E", "10:30 AM", "Holladay", 84117, 2, "At the hub", 2),
    (35, "1060 Dalton Ave S", "EOD", "Salt Lake City", 84104, 88, "At the hub", 3),
    (36, "2300 Parkway Blvd", "EOD", "West Valley City", 84119, 88, "At the hub", 2),
    (37, "410 S State St", "10:30 AM", "Salt Lake City", 84111, 2, "At the hub", 2),
    (38, "410 S State St", "EOD", "Salt Lake City", 84111, 9, "At the hub", 2),
    (39, "2010 W 500 S", "EOD", "Salt Lake City", 84104, 9, "At the hub", 3),
    (40, "380 W 2880 S", "10:30 AM", "Salt Lake City", 84115, 45, "At the hub", 2)
]

# Data set of distances from one location to another in miles
distances_data = {
    "4001 South 700 East": {
        "4001 South 700 East": 0.0, "1060 Dalton Ave S": 7.2, "1330 2100 S": 3.8, "1488 4800 S": 11.0,
        "177 W Price Ave": 2.2, "195 W Oakland Ave": 3.5, "2010 W 500 S": 10.9, "2300 Parkway Blvd": 8.6,
        "233 Canyon Rd": 7.6, "2530 S 500 E": 2.8, "2600 Taylorsville Blvd": 6.4, "2835 Main St": 3.2,
        "300 State St": 7.6, "3060 Lester St": 5.2, "3148 S 1100 W": 4.4, "3365 S 900 W": 3.7,
        "3575 W Valley Central Station bus Loop": 7.6, "3595 Main St": 2.0, "380 W 2880 S": 3.6,
        "410 S State St": 6.5, "4300 S 1300 E": 1.9, "4580 S 2300 E": 3.4, "5025 State St": 2.4,
        "5100 South 2700 West": 6.4, "5383 S 900 East #104": 2.4, "600 E 900 South": 5.0, "6351 South 900 East": 3.6
    },
    "1060 Dalton Ave S": {
        "4001 South 700 East": 7.2, "1060 Dalton Ave S": 0.0, "1330 2100 S": 7.1, "1488 4800 S": 6.4,
        "177 W Price Ave": 6.0, "195 W Oakland Ave": 4.8, "2010 W 500 S": 1.6, "2300 Parkway Blvd": 2.8,
        "233 Canyon Rd": 4.8, "2530 S 500 E": 6.3, "2600 Taylorsville Blvd": 7.3, "2835 Main St": 5.3,
        "300 State St": 4.8, "3060 Lester St": 3.0, "3148 S 1100 W": 4.6, "3365 S 900 W": 4.5,
        "3575 W Valley Central Station bus Loop": 7.4, "3595 Main St": 6.0, "380 W 2880 S": 5.0,
        "410 S State St": 4.8, "4300 S 1300 E": 9.5, "4580 S 2300 E": 10.9, "5025 State St": 8.3,
        "5100 South 2700 West": 6.9, "5383 S 900 East #104": 10.0, "600 E 900 South": 4.4, "6351 South 900 East": 13.0
    },
    "1330 2100 S": {
        "4001 South 700 East": 3.8, "1060 Dalton Ave S": 7.1, "1330 2100 S": 0.0, "1488 4800 S": 9.2,
        "177 W Price Ave": 4.4, "195 W Oakland Ave": 2.8, "2010 W 500 S": 8.6, "2300 Parkway Blvd": 6.3,
        "233 Canyon Rd": 5.3, "2530 S 500 E": 1.6, "2600 Taylorsville Blvd": 10.4, "2835 Main St": 3.0,
        "300 State St": 5.3, "3060 Lester St": 6.5, "3148 S 1100 W": 5.6, "3365 S 900 W": 5.8,
        "3575 W Valley Central Station bus Loop": 5.7, "3595 Main St": 4.1, "380 W 2880 S": 3.6,
        "410 S State St": 4.3, "4300 S 1300 E": 3.3, "4580 S 2300 E": 5.0, "5025 State St": 6.1,
        "5100 South 2700 West": 9.7, "5383 S 900 East #104": 6.1, "600 E 900 South": 2.8, "6351 South 900 East": 7.4
    },
    "1488 4800 S": {
        "4001 South 700 East": 11.0, "1060 Dalton Ave S": 6.4, "1330 2100 S": 9.2, "1488 4800 S": 0.0,
        "177 W Price Ave": 5.6, "195 W Oakland Ave": 6.9, "2010 W 500 S": 8.6, "2300 Parkway Blvd": 4.0,
        "233 Canyon Rd": 11.1, "2530 S 500 E": 7.3, "2600 Taylorsville Blvd": 1.0, "2835 Main St": 6.4,
        "300 State St": 11.1, "3060 Lester St": 3.9, "3148 S 1100 W": 4.3, "3365 S 900 W": 4.4,
        "3575 W Valley Central Station bus Loop": 7.2, "3595 Main St": 5.3, "380 W 2880 S": 6.0,
        "410 S State St": 10.6, "4300 S 1300 E": 5.9, "4580 S 2300 E": 7.4, "5025 State St": 4.7,
        "5100 South 2700 West": 0.6, "5383 S 900 East #104": 6.4, "600 E 900 South": 10.1, "6351 South 900 East": 10.1
    },
    "177 W Price Ave": {
        "4001 South 700 East": 2.2, "1060 Dalton Ave S": 6.0, "1330 2100 S": 4.4, "1488 4800 S": 5.6,
        "177 W Price Ave": 0.0, "195 W Oakland Ave": 1.9, "2010 W 500 S": 7.9, "2300 Parkway Blvd": 5.1,
        "233 Canyon Rd": 7.5, "2530 S 500 E": 2.6, "2600 Taylorsville Blvd": 6.5, "2835 Main St": 1.5,
        "300 State St": 7.5, "3060 Lester St": 3.2, "3148 S 1100 W": 2.4, "3365 S 900 W": 2.7,
        "3575 W Valley Central Station bus Loop": 1.4, "3595 Main St": 0.5, "380 W 2880 S": 1.7,
        "410 S State St": 6.5, "4300 S 1300 E": 3.2, "4580 S 2300 E": 5.2, "5025 State St": 2.5,
        "5100 South 2700 West": 6.0, "5383 S 900 East #104": 4.2, "600 E 900 South": 5.4, "6351 South 900 East": 5.5
    },
    "195 W Oakland Ave": {
        "4001 South 700 East": 3.5, "1060 Dalton Ave S": 4.8, "1330 2100 S": 2.8, "1488 4800 S": 6.9,
        "177 W Price Ave": 1.9, "195 W Oakland Ave": 0.0, "2010 W 500 S": 6.3, "2300 Parkway Blvd": 4.3,
        "233 Canyon Rd": 4.5, "2530 S 500 E": 1.5, "2600 Taylorsville Blvd": 8.7, "2835 Main St": 0.8,
        "300 State St": 4.5, "3060 Lester St": 3.9, "3148 S 1100 W": 3.0, "3365 S 900 W": 3.8,
        "3575 W Valley Central Station bus Loop": 5.7, "3595 Main St": 1.9, "380 W 2880 S": 1.1,
        "410 S State St": 3.5, "4300 S 1300 E": 4.9, "4580 S 2300 E": 6.9, "5025 State St": 4.2,
        "5100 South 2700 West": 9.0, "5383 S 900 East #104": 5.9, "600 E 900 South": 3.5, "6351 South 900 East": 7.2
    },
    "2010 W 500 S": {
        "4001 South 700 East": 10.9, "1060 Dalton Ave S": 1.6, "1330 2100 S": 8.6, "1488 4800 S": 8.6,
        "177 W Price Ave": 7.9, "195 W Oakland Ave": 6.3, "2010 W 500 S": 0.0, "2300 Parkway Blvd": 4.0,
        "233 Canyon Rd": 4.2, "2530 S 500 E": 8.0, "2600 Taylorsville Blvd": 8.6, "2835 Main St": 6.9,
        "300 State St": 4.2, "3060 Lester St": 4.2, "3148 S 1100 W": 8.0, "3365 S 900 W": 5.8,
        "3575 W Valley Central Station bus Loop": 7.2, "3595 Main St": 7.7, "380 W 2880 S": 6.6,
        "410 S State St": 3.2, "4300 S 1300 E": 11.2, "4580 S 2300 E": 12.7, "5025 State St": 10.0,
        "5100 South 2700 West": 8.2, "5383 S 900 East #104": 11.7, "600 E 900 South": 5.1, "6351 South 900 East": 14.2
    },
    "2300 Parkway Blvd": {
        "4001 South 700 East": 8.6, "1060 Dalton Ave S": 2.8, "1330 2100 S": 6.3, "1488 4800 S": 4.0,
        "177 W Price Ave": 5.1, "195 W Oakland Ave": 4.3, "2010 W 500 S": 4.0, "2300 Parkway Blvd": 0.0,
        "233 Canyon Rd": 7.7, "2530 S 500 E": 9.3, "2600 Taylorsville Blvd": 4.6, "2835 Main St": 4.8,
        "300 State St": 7.7, "3060 Lester St": 1.6, "3148 S 1100 W": 3.3, "3365 S 900 W": 3.4,
        "3575 W Valley Central Station bus Loop": 3.1, "3595 Main St": 5.1, "380 W 2880 S": 4.6,
        "410 S State St": 6.7, "4300 S 1300 E": 8.1, "4580 S 2300 E": 10.4, "5025 State St": 7.8,
        "5100 South 2700 West": 4.2, "5383 S 900 East #104": 9.5, "600 E 900 South": 6.2, "6351 South 900 East": 10.7
    },
    "233 Canyon Rd": {
        "4001 South 700 East": 7.6, "1060 Dalton Ave S": 4.8, "1330 2100 S": 5.3, "1488 4800 S": 11.1,
        "177 W Price Ave": 7.5, "195 W Oakland Ave": 4.5, "2010 W 500 S": 4.2, "2300 Parkway Blvd": 7.7,
        "233 Canyon Rd": 0.0, "2530 S 500 E": 4.8, "2600 Taylorsville Blvd": 11.9, "2835 Main St": 4.7,
        "300 State St": 0.6, "3060 Lester St": 7.6, "3148 S 1100 W": 7.8, "3365 S 900 W": 6.6,
        "3575 W Valley Central Station bus Loop": 7.2, "3595 Main St": 5.9, "380 W 2880 S": 5.4,
        "410 S State St": 1.0, "4300 S 1300 E": 8.5, "4580 S 2300 E": 10.3, "5025 State St": 7.8,
        "5100 South 2700 West": 11.5, "5383 S 900 East #104": 9.5, "600 E 900 South": 2.8, "6351 South 900 East": 14.1
    },
    "2530 S 500 E": {
        "4001 South 700 East": 2.8, "1060 Dalton Ave S": 6.3, "1330 2100 S": 1.6, "1488 4800 S": 7.3,
        "177 W Price Ave": 2.6, "195 W Oakland Ave": 1.5, "2010 W 500 S": 8.0, "2300 Parkway Blvd": 9.3,
        "233 Canyon Rd": 4.8, "2530 S 500 E": 0.0, "2600 Taylorsville Blvd": 9.4, "2835 Main St": 1.1,
        "300 State St": 5.1, "3060 Lester St": 4.6, "3148 S 1100 W": 3.7, "3365 S 900 W": 4.0,
        "3575 W Valley Central Station bus Loop": 6.7, "3595 Main St": 2.3, "380 W 2880 S": 1.8,
        "410 S State St": 4.1, "4300 S 1300 E": 3.8, "4580 S 2300 E": 5.8, "5025 State St": 4.3,
        "5100 South 2700 West": 7.8, "5383 S 900 East #104": 4.8, "600 E 900 South": 3.2, "6351 South 900 East": 6.0
    },
    "2600 Taylorsville Blvd": {
        "4001 South 700 East": 6.4, "1060 Dalton Ave S": 7.3, "1330 2100 S": 10.4, "1488 4800 S": 1.0,
        "177 W Price Ave": 6.5, "195 W Oakland Ave": 8.7, "2010 W 500 S": 8.6, "2300 Parkway Blvd": 4.6,
        "233 Canyon Rd": 11.9, "2530 S 500 E": 9.4, "2600 Taylorsville Blvd": 0.0, "2835 Main St": 7.3,
        "300 State St": 12.0, "3060 Lester St": 4.9, "3148 S 1100 W": 5.2, "3365 S 900 W": 5.4,
        "3575 W Valley Central Station bus Loop": 8.1, "3595 Main St": 6.2, "380 W 2880 S": 6.9,
        "410 S State St": 11.5, "4300 S 1300 E": 6.9, "4580 S 2300 E": 8.3, "5025 State St": 4.1,
        "5100 South 2700 West": 0.4, "5383 S 900 East #104": 4.9, "600 E 900 South": 11.0, "6351 South 900 East": 6.8
    },
    "2835 Main St": {
        "4001 South 700 East": 3.2, "1060 Dalton Ave S": 5.3, "1330 2100 S": 3.0, "1488 4800 S": 6.4,
        "177 W Price Ave": 1.5, "195 W Oakland Ave": 0.8, "2010 W 500 S": 6.9, "2300 Parkway Blvd": 4.8,
        "233 Canyon Rd": 4.7, "2530 S 500 E": 1.1, "2600 Taylorsville Blvd": 7.3, "2835 Main St": 0.0,
        "300 State St": 4.7, "3060 Lester St": 3.5, "3148 S 1100 W": 2.6, "3365 S 900 W": 2.9,
        "3575 W Valley Central Station bus Loop": 6.3, "3595 Main St": 1.2, "380 W 2880 S": 1.0,
        "410 S State St": 3.7, "4300 S 1300 E": 4.1, "4580 S 2300 E": 6.2, "5025 State St": 3.4,
        "5100 South 2700 West": 6.9, "5383 S 900 East #104": 5.2, "600 E 900 South": 3.7, "6351 South 900 East": 6.4
    },
    "300 State St": {
        "4001 South 700 East": 7.6, "1060 Dalton Ave S": 4.8, "1330 2100 S": 5.3, "1488 4800 S": 11.1,
        "177 W Price Ave": 7.5, "195 W Oakland Ave": 4.5, "2010 W 500 S": 4.2, "2300 Parkway Blvd": 7.7,
        "233 Canyon Rd": 0.6, "2530 S 500 E": 5.1, "2600 Taylorsville Blvd": 12.0, "2835 Main St": 4.7,
        "300 State St": 0.0, "3060 Lester St": 7.3, "3148 S 1100 W": 7.8, "3365 S 900 W": 6.6,
        "3575 W Valley Central Station bus Loop": 7.2, "3595 Main St": 5.9, "380 W 2880 S": 5.4,
        "410 S State St": 1.0, "4300 S 1300 E": 8.5, "4580 S 2300 E": 10.3, "5025 State St": 7.8,
        "5100 South 2700 West": 11.5, "5383 S 900 East #104": 9.5, "600 E 900 South": 2.8, "6351 South 900 East": 14.1
    },
    "3060 Lester St": {
        "4001 South 700 East": 5.2, "1060 Dalton Ave S": 3.0, "1330 2100 S": 6.5, "1488 4800 S": 3.9,
        "177 W Price Ave": 3.2, "195 W Oakland Ave": 3.9, "2010 W 500 S": 4.2, "2300 Parkway Blvd": 1.6,
        "233 Canyon Rd": 7.6, "2530 S 500 E": 4.6, "2600 Taylorsville Blvd": 4.9, "2835 Main St": 3.5,
        "300 State St": 7.3, "3060 Lester St": 0.0, "3148 S 1100 W": 1.3, "3365 S 900 W": 1.5,
        "3575 W Valley Central Station bus Loop": 4.0, "3595 Main St": 3.2, "380 W 2880 S": 3.0,
        "410 S State St": 6.9, "4300 S 1300 E": 6.2, "4580 S 2300 E": 8.2, "5025 State St": 5.5,
        "5100 South 2700 West": 4.4, "5383 S 900 East #104": 7.2, "600 E 900 South": 6.4, "6351 South 900 East": 10.5
    },
    "3148 S 1100 W": {
        "4001 South 700 East": 4.4, "1060 Dalton Ave S": 4.6, "1330 2100 S": 5.6, "1488 4800 S": 4.3,
        "177 W Price Ave": 2.4, "195 W Oakland Ave": 3.0, "2010 W 500 S": 8.0, "2300 Parkway Blvd": 3.3,
        "233 Canyon Rd": 7.8, "2530 S 500 E": 3.7, "2600 Taylorsville Blvd": 5.2, "2835 Main St": 2.6,
        "300 State St": 7.8, "3060 Lester St": 1.3, "3148 S 1100 W": 0.0, "3365 S 900 W": 0.6,
        "3575 W Valley Central Station bus Loop": 6.4, "3595 Main St": 2.4, "380 W 2880 S": 2.2,
        "410 S State St": 6.8, "4300 S 1300 E": 5.3, "4580 S 2300 E": 7.4, "5025 State St": 4.6,
        "5100 South 2700 West": 4.8, "5383 S 900 East #104": 6.3, "600 E 900 South": 6.5, "6351 South 900 East": 8.8
    },
    "3365 S 900 W": {
        "4001 South 700 East": 3.7, "1060 Dalton Ave S": 4.5, "1330 2100 S": 5.8, "1488 4800 S": 4.4,
        "177 W Price Ave": 2.7, "195 W Oakland Ave": 3.8, "2010 W 500 S": 5.8, "2300 Parkway Blvd": 3.4,
        "233 Canyon Rd": 6.6, "2530 S 500 E": 4.0, "2600 Taylorsville Blvd": 5.4, "2835 Main St": 2.9,
        "300 State St": 6.6, "3060 Lester St": 1.5, "3148 S 1100 W": 0.6, "3365 S 900 W": 0.0,
        "3575 W Valley Central Station bus Loop": 5.6, "3595 Main St": 1.6, "380 W 2880 S": 1.7,
        "410 S State St": 6.4, "4300 S 1300 E": 4.9, "4580 S 2300 E": 6.9, "5025 State St": 4.2,
        "5100 South 2700 West": 5.6, "5383 S 900 East #104": 5.9, "600 E 900 South": 5.7, "6351 South 900 East": 8.4
    },
    "3575 W Valley Central Station bus Loop": {
        "4001 South 700 East": 7.6, "1060 Dalton Ave S": 7.4, "1330 2100 S": 5.7, "1488 4800 S": 7.2,
        "177 W Price Ave": 1.4, "195 W Oakland Ave": 5.7, "2010 W 500 S": 7.2, "2300 Parkway Blvd": 3.1,
        "233 Canyon Rd": 7.2, "2530 S 500 E": 6.7, "2600 Taylorsville Blvd": 8.1, "2835 Main St": 6.3,
        "300 State St": 7.2, "3060 Lester St": 4.0, "3148 S 1100 W": 6.4, "3365 S 900 W": 5.6,
        "3575 W Valley Central Station bus Loop": 0.0, "3595 Main St": 7.1, "380 W 2880 S": 6.1,
        "410 S State St": 7.2, "4300 S 1300 E": 10.6, "4580 S 2300 E": 12.0, "5025 State St": 9.4,
        "5100 South 2700 West": 7.5, "5383 S 900 East #104": 11.1, "600 E 900 South": 6.2, "6351 South 900 East": 13.6
    },
    "3595 Main St": {
        "4001 South 700 East": 2.0, "1060 Dalton Ave S": 6.0, "1330 2100 S": 4.1, "1488 4800 S": 5.3,
        "177 W Price Ave": 0.5, "195 W Oakland Ave": 1.9, "2010 W 500 S": 7.7, "2300 Parkway Blvd": 5.1,
        "233 Canyon Rd": 5.9, "2530 S 500 E": 2.3, "2600 Taylorsville Blvd": 6.2, "2835 Main St": 1.2,
        "300 State St": 5.9, "3060 Lester St": 3.2, "3148 S 1100 W": 2.4, "3365 S 900 W": 1.6,
        "3575 W Valley Central Station bus Loop": 7.1, "3595 Main St": 0.0, "380 W 2880 S": 1.6,
        "410 S State St": 4.9, "4300 S 1300 E": 3.0, "4580 S 2300 E": 5.0, "5025 State St": 2.3,
        "5100 South 2700 West": 5.5, "5383 S 900 East #104": 4.0, "600 E 900 South": 5.1, "6351 South 900 East": 5.2
    },
    "380 W 2880 S": {
        "4001 South 700 East": 3.6, "1060 Dalton Ave S": 5.0, "1330 2100 S": 3.6, "1488 4800 S": 6.0,
        "177 W Price Ave": 1.7, "195 W Oakland Ave": 1.1, "2010 W 500 S": 6.6, "2300 Parkway Blvd": 4.6,
        "233 Canyon Rd": 5.4, "2530 S 500 E": 1.8, "2600 Taylorsville Blvd": 6.9, "2835 Main St": 1.0,
        "300 State St": 5.4, "3060 Lester St": 3.0, "3148 S 1100 W": 2.2, "3365 S 900 W": 1.7,
        "3575 W Valley Central Station bus Loop": 6.1, "3595 Main St": 1.6, "380 W 2880 S": 0.0,
        "410 S State St": 4.4, "4300 S 1300 E": 4.6, "4580 S 2300 E": 6.6, "5025 State St": 3.9,
        "5100 South 2700 West": 6.5, "5383 S 900 East #104": 5.6, "600 E 900 South": 4.3, "6351 South 900 East": 6.9
    },
    "410 S State St": {
        "4001 South 700 East": 6.5, "1060 Dalton Ave S": 4.8, "1330 2100 S": 4.3, "1488 4800 S": 10.6,
        "177 W Price Ave": 6.5, "195 W Oakland Ave": 3.5, "2010 W 500 S": 3.2, "2300 Parkway Blvd": 6.7,
        "233 Canyon Rd": 1.0, "2530 S 500 E": 4.1, "2600 Taylorsville Blvd": 11.5, "2835 Main St": 3.7,
        "300 State St": 1.0, "3060 Lester St": 6.9, "3148 S 1100 W": 6.8, "3365 S 900 W": 6.4,
        "3575 W Valley Central Station bus Loop": 7.2, "3595 Main St": 4.9, "380 W 2880 S": 4.4,
        "410 S State St": 0.0, "4300 S 1300 E": 7.5, "4580 S 2300 E": 9.3, "5025 State St": 6.8,
        "5100 South 2700 West": 11.4, "5383 S 900 East #104": 8.5, "600 E 900 South": 1.8, "6351 South 900 East": 13.1
    },
    "4300 S 1300 E": {
        "4001 South 700 East": 1.9, "1060 Dalton Ave S": 9.5, "1330 2100 S": 3.3, "1488 4800 S": 5.9,
        "177 W Price Ave": 3.2, "195 W Oakland Ave": 4.9, "2010 W 500 S": 11.2, "2300 Parkway Blvd": 8.1,
        "233 Canyon Rd": 8.5, "2530 S 500 E": 3.8, "2600 Taylorsville Blvd": 6.9, "2835 Main St": 4.1,
        "300 State St": 8.5, "3060 Lester St": 6.2, "3148 S 1100 W": 5.3, "3365 S 900 W": 4.9,
        "3575 W Valley Central Station bus Loop": 10.6, "3595 Main St": 3.0, "380 W 2880 S": 4.6,
        "410 S State St": 7.5, "4300 S 1300 E": 0.0, "4580 S 2300 E": 2.0, "5025 State St": 2.9,
        "5100 South 2700 West": 6.4, "5383 S 900 East #104": 2.8, "600 E 900 South": 6.0, "6351 South 900 East": 4.1
    },
    "4580 S 2300 E": {
        "4001 South 700 East": 3.4, "1060 Dalton Ave S": 10.9, "1330 2100 S": 5.0, "1488 4800 S": 7.4,
        "177 W Price Ave": 5.2, "195 W Oakland Ave": 6.9, "2010 W 500 S": 12.7, "2300 Parkway Blvd": 10.4,
        "233 Canyon Rd": 10.3, "2530 S 500 E": 5.8, "2600 Taylorsville Blvd": 8.3, "2835 Main St": 6.2,
        "300 State St": 10.3, "3060 Lester St": 8.2, "3148 S 1100 W": 7.4, "3365 S 900 W": 6.9,
        "3575 W Valley Central Station bus Loop": 12.0, "3595 Main St": 5.0, "380 W 2880 S": 6.6,
        "410 S State St": 9.3, "4300 S 1300 E": 2.0, "4580 S 2300 E": 0.0, "5025 State St": 4.4,
        "5100 South 2700 West": 7.9, "5383 S 900 East #104": 3.4, "600 E 900 South": 7.9, "6351 South 900 East": 4.7
    },
    "5025 State St": {
        "4001 South 700 East": 2.4, "1060 Dalton Ave S": 8.3, "1330 2100 S": 6.1, "1488 4800 S": 4.7,
        "177 W Price Ave": 2.5, "195 W Oakland Ave": 4.2, "2010 W 500 S": 10.0, "2300 Parkway Blvd": 7.8,
        "233 Canyon Rd": 7.8, "2530 S 500 E": 4.3, "2600 Taylorsville Blvd": 4.1, "2835 Main St": 3.4,
        "300 State St": 7.8, "3060 Lester St": 5.5, "3148 S 1100 W": 4.6, "3365 S 900 W": 4.2,
        "3575 W Valley Central Station bus Loop": 9.4, "3595 Main St": 2.3, "380 W 2880 S": 3.9,
        "410 S State St": 6.8, "4300 S 1300 E": 2.9, "4580 S 2300 E": 4.4, "5025 State St": 0.0,
        "5100 South 2700 West": 4.5, "5383 S 900 East #104": 1.7, "600 E 900 South": 6.8, "6351 South 900 East": 3.1
    },
    "5100 South 2700 West": {
        "4001 South 700 East": 6.4, "1060 Dalton Ave S": 6.9, "1330 2100 S": 9.7, "1488 4800 S": 0.6,
        "177 W Price Ave": 6.0, "195 W Oakland Ave": 9.0, "2010 W 500 S": 8.2, "2300 Parkway Blvd": 4.2,
        "233 Canyon Rd": 11.5, "2530 S 500 E": 7.8, "2600 Taylorsville Blvd": 0.4, "2835 Main St": 6.9,
        "300 State St": 11.5, "3060 Lester St": 4.4, "3148 S 1100 W": 4.8, "3365 S 900 W": 5.6,
        "3575 W Valley Central Station bus Loop": 7.5, "3595 Main St": 5.5, "380 W 2880 S": 6.5,
        "410 S State St": 11.4, "4300 S 1300 E": 6.4, "4580 S 2300 E": 7.9, "5025 State St": 4.5,
        "5100 South 2700 West": 0.0, "5383 S 900 East #104": 5.4, "600 E 900 South": 10.6, "6351 South 900 East": 7.8
    },
    "5383 S 900 East #104": {
        "4001 South 700 East": 2.4, "1060 Dalton Ave S": 10.0, "1330 2100 S": 6.1, "1488 4800 S": 6.4,
        "177 W Price Ave": 4.2, "195 W Oakland Ave": 5.9, "2010 W 500 S": 11.7, "2300 Parkway Blvd": 9.5,
        "233 Canyon Rd": 9.5, "2530 S 500 E": 4.8, "2600 Taylorsville Blvd": 6.4, "2835 Main St": 5.2,
        "300 State St": 9.5, "3060 Lester St": 7.2, "3148 S 1100 W": 6.3, "3365 S 900 W": 5.9,
        "3575 W Valley Central Station bus Loop": 11.1, "3595 Main St": 4.0, "380 W 2880 S": 5.6,
        "410 S State St": 8.5, "4300 S 1300 E": 2.8, "4580 S 2300 E": 3.4, "5025 State St": 1.7,
        "5100 South 2700 West": 5.4, "5383 S 900 East #104": 0.0, "600 E 900 South": 7.0, "6351 South 900 East": 1.3
    },
    "600 E 900 South": {
        "4001 South 700 East": 5.0, "1060 Dalton Ave S": 4.4, "1330 2100 S": 2.8, "1488 4800 S": 10.1,
        "177 W Price Ave": 5.4, "195 W Oakland Ave": 3.5, "2010 W 500 S": 5.1, "2300 Parkway Blvd": 6.2,
        "233 Canyon Rd": 2.8, "2530 S 500 E": 3.2, "2600 Taylorsville Blvd": 11.0, "2835 Main St": 3.7,
        "300 State St": 2.8, "3060 Lester St": 6.4, "3148 S 1100 W": 6.5, "3365 S 900 W": 5.7,
        "3575 W Valley Central Station bus Loop": 6.2, "3595 Main St": 5.1, "380 W 2880 S": 4.3,
        "410 S State St": 1.8, "4300 S 1300 E": 6.0, "4580 S 2300 E": 7.9, "5025 State St": 6.8,
        "5100 South 2700 West": 10.6, "5383 S 900 East #104": 7.0, "600 E 900 South": 0.0, "6351 South 900 East": 8.3
    },
    "6351 South 900 East": {
        "4001 South 700 East": 3.6, "1060 Dalton Ave S": 13.0, "1330 2100 S": 7.4, "1488 4800 S": 10.1,
        "177 W Price Ave": 5.5, "195 W Oakland Ave": 7.2, "2010 W 500 S": 14.2, "2300 Parkway Blvd": 10.7,
        "233 Canyon Rd": 14.1, "2530 S 500 E": 6.0, "2600 Taylorsville Blvd": 10.1, "2835 Main St": 6.4,
        "300 State St": 14.1, "3060 Lester St": 10.5, "3148 S 1100 W": 8.8, "3365 S 900 W": 8.4,
        "3575 W Valley Central Station bus Loop": 13.6, "3595 Main St": 5.2, "380 W 2880 S": 6.9,
        "410 S State St": 13.1, "4300 S 1300 E": 4.1, "4580 S 2300 E": 4.7, "5025 State St": 3.1,
        "5100 South 2700 West": 7.8, "5383 S 900 East #104": 1.3, "600 E 900 South": 8.3, "6351 South 900 East": 0.0
    }
}


# Define hash table class
class HashTable:
    def __init__(self, size):
        # Set the table size
        self.size = size
        # Allocate table space based on the size
        self.table = [[] for _ in range(size)]

    # Hash function method which returns the bucket number for a given key
    def calculate_hash(self, key):
        # Allocates the bucket number as evenly as the size of the hash table and return it
        return hash(key) % self.size

    # Insert package method, which inserts each data component of a package into the hash table
    def insert(self, package_id, delivery_address, delivery_deadline, delivery_city, delivery_zip_code, package_weight, delivery_status, truck_number):
        # Calculate the bucket of the package using the hash function method
        bucket = self.calculate_hash(package_id)
        # Set the package data per parameters
        package_components = {
            "package_id": package_id,
            "delivery_address": delivery_address,
            "delivery_deadline": delivery_deadline,
            "delivery_city": delivery_city,
            "delivery_zip_code": delivery_zip_code,
            "package_weight": package_weight,
            "delivery_status": delivery_status,
            "truck_number": truck_number
        }
        # Iterate through each entry in the bucket in the hash table
        for entry in self.table[bucket]:
            # If the package id match is found
            if entry["package_id"] == package_id:
                # Update every component per parameters
                entry.update(package_components)
                return
        # If no match has been found, append the component set as a new entry
        self.table[bucket].append(package_components)

    # Look up method that takes package_id as a parameter and returns important package details
    def lookup(self, package_id):
        # Calculate the bucket to search in using the hash method
        bucket = self.calculate_hash(package_id)
        # Iterate through each entry in the bucket in the hash table
        for entry in self.table[bucket]:
            # If the package id match is found
            if entry["package_id"] == package_id:
                # Return the important package details as a tuple
                return (
                    entry["delivery_address"],
                    entry["delivery_deadline"],
                    entry["delivery_city"],
                    entry["delivery_zip_code"],
                    entry["package_weight"],
                    entry["delivery_status"],
                    entry["truck_number"]
                )
        # If no match has been found, return None
        return None

    # A method to update delivery status/time during the simulation
    def update_status(self, package_id, delivery_status):
        # Calculate the specific bucket of the package id using the hash method
        bucket = self.calculate_hash(package_id)
        # Iterate through each entry within the bucket
        for entry in self.table[bucket]:
            # If a package id match has been found
            if entry["package_id"] == package_id:
                # Update the delivery status per parameter
                entry["delivery_status"] = delivery_status
                # Return True to indicate it has successfully updated
                return True
        # If no match has been found, return False
        return False

    # A method to update delivery address during the simulation
    def update_address(self, package_id, delivery_address, delivery_zip_code):
        # Calculate the specific bucket of the package id using the hash method
        bucket = self.calculate_hash(package_id)
        # Iterate through each entry within the bucket
        for entry in self.table[bucket]:
            # If a package id match has been found
            if entry["package_id"] == package_id:
                # Update the delivery status per parameter
                entry["delivery_address"] = delivery_address
                entry["delivery_zip_code"] = delivery_zip_code
                # Return True to indicate it has successfully updated
                return True
        # If no match has been found, return False
        return False

# Instantiate a hash table object of size 40
hash_table = HashTable(40)
# Iterate through the package data set
for package in packages_data:
    # Insert each package data for each iteration with the unpacking operator
    hash_table.insert(*package)

# A function to get distance between two locations
def get_distance(from_address, to_address):
    # Look up the miles value from distance data, "from" address to the nested "to" address
    return (distances_data.get(from_address)).get(to_address)

# A function using the nearest neighbor algorithm to return the nearest address and package
def find_nearest(current_address, truck, current_time):
    # Initialize nearest address to current address
    nearest_address = current_address
    # Initialize shortest distance to infinite
    nearest_distance = float('inf')
    # Initialize nearest package to None
    nearest_package_id = None
    # Loop through each package id in truck
    for package_id in truck:
        # If we encounter package 9 before 10:20 AM, skip it (because it will still have an incorrect address)
        if package_id == 9 and current_time < 620:
            continue
        # Find the package details using the lookup function
        package_details = hash_table.lookup(package_id)
        # get the delivery address from the first lookup data component of the package, which is the delivery_address
        delivery_address = package_details[0]
        # Find and store the distance to the delivery address
        delivery_distance = get_distance(current_address, delivery_address)
        # Start the Nearest Neighbor Algorithm
        # If this delivery address is not the current address and shorter than shortest_distance found thus far,
        if nearest_distance > delivery_distance and current_address != delivery_address:
            # Then set this delivery address as the nearest address
            nearest_address = delivery_address
            # Set the shortest distance as this delivery distance
            nearest_distance = delivery_distance
            # Set the nearest package id as this package id
            nearest_package_id = package_id
    # Return the nearest address and nearest package id
    return nearest_address, nearest_package_id

# A function to run the delivery simulation
def simulate_delivery(current_time, end_time, truck):
    # Initialize the current address as the hub
    current_address = "4001 South 700 East"
    # Initialize total distance traveled by the truck as 0 miles
    total_distance = 0
    # Initialize required distance to the next address as 0 miles
    required_distance = 0
    # Initialize required time to the next address as 0 minutes
    required_time = 0

    # While there is still package in truck
    while truck and current_time < end_time:
        # Find the nearest delivery address
        nearest_address, nearest_package_id = find_nearest(current_address, truck, current_time)
        # Find the travel distance to there
        required_distance = get_distance(current_address, nearest_address)
        # Find the travel time to there
        required_time = (required_distance * 60)/18

        # Update the delivery status to En route before the travel starts
        hash_table.update_status(nearest_package_id, "En route")

        # Check if time will reach 10:20 AM during this travel and if simulation does not end before 10:20 AM
        if current_time + required_time >= 620 and end_time >= 620:
            # Then update package 9 to the correct address and zip code
            hash_table.update_address(9, "410 S State St", 84111)

        # Check if the expected delivery time will exceed the simulation end time
        if current_time + required_time > end_time:
            # Then regardless of not making it, travel what distance you can cover until the end of the simulation
            total_distance += (required_distance * (end_time - current_time))/18
            # Update the current time to the end time of the simulation
            current_time = end_time
            # Break out of the while loop
            break

        # Update the current time
        current_time += required_time
        # Update the travel distance
        total_distance += required_distance
        # Update the current address
        current_address = nearest_address
        # Unload (remove) the package from the truck
        truck.remove(nearest_package_id)
        # Update the package delivery status
        hash_table.update_status(nearest_package_id, ("Delivered at " + minutes_to_military(current_time)))

    return total_distance

# A function to convert from military time to nth minute
def military_to_minutes(military_time):
    # Extract the values before and after colon into hours and minutes variables
    hours, minutes = military_time.split(":")
    # Convert hours and minutes into integers
    hours = int(hours)
    minutes = int(minutes)
    # Calculate total minutes
    total_minutes = (hours * 60) + minutes
    # Return the total nth minute
    return total_minutes

# A function to convert from nth minute to military time
def minutes_to_military(total_minutes):
    # Ensure total_minutes is an integer
    total_minutes = int(total_minutes)
    # Calculate hours by getting the quotient of the total minutes divided by 60
    hours = total_minutes // 60
    # Calculate the remaining minutes by getting the remainder of the total minutes divided by 60
    minutes = total_minutes % 60
    # Concatenate hours, colon, and minutes while ensuring two digits
    military_time = f"{hours:02}:{minutes:02}"
    # Return the military time
    return military_time

# A function to get and validate user's military time input
def get_time_input():
    # Get and store user input for military time
    input_time = input("Enter the time in military format, e.g. 14:50: ")
    # If the input does not contain a colon,
    if ":" not in input_time:
        print ("Invalid input. Please enter the time in HH:MM format.")
        return
    # Extract the values before and after colon into hours and minutes variables.
    hours, minutes = input_time.split(":")
    # If the digit length is 2 for hours and minutes, and they are digits,
    if len(hours) == 2 and len(minutes) == 2 and hours.isdigit() and minutes.isdigit():
        # Then convert hours and minutes into integers.
        hours = int(hours)
        minutes = int(minutes)
        # If value of hours and minutes are out of bounds,
        if hours >= 24 or minutes >= 60:
            print ("Invalid input. Please enter valid numerical values for hours and minutes.")
            return
    # If the length was off or input is not numerical,
    else:
        print ("Invalid input. Please enter the time in HH:MM format.")
        return

    return input_time

# Load trucks with all constraints considered with 16 packages per truck at maximum
# truck 1: co-delivery (13, 14, 15, 16, 19, 20)
truck_1 = [17, 21, 22, 23, 24, 26, 27, 13, 14, 15, 16, 19, 20]
# truck 2: truck 2 only (3, 18, 36, 38)
truck_2 = [29, 30, 31, 34, 37, 40, 3, 18, 36, 38, 12]
# truck 3: past 9:05 AM (6, 25, 28, 32)
truck_3 = [1, 6, 25, 28, 32, 33, 35, 39, 2, 9, 4, 5, 7, 8, 10, 11]

# An interface function to let user control the simulation program
def interface():
    # Initialize total distance traveled by all trucks to 0
    total_distance = 0
    # Initialize user's time input to None
    input_time = None

    # Repeat user's time input prompt until the input is validated
    while input_time is None:
        # Provide user with a description of the input
        print("At what time of the day would you like to check the progress for?")
        # Get user input of the time which will return None if not valid
        input_time = get_time_input()

    # Convert the user's military time into the nth minute form
    end_time = military_to_minutes(input_time)
    # Start the first truck at 8:00 AM and add distance traveled
    total_distance += simulate_delivery(480, end_time, truck_1)
    # Start the second truck at 9:05 AM and add distance traveled
    total_distance += simulate_delivery(480, end_time, truck_2)
    # Start the third truck at 10:20 AM and add distance traveled
    total_distance += simulate_delivery(545, end_time, truck_3)
    # Print the total distance covered by all trucks
    print("Total distance traveled by all trucks: " + str(total_distance) + " miles")

    # Get all packages
    all_packages = [package for bucket in hash_table.table for package in bucket]
    # Sort the packages by package_id using a lambda function
    all_packages = sorted(all_packages, key = lambda p:p["package_id"])

    # Print the column headers
    print("{:<10} {:<8} {:<40} {:<12} {:<20}".format(
        "Package", "Truck", "Delivery Address", "Deadline", "Status"))
    # Loop through each package
    for package in all_packages:
        # Retrieve package details using the lookup function
        package_details = hash_table.lookup(package["package_id"])
        # Output the package id, truck number and delivery status and time from the package lookup data.
        print("{:<10} {:<8} {:<40} {:<12} {:<20}".format(
            # Output package id
            package["package_id"],
            # Output truck id
            package_details[6],
            # Output delivery address
            package_details[0],
            # Output delivery deadline
            package_details[1],
            # Output delivery status including time
            package_details[5]
        ))

    return None
# Call the interface function to start user interaction with the simulation program
interface()