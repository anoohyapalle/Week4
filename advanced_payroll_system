
class Employee:
    def __init__(self, name, hours_worked, hourly_rate):
        self.name = name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_pay(self):
        overtime_hours = 0
        regular_hours = self.hours_worked

        if self.hours_worked > 40:
            overtime_hours = self.hours_worked - 40
            regular_hours = 40

        regular_pay = regular_hours * self.hourly_rate
        overtime_pay = overtime_hours * (self.hourly_rate * 1.5)
        total_pay = regular_pay + overtime_pay

        return total_pay


class Manager(Employee):
    def __init__(self, name, hours_worked, hourly_rate, bonus):
        super().__init__(name, hours_worked, hourly_rate)
        self.bonus = bonus

    def calculate_pay(self):
        base_pay = super().calculate_pay()
        total_pay = base_pay + self.bonus
        return total_pay

employee = Employee("Anoohya", 45, 20)
employee_pay = employee.calculate_pay()
print(f"Total pay for {employee.name}: ${employee_pay:.2f}")

manager = Manager("Devika", 50, 30, 500)
manager_pay = manager.calculate_pay()
print(f"Total pay for {manager.name}: ${manager_pay:.2f}")
