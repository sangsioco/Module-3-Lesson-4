import re

# Product descriptions
descriptions = [
    "Smartphone with 6-inch screen and 128GB memory",
    "Cotton t-shirt in medium size",
    "Stainless steel kitchen knife set"
]

# Prices
texts_with_prices = [
    "The price is $49.99 and €39.99.",
    "It costs 29.99 USD or 25.99 EUR.",
    "Price: 100 dollars or 90 euros."
]

# Function to tag products based on keywords
def tag_products(descriptions):
    tags = []
    for description in descriptions:
        if re.search(r'\b(smartphone|memory|screen|electronic|tablet|laptop)\b', description, re.I):
            tags.append('Electronics')
        elif re.search(r'\b(cotton|t-shirt|shirt|apparel|clothing|jeans|dress)\b', description, re.I):
            tags.append('Apparel')
        elif re.search(r'\b(kitchen|knife|cookware|home|furniture|utensil)\b', description, re.I):
            tags.append('Home & Kitchen')
        else:
            tags.append('Uncategorized')
    return tags

# Function to convert price formats to 'USD XX.XX'
def convert_price_format(text):
    # Replace different price formats with 'USD XX.XX'
    text = re.sub(r'\$([0-9]+(?:\.[0-9]{2})?)', r'USD \1', text)
    text = re.sub(r'€([0-9]+(?:\.[0-9]{2})?)', r'USD \1', text)
    text = re.sub(r'([0-9]+(?:\.[0-9]{2})?)\s?USD', r'USD \1', text)
    text = re.sub(r'([0-9]+(?:\.[0-9]{2})?)\s?(dollars?|usd)', r'USD \1', text, flags=re.I)
    text = re.sub(r'([0-9]+(?:\.[0-9]{2})?)\s?(euros?|eur|euro)', r'USD \1', text, flags=re.I)
    return text

# Tag each product
product_tags = tag_products(descriptions)

# Apply the conversion to each text
converted_texts = [convert_price_format(text) for text in texts_with_prices]

# Print tagged products
for description, tag in zip(descriptions, product_tags):
    print(f"Description: {description}\nTag: {tag}\n")

# Print converted texts
for original, converted in zip(texts_with_prices, converted_texts):
    print(f"Original: {original}\nConverted: {converted}\n")
