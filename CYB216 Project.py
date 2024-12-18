from collections import Counter


# Function to count the frequency of words in a file
def count_word_frequency(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()

        # Convert to lowercase and split the text into words
        words = text.lower().split()

        # Count the frequency of each word
        word_count = Counter(words)

        # Display the frequency of each word
        for word, count in word_count.items():
            print(f'{word}: {count}')
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Specify the path to your text file

file_path = r"C:\\Users\julianne\Desktop\Project.txt"

# Call the function
count_word_frequency(file_path)
