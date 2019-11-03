"""---author==hxj---"""


class Salary:
    def __init__(self, manager, programmer_hours, salesman_money):
        self.manager = manager
        self.programmer_hours = programmer_hours
        self.salesman_money = salesman_money

    def programmer(self):
        return self.programmer_hours * 200

    def salesman(self):
        return self.salesman_money * 0.05 + 1800


def main():

    salary = Salary(12000, 100, 1000)
    # programmer_money = salary.programmer(100)
    # salesman_total_money = salary.salesman(int(sys.argv[2]))
    # print(salary.programmer())
    # a = salary.programmer()
    # b = salary.salesman()
    salary_list = [salary.manager, salary.programmer(), salary.salesman()]
    #salary_list.append(a)
    # salary_list.append(b)
    # print(salary.manager)
    print(salary_list)
    # print(b)


# main()
if __name__ == '__main__':
    main()