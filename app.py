import sqlite3
import requests

# Function to fetch sales transactions from the database
def fetch_sales_transactions():
    # Connect to the SQLite database
    conn = sqlite3.connect('retail_restaurant.db')
    cursor = conn.cursor()
    
    # Fetch sales transactions from the database
    cursor.execute('SELECT * FROM sales_transactions')
    sales_transactions = cursor.fetchall()
    
    # Close database connection
    conn.close()
    
    return sales_transactions

# Function to send sales transactions to the REST API endpoint
def send_sales_transactions(sales_transactions, token):
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    for transaction in sales_transactions:
        # Assuming the API endpoint is '/sales'
        response = requests.post('https://example.com/api/sales', json=transaction, headers=headers)
        if response.status_code == 200:
            print(f"Transaction {transaction['id']} successfully sent.")
        else:
            print(f"Failed to send transaction {transaction['id']}.")

# Function to obtain bearer token from the REST API
def get_bearer_token(username, password):
    auth_data = {
        'username': username,
        'password': password
    }
    response = requests.post('https://example.com/api/auth', json=auth_data)
    if response.status_code == 200:
        return response.json().get('token')
    else:
        print("Failed to obtain bearer token.")
        return None

# Main function
def main():
    # Replace these placeholders with your actual credentials and API endpoint
    username = 'your_username'
    password = 'your_password'
    db_file = 'retail_restaurant.db'
    
    # Fetch sales transactions from the database
    sales_transactions = fetch_sales_transactions()
    
    # Get bearer token
    token = get_bearer_token(username, password)
    
    if token:
        # Send sales transactions to the REST API endpoint
        send_sales_transactions(sales_transactions, token)
    else:
        print("Exiting program due to authentication failure.")

if __name__ == "__main__":
    main()
