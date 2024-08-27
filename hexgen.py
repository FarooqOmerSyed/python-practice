import random

def hex_generator(length = 6):
  
  if length <= 0:
    raise ValueError("Length can't be less than 6")
  
  hex_characters = "0123456789ABCDEF"
  hexcode = "".join(random.choice(hex_characters) for _ in range(length))
  return f"#{hexcode}"
  

if __name__ == "__main__":
  hexcode_length = int(input('enter the length: '))
  generated_hexcode = hex_generator(hexcode_length)
  print(f"Generated hexcode:{generated_hexcode}")

