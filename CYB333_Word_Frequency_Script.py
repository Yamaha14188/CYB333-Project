import re
from collections import Counter

# List of specific keywords to count
KEYWORDS = ["failed login", "warn", "error"]

# Common stop words to exclude
STOP_WORDS = {"the", "and", "is", "to", "in", "of", "a", "for", "on", "at", "by", "an"}

# Function to count specific words in the log file
def count_keywords(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read().lower()  # Convert text to lowercase for case-insensitivity

        # Split text into words and filter out stop words
        words = re.findall(r'\b\w+\b', text)
        filtered_words = [word for word in words if word not in STOP_WORDS]

        # Count occurrences of specific keywords
        word_counts = Counter()
        for keyword in KEYWORDS:
            word_counts[keyword] = text.count(keyword.lower())

        # Return keyword counts
        return word_counts

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}

# Main script execution
if __name__ == "__main__":
    # File name
    file_name = "Example Sys Log.txt"

    # Count keywords in the log file
    keyword_counts = count_keywords(file_name)

    # Save results to a text file
    output_file = "keyword_counts.txt"
    with open(output_file, 'w', encoding='utf-8') as output:
        for keyword, count in keyword_counts.items():
            output.write(f"{keyword}: {count}\n")

    print(f"Keyword counts have been saved to {output_file}.")
