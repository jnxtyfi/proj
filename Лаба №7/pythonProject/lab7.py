class Employee:
    def __init__(self, employee_name, employee_id):
        self.employee_name = employee_name
        self.employee_id = employee_id
    def get_info(self):
        return self.employee_id, self.employee_name

class Manager(Employee):
    def __init__(self, employee_name, employee_id, manager_departament=""):
        super().__init__(employee_name, employee_id)
        self.manager_departament = manager_departament
    def get_info(self):
        return super().get_info(), self.manager_departament
    def manage_project(self):
        return "he is managing project"

class Technician(Employee):
    def __init__(self, employee_name, employee_id, specialization=""):
        super().__init__(employee_name, employee_id)
        self.specialization = specialization
    def get_info(self):
        return super().get_info(), self.specialization
    def perform_maintenance(self):
        return "ok"

class TechManager(Manager, Technician):
    def __init__(self, employee_name, employee_id, specialization, manager_departament, new_employee_id = '', new_employee_name = ''):
        super().__init__(employee_name, employee_id)
        self.specialization = specialization
        self.manager_departament = manager_departament
        self.new_employee_name = new_employee_name
        self.new_employee_id = new_employee_id
        self.news = []
    def get_info(self):
        return super().get_info()

    def manage_project(self):
        return super().manage_project()

    def add_employee(self, new_employee_name, new_employee_id):
        new_employee = (new_employee_name, new_employee_id)
        self.news.append(new_employee)

    def get_team_info(self):
        return self.news




employ = Employee("John", "13234")
manag = Manager("Harry", "0909" , "X-106")
tech = Technician("Josh", "524" , "Progger")
techmanag = TechManager("Vladimir", "77", "Prezident", "Country RF")


techmanag.add_employee('Peter', 10)
techmanag.add_employee('Tambi', 160)
techmanag.add_employee('Joshua', 12784)



print(Employee.get_info(employ))
print(Manager.get_info(manag))
print(techmanag.get_info())
print(techmanag.get_team_info())