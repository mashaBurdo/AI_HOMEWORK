# API Testing Project

This project automates validation of product data from the public API https://fakestoreapi.com/products.

## Features
- Fetches product data from the API
- Validates:
  - HTTP response code is 200
  - Each product has a non-empty title
  - Each product has a non-negative price
  - Each product's rating.rate does not exceed 5
- Generates a list of products with detected defects

## Requirements
- Python 3.8+
- `requests` library

## Usage
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the tests:
   ```bash
   python test_api.py
   ```

## Project Structure
- `test_api.py`: Main script for API testing and validation
- `requirements.txt`: Python dependencies
