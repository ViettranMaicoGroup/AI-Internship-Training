from datetime import date

class Employee():
    def __init__(self, full_name, date_of_birth, position, skills, start_year):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.position = position
        self.skills = skills
        self.start_year = start_year # yyyy//mm//dd

class TechEmployee(Employee):
    def __init__(self, full_name, date_of_birth, position, skills, start_year, languages_program, projects):
        Employee.__init__(self, full_name, date_of_birth, position, skills, start_year)
        self.languages_program = languages_program
        self.projects = projects

class EmployeesList():
    employee_list  = []

    def add_employee(self, employee):
        self.employee_list.append(employee)

    def learned_employees(self):
        now = date.today()
        year_now = int(now.strftime("%Y"))
        employees = list(map(lambda x: (x, len(x.skills) * 10000 + (year_now - x.start_year)
                                        * 100 + (90 - ord(
            x.full_name.split()[len(x.full_name.split()) - 1][0].upper()))), self.employee_list))
        choosen = sorted(employees, key=lambda x: x[1], reverse=True)
        print("LIST OF PARTICIPANTS IN COURSE:")
        for i in range(3):
            try:
                print(f"""
                ID employee:  {i + 1}:
                Full Name : {choosen[i][0].full_name}
                Date of birth : {choosen[i][0].date_of_birth}
                Position : {choosen[i][0].position}
                Skills numbers : {len(choosen[i][0].skills)}
                Start years: {choosen[i][0].start_year}
                        """)
            except:
                return

class ListTechEmployee():
    tech_employee_list = []

    def add_tech_employee(self, tech_employee):
        self.tech_employee_list.append(tech_employee)

    def python_dev_list(self):
        employee_numbers = int(input("Enter number of employees: (number < adding tech employees numbers)): "))
        python_employees = list(filter(lambda x: "python" in x.languages_program, self.tech_employee_list))
        python_employees_having_projects = sorted(python_employees, key= lambda x:len(x.projects), reverse=True)
        print("*    List of employees selected using Python and having more projects: ")
        for i in range(employee_numbers):
            try:
                print(f"""
                        Employee {i + 1}, 
                        FullName: {python_employees_having_projects[i].full_name}
                        Date of Birth: {python_employees_having_projects[i].date_of_birth}
                        Position: {python_employees_having_projects[i].position}
                        Use python : {"python" in python_employees_having_projects[i].languages_program} 
                        Project numbers: {python_employees_having_projects[i].projects}
                        """)
            except:
                return

    def experience_dev_list(self):
        now = date.today()
        year_now = int(now.strftime("%Y"))
        emp_under_30 = list(filter(lambda x: (year_now - int(x.date_of_birth.split("/")[0]))>=30, self.tech_employee_list))
        emp_under_30_having_more_5_projects = list(filter(lambda x: len(x.projects) >=5 , emp_under_30))
        print("*    List of employees under 30 and having more 5 projects: ")
        for i in range(len(emp_under_30_having_more_5_projects)):
                print(f"""
                        Employee {i + 1}
                        FullName: {emp_under_30_having_more_5_projects[i].full_name}
                        Date of Birth: {emp_under_30_having_more_5_projects[i].date_of_birth}
                        Position: {emp_under_30_having_more_5_projects[i].position}
                        Project numbers: {emp_under_30_having_more_5_projects[i].projects}
                        """)

if __name__ == '__main__':
    #Case 1
    emp1 = Employee("Trần Văn A", "1975/5/6", "dev", ["group working", "english"], 2019)
    emp2 = Employee("Trần Văn B", "1977/9/6", "dev", ["english"], 2015)
    emp3 = Employee("Nguyễn Văn A", "1972/5/6", "dev", ["group working", "math"], 2010)
    emp4 = Employee("Trần Thanh D", "1980/5/6", "dev", ["group working", "english"], 2020)
    emp5 = Employee("Cao Văn A", "1985/5/6", "dev", ["group working", "english"], 2008)

    emp_list = EmployeesList()
    emp_list.add_employee(emp1)
    emp_list.add_employee(emp2)
    emp_list.add_employee(emp3)
    emp_list.add_employee(emp4)
    emp_list.add_employee(emp5)

    emp_list.learned_employees()

    #Case 2:
    tech_emp1 = TechEmployee("Trần Văn A", "1975/5/6", "dev", ["group working", "english"], 2019, ["c", "java"], ["proj1", "proj2"])
    tech_emp2 = TechEmployee("Trần Văn B", "1977/9/6", "dev", ["english"], 2015, ["c", "java", "python"], ["proj1", "proj2", "proj3", "proj4", "proj5"])
    tech_emp3 = TechEmployee("Nguyễn Văn A", "1972/5/6", "dev", ["group working", "math"], 2010, ["c", "java", "python"], ["proj1", "proj2", "proj3", "proj4", "proj5", "proj6"])
    tech_emp4 = TechEmployee("Trần Thanh D", "1980/5/6", "dev", ["group working", "english"], 2020, ["c", "python"], ["proj1", "proj2"])
    tech_emp5 = TechEmployee("Cao Văn A", "1985/5/6", "dev", ["group working", "english"], 2008, ["c", "java"], ["proj1"])

    tech_emp_list = ListTechEmployee()
    tech_emp_list.add_tech_employee(tech_emp1)
    tech_emp_list.add_tech_employee(tech_emp2)
    tech_emp_list.add_tech_employee(tech_emp3)
    tech_emp_list.add_tech_employee(tech_emp4)
    tech_emp_list.add_tech_employee(tech_emp5)
    tech_emp_list.python_dev_list()
    tech_emp_list.experience_dev_list()
