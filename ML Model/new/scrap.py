import re

# Regular expression pattern to match URLs
url_pattern=[]
abc = re.compile(r'htt[p]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
# url_pattern.append(abc)
#abc = re.compile(r'ngro[k]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
url_pattern.append(abc)
abc = re.compile(r'htt[p]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
# url_pattern.append(abc)
#abc = re.compile(r'ngro[k]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
url_pattern.append(abc)
# abc = re.compile(r'bitly[]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
# url_pattern.append(abc)
# url_pattern=['ngrok','http','bitly']
# List to store the extracted links
links = []

# Open the text file for reading
with open('file.py', 'r') as file:
    # Read the file line by line
    for line in file:
        # Search for URLs in the line using the regex pattern
        for i in range(len(url_pattern)):
            urls = re.findall(url_pattern[i], line)
            # Add the found URLs to the list of links
            links.extend(urls)

print(links)
