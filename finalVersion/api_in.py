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
        return definition 
    else:
        print("none")
        return None
    
def remove_square_brackets(input_string):
    return input_string.replace("[", "").replace("]", "")

        

def get_slanga_example(word):
    urban_dict = UrbanDict(word)
    results = urban_dict.search()
    if results:
        first_result = results[0]
        example = first_result.example
        return example
    else:
        return None
    
def translate_definition(definition, target_language='english'):
    # Translation API - Replace with your actual translation API endpoint and parameters
    # For demonstration, this is a placeholder function
    # You can use libraries like `googletrans` for actual translation
    return f"[Translated to {target_language}]: {definition}"

def main(word):
    while True:
        # Ask the user for a slang word to search
        #word = input("Enter a slang word to define (or type 'exit' to close the program): ").strip()  # User input for slang word
        
        # Check if the user wants to exit
        
        
        definition = get_slanga_definitions(word)
        example = get_slanga_example(word)
        if definition:
            word1=f"Word: {word}"
            word1u=remove_square_brackets(word1)
            word2=f"Definition: {definition}"
            word2u=remove_square_brackets(word2)
            #example = get_slanga_example(word)
            word3=f"Example: {example}"
            word3u=remove_square_brackets(word3)
            # Translate the definition to Spanish
            translated_definition = translate_definition(definition)
            return(word1u+"\n"+word2u+"\n"+word3u)
            
        else:
            print(f"No slang definition found for the word: {word}. Please try again.")
            
        break
    

# Example usage
