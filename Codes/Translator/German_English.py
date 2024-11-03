from deep_translator import GoogleTranslator

# Function to translate text from German to Spanish


def translate_to_english(text):
    # Translate from German to Spanish
    translator = GoogleTranslator(source='de', target='en')
    return translator.translate(text)


# Input text from the user
text_to_translate = input("Enter German Text to translate to English: ")
translated_text = translate_to_english(text_to_translate)

print(f"The translation of '{text_to_translate}' is: '{translated_text}'")
