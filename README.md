# Store Inventory Management

A desktop application for managing the inventory of a small retail shop. Built with Python and Tkinter, it provides a user-friendly interface for tracking products, categories, quantities, and prices, and supports searching, filtering, and exporting inventory data.

## Features

- Add, modify, and delete products in inventory
- Search products by name
- Filter products by category
- View all products in a sortable table
- Export product data to CSV
- Data persisted in a local SQLite database
- User-friendly GUI built with Tkinter

## Getting Started

### Prerequisites
- Python 3.x

### Installation
1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd store-inventory-management
   ```
2. Install required packages (Tkinter is included with most Python installations):
   ```bash
   pip install tkinter
   ```

### Running the Application

```bash
python3 app.py
```

The application window will open, allowing you to manage your store's inventory.

## Project Structure

- `app.py`: Main entry point. Initializes the database and starts the GUI.
- `view.py`: Contains the `GestionInventaire` class, which defines the GUI and its logic.
- `database.py`: Handles all database operations (CRUD, sorting, filtering).
- `data.txt`, `products.csv`: Example data files (optional, for demonstration or export).
- `inventaire.db`: SQLite database file (created automatically).

## Usage

- **Add Product**: Click the add button and fill in the product details.
- **Modify Product**: Select a product and click modify.
- **Delete Product**: Select a product and click delete.
- **Search**: Enter a product name in the search box and click search.
- **Filter**: Enter a category and click filter.
- **Export**: Use the export button to save products to CSV.

## Author

- Zaha Anass
