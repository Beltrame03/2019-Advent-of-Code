

def add(mass):
  mass = mass / 3
  mass = round(mass, 0)
  mass -= 2
  print(mass)
  return mass

def main():
  total = 0
  print("Input number of modules")
  modules = int(input())
  for i in range(modules):
    print("Input mass of module", i + 1)
    mass = int(input())
    total += add(mass)
  print("The total amount of fuel required is", total)

main()