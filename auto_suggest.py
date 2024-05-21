import re


def auto_suggest(words, subtext):
    if '*' in subtext:
        # Convert wildcard '' to regex '.'
        regex_pattern = re.escape(subtext).replace(r'\*', '.*')
        pattern = re.compile(f'^{regex_pattern}$', re.IGNORECASE)
    else:
        # Create a regex pattern to match the phrase as a substring
        regex_pattern = re.escape(subtext)
        pattern = re.compile(f'.*{regex_pattern}.*', re.IGNORECASE)
    
    # Filter words that match the pattern
    matching_words = [word for word in words if pattern.match(word)]
    return matching_words

# Function to take input from the user
def get_user_input():
    words_input = input("Enter up to 5 words with same spellings: ")
    words = [word.strip() for word in words_input.split(',')]

    subtext_input = input("Enter the subtext of the words: ")
    subtext= subtext_input.strip()

    return words, subtext

# Example usage
if __name__== "__main__":
    words, subtext = get_user_input()
    matching_words = auto_suggest(words, subtext)
    print("Matching words:",matching_words)
