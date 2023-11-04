# import requests
# from bs4 import BeautifulSoup
# import urllib.parse

# # Define the starting URL
# start_url = 'http://itekindia.com/dashboard/pages/sign-in.html'

# # Create a set to store visited URLs to avoid duplicate requests
# visited_urls = set()

# # Create a function to crawl the website and collect links and files
# def crawl(url):
#     try:
#         # Send an HTTP GET request to the URL
#         response = requests.get(url)
        
#         # Check if the request was successful
#         if response.status_code == 200:
#             # Parse the HTML content of the page
#             soup = BeautifulSoup(response.text, 'html.parser')
            
#             # Collect links and files
#             links = set()
#             files = set()
            
#             # Extract links and files from the page
#             for link in soup.find_all('a'):
#                 href = link.get('href')
#                 if href:
#                     links.add(href)
            
#             # You can also collect other file types (e.g., PDF, images) based on their URLs
#             for file in soup.find_all('a', href=lambda href: (href.endswith('.pdf') or href.endswith('.jpg'))):
#                 files.add(file['href'])
            
#             # Print the collected links and files
#             print(f'Links at {url}:')
#             for link in links:
#                 full_link = urllib.parse.urljoin(url, link)
#                 print(full_link)
#             print(f'\nFiles at {url}:')
#             for file in files:
#                 full_file_url = urllib.parse.urljoin(url, file)
#                 print(full_file_url)
            
#             # Add the URL to the set of visited URLs
#             visited_urls.add(url)
            
#             # Recursively crawl linked pages
#             for link in links:
#                 full_link = urllib.parse.urljoin(url, link)
#                 if full_link not in visited_urls:
#                     crawl(full_link)
    
#     except Exception as e:
#         print(f"Error while crawling {url}: {e}")

# # Start crawling
# crawl(start_url)
# import requests
# from bs4 import BeautifulSoup
# import urllib.parse

# # Define the starting URL
# start_url = 'http://itekindia.com/dashboard/pages/sign-in.html'

# # Extract the base URL to restrict crawling to the same domain
# base_url = urllib.parse.urlparse(start_url).scheme + '://' + urllib.parse.urlparse(start_url).hostname

# # Create a set to store visited URLs to avoid duplicate requests
# visited_urls = set()

# # Create a function to crawl the website and collect links and files
# def crawl(url):
#     try:
#         # Send an HTTP GET request to the URL
#         response = requests.get(url)
        
#         # Check if the request was successful
#         if response.status_code == 200:
#             # Parse the HTML content of the page
#             soup = BeautifulSoup(response.text, 'html.parser')
            
#             # Collect links and files
#             links = set()
#             files = set()
            
#             # Extract links from the page that are on the same domain
#             for link in soup.find_all('a'):
#                 href = link.get('href')
#                 if href:
#                     full_link = urllib.parse.urljoin(url, href)
#                     if full_link.startswith(base_url):
#                         links.add(full_link)
            
#             # You can also collect other file types (e.g., PDF, images) based on their URLs
#             for file in soup.find_all('a', href=lambda href: (href.endswith('.pdf') or href.endswith('.jpg'))):
#                 full_file_url = urllib.parse.urljoin(url, file['href'])
#                 if full_file_url.startswith(base_url):
#                     files.add(full_file_url)
            
#             # Print the collected links and files
#             print(f'Links at {url}:')
#             for link in links:
#                 print(link)
#             print(f'\nFiles at {url}:')
#             for file_url in files:
#                 print(file_url)
            
#             # Add the URL to the set of visited URLs
#             visited_urls.add(url)
            
#             # Recursively crawl linked pages
#             for link in links:
#                 if link not in visited_urls:
#                     crawl(link)
    
#     except Exception as e:
#         print(f"Error while crawling {url}: {e}")

# # Start crawling
# crawl(start_url)
# import requests
# from bs4 import BeautifulSoup
# import urllib.parse

# # Define the starting URL
# start_url = 'http://itekindia.com/dashboard/pages/sign-in.html'

# # Extract the base URL to restrict crawling to the same domain
# base_url = urllib.parse.urlparse(start_url).scheme + '://' + urllib.parse.urlparse(start_url).hostname

# # Create a set to store visited URLs to avoid duplicate requests
# visited_urls = set()

