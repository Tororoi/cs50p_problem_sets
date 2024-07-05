# Slow user's input by replacing whitespace with ellipses (...)
def main():
    # Get text from the user
    text = input()
    # Replace whitespace with ellipses
    text = text.replace(' ', '...')
    # Print out the text with ellipses
    print(text)

main()
