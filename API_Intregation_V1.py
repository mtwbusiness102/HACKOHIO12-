from pyurbandict import UrbanDict

def get_slanga_definitions(word):
    # Create an instance of UrbanDict
    urban_dict = UrbanDict(word)
    
    # Search for definitions
    results = urban_dict.search()
    
    # Check if there are any results
    if results:
        # Extracting the first definition
        first_result = results[0]
        definition = first_result.definition
        example = first_result.example
        return definition, example
    else:
        return None, None

def translate_definition(definition, target_language='english'):
    # Translation API - Replace with your actual translation API endpoint and parameters
    # For demonstration, this is a placeholder function
    # You can use libraries like `googletrans` for actual translation
    return f"[Translated to {target_language}]: {definition}"

def main():
    while True:
        # Ask the user for a slang word to search
        word = input("Enter a slang word to define (or type 'exit' to close the program): ").strip()  # User input for slang word
        
        # Check if the user wants to exit
        if word.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break
        
        definition, example = get_slanga_definitions(word)
        
        if definition:
            print(f"Word: {word}")
            print(f"Definition: {definition}")
            print(f"Example: {example}")
            
            # Translate the definition to Spanish
            translated_definition = translate_definition(definition)
            print(translated_definition)
        else:
            print(f"No slang definition found for the word: {word}. Please try again.")

if __name__ == "__main__":
    main()





