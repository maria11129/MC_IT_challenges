import requests
import logging

logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def check_website(url):
    try:
        
        head_response = requests.head(url, timeout=10)
        if head_response.status_code == 200:
            logging.info("Server is alive")
        else:
            logging.info(f"Status Code: {head_response.status_code}")
        
        
        get_response = requests.get(url, timeout=10)
        server_tech = get_response.headers.get('Server', 'Unknown')
        logging.info(f"Server Technology: {server_tech}")
        
        
        options_response = requests.options(url, timeout=10)
        allowed_methods = options_response.headers.get('Allow', 'No methods discovered')
        logging.info(f"Allowed HTTP Methods: {allowed_methods}")
    
    except requests.exceptions.Timeout:
        logging.error("Request timed out")
    except requests.exceptions.ConnectionError:
        logging.error("Server cannot be reached")
    except requests.exceptions.RequestException as e:
        logging.error(f"An error occurred: {e}")

def main():
    url = input("Enter a URL to investigate (e.g., https://example.com): ").strip()
    if not url.startswith(('http://', 'https://')):
        url = f'https://{url}'
    check_website(url)

if __name__ == "__main__":
    main()
