from deep_translator import GoogleTranslator

# Function to translate text from German to Spanish


def translate_to_german(text):
    # Translate from German to Spanish
    translator = GoogleTranslator(source='es', target='de')
    return translator.translate(text)


# Input text from the user
text_to_translate = input("Enter Spanish text to translate to German: ")
translated_text = translate_to_german(text_to_translate)

print(f"The translation of '{text_to_translate}' is: '{translated_text}'")