# # Create a function to crawl the website and collect links, files, and assets
# def crawl(url):
#     try:
#         # Send an HTTP GET request to the URL
#         response = requests.get(url)
        
#         # Check if the request was successful
#         if response.status_code == 200:
#             # Parse the HTML content of the page
#             soup = BeautifulSoup(response.text, 'html.parser')
            
#             # Collect links, files, and assets
#             links = set()
#             files = set()
#             assets = set()
            
#             # Extract links from the page that are on the same domain
#             for link in soup.find_all('a'):
#                 href = link.get('href')
#                 if href:
#                     full_link = urllib.parse.urljoin(url, href)
#                     if full_link.startswith(base_url):
#                         links.add(full_link)
            
#             # Collect other file types (e.g., PDF, images) based on their URLs
#             for file in soup.find_all('a', href=lambda href: (href.endswith('.pdf') or href.endswith('.jpg'))):
#                 full_file_url = urllib.parse.urljoin(url, file['href'])
#                 if full_file_url.startswith(base_url):
#                     files.add(full_file_url)
            
#             # Collect assets, including images, stylesheets, and JavaScript files
#             for asset in soup.find_all(['img', 'link', 'script']):
#                 asset_url = asset.get('src') or asset.get('href')
#                 if asset_url:
#                     full_asset_url = urllib.parse.urljoin(url, asset_url)
#                     if full_asset_url.startswith(base_url):
#                         assets.add(full_asset_url)
            
#             # Print the collected links, files, and assets
#             print(f'Links at {url}:')
#             for link in links:
#                 print(link)
#             print(f'\nFiles at {url}:')
#             for file_url in files:
#                 print(file_url)
#             print(f'\nAssets at {url}:')
#             for asset_url in assets:
#                 print(asset_url)
            
#             # Add the URL to the set of visited URLs
#             visited_urls.add(url)
            
#             # Recursively crawl linked pages
#             for link in links:
#                 if link not in visited_urls:
#                     crawl(link)
    
#     except Exception as e:
#         print(f"Error while crawling {url}: {e}")

# # Start crawling
# crawl(start_url)
import requests
from bs4 import BeautifulSoup
import urllib.parse

# Define the starting URL
start_url =   input('Enter website address :')  #'http://itekindia.com/dashboard/pages/sign-in.html'

# Extract the base URL to restrict crawling to the same domain
base_url = urllib.parse.urlparse(start_url).scheme + '://' + urllib.parse.urlparse(start_url).hostname

# Create a set to store visited URLs to avoid duplicate requests
visited_urls = set()

# Create a function to crawl the website and collect links, files, and assets
def crawl(url):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Collect links, files, and assets
            links = set()
            files = set()
            assets = set()
            
            # Extract links from the page that are on the same domain
            for link in soup.find_all('a'):
                href = link.get('href')
                if href:
                    full_link = urllib.parse.urljoin(url, href)
                    if full_link.startswith(base_url):
                        links.add(full_link)
            
            # Collect other file types (e.g., PDF, images) based on their URLs
            for file in soup.find_all('a', href=lambda href: (href.endswith('.pdf') or href.endswith('.jpg'))):
                full_file_url = urllib.parse.urljoin(url, file['href'])
                if full_file_url.startswith(base_url):
                    files.add(full_file_url)
            
            # Collect assets, including images, stylesheets, and JavaScript files
            for asset in soup.find_all(['img', 'link', 'script']):
                asset_url = asset.get('src') or asset.get('href')
                if asset_url:
                    full_asset_url = urllib.parse.urljoin(url, asset_url)
                    if full_asset_url.startswith(base_url):
                        assets.add(full_asset_url)
            
            # Print the collected links, files, and assets
            print(f'Links at {url}:')
            for link in links:
                print(link)
            print(f'\nFiles at {url}:')
            for file_url in files:
                print(file_url)
            print(f'\nAssets at {url}:')
            for asset_url in assets:
                print(asset_url)
            
            # Add the URL to the set of visited URLs
            visited_urls.add(url)
            
            # Recursively crawl linked pages
            for link in links:
                if link not in visited_urls:
                    crawl(link)
    
    except Exception as e:
        print(f"Error while crawling {url}: {e}")

# Start crawling
crawl(start_url)
