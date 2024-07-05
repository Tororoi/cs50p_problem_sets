# Convert emoticons to emojis
def main():
  text = input("Enter text: ")
  converted_text = convert(text)
  print(converted_text)

def convert(text):
  text = text.replace(':)', '🙂')
  text = text.replace(':(', '🙁')
  return text

main()
