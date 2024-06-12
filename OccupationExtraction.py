import re

# Function to extract the value corresponding to a specific key
def extract_value(key, text):
    pattern = rf"{key}: ([^;]+)"
    match = re.search(pattern, text)
    if match:
        return match.group(1).strip()
    return None

# Extract the Occupation from the text
text = "Name: John Doe; Age: 30; Occupation: Engineer; Location: New York"
occupation = extract_value('Occupation', text)
print(f"Occupation: {occupation}")

# List of URLs to validate
urls = [
    "http://example.com",
    "https://www.example.com",
    "ftp://example.com",
    "http://example",
    "https://example.org",
    "invalid-url"
]

# Function to validate URLs
def validate_urls(urls):
    valid_url_pattern = re.compile(
        r'^(https?|ftp):\/\/'  # http:// or https:// or ftp://
        r'(([A-Za-z0-9-]+\.)+[A-Za-z]{2,})'  # domain
        r'(:\d+)?'  # optional port
        r'(\/[^\s]*)?$'  # path
    )
    valid_urls = []
    invalid_urls = []

    for url in urls:
        if re.match(valid_url_pattern, url):
            valid_urls.append(url)
        else:
            invalid_urls.append(url)

    return valid_urls, invalid_urls

# Validate the URLs
valid_urls, invalid_urls = validate_urls(urls)
print("Valid URLs:", valid_urls)
print("Invalid URLs:", invalid_urls)
