class Loan:
    name = 'My loan Calculator' # static variable

    def __init__(self,principle=0, interest_rate=0.0, year=0):
        """
        Constructor of the Loan
        :param principle: a principle amonuth
        :param interest_rate: a interest rate
        :param year: a year
        """
        self.principle = principle
        self.interest_rate = interest_rate
        self.year = year

    def __str__(self):
        """
        Human readable Loan object value
        :return: a string
        """
        return 'My Loan for principle {} interest rate {} and year '\
            .format(self.principle, self.interest_rate, self.year)

    def calculate_loan(self): # is implemented in the subclass
        pass

