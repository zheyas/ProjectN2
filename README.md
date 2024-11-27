
# Product and Category Management System

## Overview
This project provides a flexible and extendable structure to manage products and categories. It includes base classes for generic products and specialized classes for specific product types such as smartphones and lawn grass. The system also supports managing categories, adding products dynamically, and includes robust error handling and integration with Mixin for enhanced functionality.

---

## Features

### Product Class
- Represents a generic product.
- **Attributes**:
  - `name`: The name of the product.
  - `description`: A brief description.
  - `price`: Price of the product (with validation for positive values).
  - `quantity`: Available stock quantity.
- **Functionalities**:
  - Custom string representation for better readability.
  - Overloaded addition operator to calculate the combined cost of products.
  - Factory method (`new_product`) for creating instances from dictionaries.
  - Read-only property for price validation and dynamic updates.

### Mixin Class
- A mixin for enhanced initialization and debug printouts.
- Automatically prints the details of created objects, including attribute values.

### Category Class
- Manages a collection of products under a specific category.
- **Attributes**:
  - `category_count`: Tracks the total number of categories.
  - `product_count`: Tracks the total number of products across all categories.
  - `description`: A brief description of the category.
  - `products`: List of products in the category.
- **Functionalities**:
  - Add products dynamically with type validation.
  - View all products within a category.
  - Calculate the average price of all products in the category.

### Specialized Product Classes
#### Smartphone
- Inherits from `Product` and integrates the `Mixin` class.
- **Additional Attributes**:
  - `efficiency`: Battery efficiency.
  - `model`: Model name.
  - `memory`: Storage capacity.
  - `color`: Color of the smartphone.
- **Special Features**:
  - Restricts addition to other `Smartphone` objects only.

#### LawnGrass
- Inherits from `Product` and integrates the `Mixin` class.
- **Additional Attributes**:
  - `country`: Country of origin.
  - `germination_period`: Germination time.
  - `color`: Grass color.
- **Special Features**:
  - Restricts addition to other `LawnGrass` objects only.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/product-management-system.git
   ```
2. Navigate to the project directory:
   ```bash
   cd product-management-system
   ```
3. Ensure Python 3.7+ is installed.

---

## Usage

### Example Code
```python
# Import necessary classes
from main_14 import Smartphone, LawnGrass, Category

# Create some products
smartphone = Smartphone(
    "Samsung Galaxy S23 Ultra", 
    "256GB, Серый цвет, 200MP камера",
    180000.0, 
    5, 
    efficiency="High", 
    model="S23 Ultra", 
    memory="256GB", 
    color="Gray"
)

grass = LawnGrass(
    "Газонная трава", 
    "Элитная трава для газона", 
    500.0, 
    20, 
    country="Россия", 
    germination_period="7 дней", 
    color="Зеленый"
)

# Create a category and add products
category = Category("Смартфоны", "Описание категории", [smartphone])
category.add_product(smartphone)

# Calculate combined cost of smartphones
total_cost = smartphone + smartphone
print(f"Общая стоимость: {total_cost} руб.")
```

### Running the Tests
Run the test suite with:
```bash
pytest
```

---

## Error Handling
- Adding a non-`Product` object to a `Category` raises a `TypeError`.
- Adding incompatible product types (e.g., `Smartphone` + `LawnGrass`) raises a `TypeError`.
- Setting a negative price triggers validation.

---

## Authors
- **Your Name** - Initial development

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
