# Smart Inventory & Asset System

**Datheon Python Programming Internship – Task 5**

A Python-based inventory management application developed using Object-Oriented Programming (OOP) concepts.

## Project Overview

The Smart Inventory & Asset System manages different types of assets, including Books, Magazines, and Digital Media.

It allows users to add inventory items, search for items, check out and return assets, calculate borrowing fees, and generate audit reports through an interactive terminal interface.

## Features

- Add Books, Magazines, and Digital Media.
- Display all inventory items.
- Search items using unique IDs.
- Checkout available items.
- Return borrowed items.
- Calculate borrowing fees based on item type.
- Prevent duplicate item IDs.
- Validate item prices.
- Generate inventory audit reports.
- Handle invalid inputs and errors.

## Technologies Used

- Python 3
- ABC module
- datetime
- Object-Oriented Programming

No external Python packages are required.

## Project Structure

```text
Task_5_Inventory_System/
│
├── models.py
├── inventory.py
├── main.py
├── README.md
│
└── screenshots/
    ├── add_inventory.png
    ├── inventory_list.png
    ├── checkout_return.png
    └── audit_report.png
```

## OOP Concepts Implemented

### 1. Abstraction
Uses an abstract base class named `Item` with abstract methods.

### 2. Encapsulation
Uses private attributes to protect item information.

### 3. Inheritance
The Book, Magazine, and DigitalMedia classes inherit from the Item class.

### 4. Polymorphism
Different item classes implement their own fee calculation methods.

### 5. Method Overriding
Child classes override methods defined in the parent class.

### 6. Property Decorators
Uses `@property` and `@price.setter` for controlled access and price validation.

### 7. Dunder Methods
Implements:
- `__str__()`
- `__repr__()`
- `__eq__()`
- `__len__()`

## Borrowing Fee Structure

| Item Type | Daily Fee |
|---|---:|
| Book | Rs. 5 |
| Magazine | Rs. 3 |
| Digital Media | Rs. 10 |

These are example rates used for demonstrating polymorphism.

## How to Run

### Step 1: Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/Task_5_Inventory_System.git
```

### Step 2: Open the project folder

```bash
cd Task_5_Inventory_System
```

### Step 3: Run the application

```bash
python main.py
```

## Application Menu

```text
1. Add Book
2. Add Magazine
3. Add Digital Media
4. Display All Inventory
5. Search Item
6. Checkout Item
7. Return Item
8. Generate Audit Report
9. Show Total Inventory Count
0. Exit
```

## Testing

The following scenarios should be tested:

| Test Case | Expected Result |
|---|---|
| Add a Book | Book added successfully |
| Add a Magazine | Magazine added successfully |
| Add Digital Media | Digital media added successfully |
| Add duplicate ID | Error message |
| Search item | Item details displayed |
| Checkout item | Checkout successful |
| Checkout borrowed item | Error message |
| Return item | Return successful with fee |
| Generate audit report | Activity records displayed |

## Screenshots

### Adding Inventory
![Add Inventory](screenshots/add_inventory.png)

### Inventory List
![Inventory List](screenshots/inventory_list.png)

### Checkout and Return
![Checkout and Return](screenshots/checkout_return.png)

### Audit Report
![Audit Report](screenshots/audit_report.png)

## Learning Outcomes

Through this project, I practised:

- Creating classes and objects in Python.
- Implementing abstraction and inheritance.
- Understanding encapsulation and polymorphism.
- Using method overriding and properties.
- Implementing special methods.
- Building a modular Python application.
- Handling errors and validating user inputs.

## Current Limitations

- Inventory records are stored in memory and reset when the application exits.
- Borrowing rates are demonstration values.
- The application uses a terminal-based interface.

## Author

**Radhika Jejurkar**

B.Sc. Data Science Student

**Internship:** Datheon – Python Programming Internship

**Task 5:** OOPs Architecture – Enterprise Smart Inventory & Asset System

---

*Developed as a practical project demonstrating Object-Oriented Programming concepts using Python.*
