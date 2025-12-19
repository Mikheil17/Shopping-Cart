# Online Shopping Experience
A fully-functional shopping system built with Python and SQLite.

## What It Is
A command-line application that allows users to register, log in, browse inventory, add and remove items from a cart, and complete purchases with persistent inventory tracking using SQLite.

## Tech
Python | SQLite

## Key Features
- User registration and login
- Inventory browsing and stock management
- Cart add/remove functionality
- Checkout with database persistence

## Context
Course project focused on backend logic, database integration, and state management in Python.

#### How to Run

1. Download all files into the same folder on your computer.

2. Open a terminal (or VS Code terminal) in that folder.

3. Set up the database (run once):
   python setup.py

4. Start the shopping cart system:
   python main.py

5. Follow the on-screen menu and enjoy your online shopping experience.


#### Sample Book Inventory

The database comes pre-loaded with the following books:

ISBN             | Title                   | Author              | Genre                     | Pages | Year | Price  | Stock
-----------------|-------------------------|---------------------|---------------------------|-------|------|--------|------
978-0451524935   | 1984                    | George Orwell       | Dystopian                 | 328   | 1949 | 19.99  | 11
978-0446310789   | To Kill a Mockingbird   | Harper Lee          | Southern Gothic           | 281   | 1960 | 25.00  | 100
978-0156028356   | The Color Purple        | Alice Walker        | Epistolary                | 304   | 1982 | 15.98  | 37
978-1400033416   | Beloved                 | Toni Morrison       | American Literature       | 324   | 1987 | 20.99  | 56
978-1501156748   | Misery                  | Stephen King        | Psychological Horror      | 310   | 1987 | 9.50   | 42
978-0312424404   | Gilead                  | Marilynne Robinson  | Novel                     | 256   | 2004 | 19.99  | 39
978-0307265432   | The Road                | Cormac McCarthy     | Post-apocalyptic fiction  | 287   | 2006 | 15.99  | 17
