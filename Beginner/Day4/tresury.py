
map = ['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']

first_digit = int(input("Row"))
second_digit = int(input("Column"))

map[first_digit][second_digit] = " X"
print(f" {map[0]} \n {map[1]} \n {map[2]}")
