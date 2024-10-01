import os
from bs4 import BeautifulSoup

def extract_user_texts(file_path, username):
    """
    Extracts texts from the given username in the provided HTML file.
    """
    print(f"Reading file: {file_path}")  # Indicate that we're reading a file
    try:
        # Open and read the HTML file
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()

        # Parse the HTML content using BeautifulSoup with an alternative parser
        soup = BeautifulSoup(html_content, 'lxml')  # Try using 'lxml' or 'html5lib'

        # Find all message blocks
        message_blocks = soup.find_all('div', style='background: #f2f2f2; border-radius: 7px; padding: 3px; margin-bottom:4px;')

        user_texts = []

        # Loop through each message block to check for the username and extract the text
        for block in message_blocks:
            user_tag = block.find('h4')  # Find the username
            if user_tag and user_tag.text.strip() == username:  # Check if it matches the specified user
                text_content = block.find('p')  # Find the message text
                if text_content:
                    user_texts.append(text_content.text.strip())  # Append the extracted message

        print(f"Found {len(user_texts)} messages from {username} in {file_path}")  # Summary of messages found
        return user_texts

    except Exception as e:
        print(f"Error processing {file_path}: {e}")  # Log any errors encountered

def process_multiple_html_files(directory, username, output_file):
    """
    Processes all HTML files in the specified directory, extracts texts from the given username,
    and saves the results into the output file.
    """
    all_texts = []

    # Loop through each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            file_path = os.path.join(directory, filename)
            print(f"Processing file: {file_path}")  # Indicate the file being processed
            user_texts = extract_user_texts(file_path, username)
            all_texts.extend(user_texts)  # Collect all messages

    # Write all extracted texts to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        for idx, text in enumerate(all_texts, 1):
            file.write(f"{idx}. {text}\n")

    print(f"Texts from '{username}' have been saved to {output_file}")  # Final message after processing

# Specify the directory containing the HTML files, the username, and the output file path
directory_path = r'C:\Users\example\OneDrive\Desktop\scparser\py\html_files'  # Update this line
username = 'snapchat_username'
output_file_path = 'extracted_texts.txt'

# Process the HTML files and save the extracted texts
process_multiple_html_files(directory_path, username, output_file_path)