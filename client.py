import requests

# Function to notify server when IR beam is broken
def notify_server():
    response = requests.get('http://127.0.0.1:5000/broken_beam')
    
    if response.status_code == 200:
        print("Server notified about broken beam.")
    else:
        print("Failed to notify server.")

# Example usage
if __name__ == '__main__':
    notify_server()
