from pants import Pants


class SalesPerson:
    def __init__(self, sp_first_name, sp_last_name, sp_employee_id, sp_salary):
        self.first_name = sp_first_name
        self.last_name = sp_last_name
        self.employee_id = sp_employee_id
        self.salary = sp_salary
        self.pants_sold = []
        self.total_sales = 0

    def sell_pants(self, _pants):
        self.pants_sold.append(_pants)

    def display_sales(self):
        for pants in self.pants_sold:
            print('color: ', pants.color, 'waist_size: ', pants.waist_size, 'length: ', pants.length, 'price: ',
                  pants.price)

    def calculate_sales(self):
        for pants in self.pants_sold:
            self.total_sales += pants.price
        return self.total_sales

    def calculate_commission(self, percentage):
        return self.total_sales * percentage


pants_one = Pants('red', 35, 36, 15.12)
pants_two = Pants('blue', 40, 38, 24.12)
pants_three = Pants('tan', 28, 30, 8.12)

salesperson = SalesPerson('Amy', 'Gonzalez', 2581923, 40000)

salesperson.sell_pants(pants_one)
salesperson.sell_pants(pants_two)
salesperson.sell_pants(pants_three)

salesperson.display_sales()
