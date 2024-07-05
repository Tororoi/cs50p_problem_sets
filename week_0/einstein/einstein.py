# Convert mass in kg to joules using E=mc^2
def main():
  # Speed of light constant
  C = 300000000
  mass = int(input("Enter mass in kg: "))
  energy = mass * C**2
  print(energy)

main()
