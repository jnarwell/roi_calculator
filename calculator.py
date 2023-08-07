class Property:
    def __init__(self):
        self.adress = input('What is the property adress? ').title()
        print('Please answer these questions about this property. For all yes or no questions please respond with \'y\' or \'n\' and for all others please type only the number value.')
        self.get_income()
        self.get_expenses()
        self.get_investment()
        self.calculate_roi()
    
    def get_income(self):
        self.units = int(input('How many units are on the property? '))
        self.rent = float(input('What is the monthly rent on each unit? '))
        self.extra_income = {}
        extra_rent = input('Does this property have any other income (laundry, storage, etc.)? ')
        while extra_rent.lower() != 'n':
            extra_rent = input('Please type the name of your aditional income source, if no more please type \'n\' ').title()
            if extra_rent.lower() != 'n':
                extra_rent_value = float(input('How much do you recieve from this source monthly? '))
                self.extra_income.update({extra_rent:extra_rent_value})

        print(f'The income breakdown for this property is:\nTotal Rent - ${self.units*self.rent}')
        self.total_income = 0
        self.total_income += self.units*self.rent
        for income_source in self.extra_income:
            print(f'{income_source} - ${self.extra_income[income_source]}')
            self.total_income += self.extra_income[income_source]
        print(f'Total Income (annual) - ${self.total_income*12}')

    def get_expenses(self):
        self.tax = {'Tax':float(input('What is the monthly tax on this property? '))}
        self.insurance = {'Insurance':float(input('What is the monthly insurance payment? '))}
        utilities = input('Do you pay for any utilities (water, gas, etc.)? ')
        self.utilities_list = {}
        while utilities.lower() != 'n':
            utilities = input('Please type the name of the utility, if no more please type \'n\' ').title()
            if utilities.lower() != 'n':
                utilities_value = float(input('How much do you pay monthly for this utility? '))
                self.utilities_list.update({utilities:utilities_value})
        self.hoa = {'HOA':float(input('What is the monthly HOA payment? '))}
        self.lawn = {'Lawn/Snow':float(input('What is the average monthly lawn/snow care payment? '))}
        self.vacancy = {'Vacancy':float(input('What is the average monthly vacancy payment? '))}
        self.repairs = {'Repairs':float(input('What is the average monthly repair payment? '))}
        self.capex = {'CapEx':float(input('What is the average monthly CapEx payment? '))}
        self.managment = {'Managment':float(input('What is the average monthly property managment payment? '))}
        self.mortgage = {'Mortgage':float(input('What is the average monthly mortgage payment? '))}
        self.expenses = [self.tax, self.insurance, self.hoa, self.lawn, self.vacancy, self.repairs, self.capex, self.managment, self.mortgage]

        self.total_expense = 0
        print(f'The expense breakdown for this property is:')
        for expense in self.expenses:
            for key in expense:
                if expense[key]!=0:
                    print(f'{key} - ${expense[key]}')
                    self.total_expense += expense[key]
        if len(self.utilities_list) != 0:
            print('Utilities:')
            for utility in self.utilities_list:
                print(f'\t{utility} - ${self.utilities_list[utility]}')
                self.total_expense += self.utilities_list[utility]
        print(f'Total Expense (annual) - ${self.total_expense*12}')

    def get_investment(self):
        self.down_payment = {'Down Payment':float(input('What was the down payment on this property? '))}
        self.closing_cost = {'Closing Cost':float(input('What were the closing costs on this property? '))}
        self.rehab = {'Rehab Cost':float(input('What was the rehab cost on this property? '))}
        self.misc = {'Miscellaneous':float(input('What were the miscellaneous costs on this property? '))}

        self.investments = [self.down_payment, self.closing_cost, self.rehab, self.misc]
        self.total_investment = 0
        print(f'The investment breakdown for this property is:')
        for investment in self.investments:
            for key in investment:
                if investment[key]!=0:
                    print(f'{key} - ${investment[key]}')
                    self.total_investment += investment[key]
        print(f'Total Investment - ${self.total_investment}')

    def calculate_roi(self):
        self.roi = ((self.total_income-self.total_expense)/self.total_investment)*100
        print(f'The ROI on the property at {self.adress} is {round(self.roi,1)}%')

property_1 = Property()