import prettytable
table = prettytable.PrettyTable()
numbers = [1, 2, 3, 4, 5]
names = ["Soham", "Amitabh", "Akash", "Souvik", "Subhasish"]
marks = [69, 55, 31, 87, 79]



table.add_column("Serial No", numbers)
table.add_column("Names", names)
table.add_column("Marks", marks)
table.align = "l"

print(table)