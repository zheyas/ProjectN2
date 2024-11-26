
# Product and Category Management System

## Overview
This project provides a basic structure to manage products and categories. It includes base classes for general products and specialized classes for specific product types like smartphones and lawn grass. The system also tracks product categories, supports adding new products, and provides custom error handling for invalid operations.

---

## Features
### Product Class
- Represents a generic product.
- Includes attributes for:
  - `name`: The name of the product.
  - `description`: Description of the product.
  - `price`: Price of the product (with validation to ensure it's positive).
  - `quantity`: Number of items in stock.
- Supports:
  - Custom string representation.
  - Adding products to calculate the combined total cost of multiple products.
  - Factory method (`new_product`) to create instances from a dictionary.

### Category Class
- Represents a product category.
- Tracks:
  - Total number of categories (`category_count`).
  - Total number of products across all categories (`product_count`).
- Supports:
  - Adding products to the category.
  - Viewing all products in a category.

### Specialized Product Classes
#### Smartphone
- Inherits from `Product`.
- Adds attributes:
  - `efficiency`: Battery efficiency rating.
  - `model`: Model of the smartphone.
  - `memory`: Storage capacity.
  - `color`: Smartphone color.
- Restricts addition to only other `Smartphone` objects.

#### LawnGrass
- Inherits from `Product`.
- Adds attributes:
  - `country`: Country of origin.
  - `germination_period`: Time required for germination.
  - `color`: Color of the grass.
- Restricts addition to only other `LawnGrass` objects.

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
from typing import List
# Initialize some products
smartphone = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера",
                        180000.0, 5, 95.5, "S23 Ultra", 256, "Серый")
grass = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")

# Create a category and add products
category = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone])
print(category.products)

# Calculate combined cost
total_cost = smartphone + smartphone
print(f"Общая стоимость: {total_cost} руб.")
```

### Running the Script
Run the script directly:
```bash
python main.py
```

---

## Error Handling
- Adding a non-`Product` object to a `Category` raises a `TypeError`.
- Adding incompatible types of products (e.g., `Smartphone` + `LawnGrass`) raises a `TypeError`.

---

## Authors
- **Your Name** - Initial development

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
