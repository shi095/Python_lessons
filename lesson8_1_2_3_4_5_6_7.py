# 4 5 6

class Warehouse_office_equipment:

    def __init__(self):
        self._dict = {}

    def add(self,office_equipment):
        return self._dict.setdefault(office_equipment.name, [office_equipment.year, office_equipment.country])

class Office_equipment:

    def __init__(self,name,year,country):
        self.name = name
        self.year = year
        self.country = country


class Printer(Office_equipment):
    def __init__(self,name,year,country,value):
        super().__init__(name,year,country)
        self.value = value


    def action(self):
        return f'Принтер {self.name} печатает {self.value} страниц в минуту.'

class Scanner(Office_equipment):
    def __init__(self,name,year,country,optical):
        super().__init__(name,year,country)
        self.optical = optical

    def action(self):
        return f'Сканер {self.name} cканирует c разрешением {self.optical} ppi.'

class Copier(Office_equipment):
    def __init__(self,name,year,country,color):
        super().__init__(name,year,country)
        self.color = color

    def action(self):
        return f'Ксерокc {self.name} делает {self.color} копии.'

warehouse = Warehouse_office_equipment()
printer = Printer ('HP',2020, 'США',100)
scanner = Scanner ('Canon',2018, 'Япония',300)
copier = Copier ('Xerox',2010, 'США','цветные')

warehouse.add(printer)
warehouse.add(scanner)
warehouse.add(copier)
print(warehouse._dict)

print(printer.action())
print(scanner.action())
print(copier.action())
