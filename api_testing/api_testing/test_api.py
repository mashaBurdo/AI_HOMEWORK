import requests

API_URL = "https://fakestoreapi.com/products"

def fetch_products():
    response = requests.get(API_URL)
    return response

def validate_products(products):
    defects = []
    for product in products:
        product_defects = []
        if not product.get('title'):
            product_defects.append('Missing or empty title')
        if product.get('price', 0) < 0:
            product_defects.append('Negative price')
        rating = product.get('rating', {})
        if rating.get('rate', 0) > 5:
            product_defects.append('Rating exceeds 5')
        if product_defects:
            defects.append({'id': product.get('id'), 'defects': product_defects, 'product': product})
    return defects

def main():
    response = fetch_products()
    print(f"Status code: {response.status_code}")
    assert response.status_code == 200, "Expected status code 200"
    products = response.json()
    defects = validate_products(products)
    if defects:
        print("Defective products found:")
        for d in defects:
            print(f"Product ID {d['id']}: {d['defects']}")
    else:
        print("No defects found.")

if __name__ == "__main__":
    main()
