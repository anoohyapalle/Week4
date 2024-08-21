

from text_processing_tool import count_words, find_unique_words, convert_to_uppercase

def main():
    text = input("Enter a text string: ")

    print("Choose a text processing task:")
    print("1. Count words")
    print("2. Find unique words")
    print("3. Convert to uppercase")
    choice = input("Enter the number of your choice: ")

    if choice == "1":
        word_count = count_words(text)
        print(f"Number of words: {word_count}")
    elif choice == "2":
        unique_words = find_unique_words(text)
        print(f"Unique words: {unique_words}")
    elif choice == "3":
        uppercase_text = convert_to_uppercase(text)
        print(f"Text in uppercase: {uppercase_text}")
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
