"""
Author: Rahula Krishnan Pakkiri Swamy
Class: CS 521 - Summer 2
Date: Aug 9th 2020
Homework Problem # 5.15.5
Description of Problem:Recursive componnd interest calculator
"""

import sys
import datetime
from os import path

from termproject.Loan import Loan


class Mortgage(Loan):
    """
    The Mortgage class inherit the Loan class
    The class is used to calculate the mortgage monthly payment and generate the
    report.
    """

    name = "My Mortgage Calculator"  # static same for all instance of mortgage
    __disclosure_file = 'disclosure_agreement.txt'  # private does allow changes

    def __init__(self, principle=0, interest_rate=0.0, year=0):
        """
        The Constructor of the Mortgage class. instance the private and public
        attribute.
        """

        super().__init__(principle, interest_rate, year)
        self.principle = principle
        self.interest_rate = interest_rate
        self.year = year
        # private variable
        self.__date_of_calc = datetime.datetime.now()
        self.__percentage_interest = self.interest_rate / 100
        self.__months = self.year * 12
        # assert validation for the interest rate
        assert isinstance(interest_rate, float), 'is a not a float'

    def __str__(self):
        """
        The Human readable object value
        :return:
        """
        return "{} has calculated the mortgage repayment amount per month\n" \
               "based on the entered principle amount:${:,.2f} , interest " \
               "rate {:.2f}% \n" \
               "and number of years is {} as of date {}.\nThe " \
               "Monthly payment  is: $ {:,.2f}".format(Mortgage.name,
                                                       self.principle,
                                                       self.interest_rate,
                                                       self.year,
                                                       self.__date_of_calc,
                                                       self.calculate_loan())

    def __repr__(self):
        """
        Implement to show the object value in string format
        :return:
        """
        return "{} has calculated the mortgage repayment amount per month\n" \
               "based on the entered principle amount:${:,.2f} , interest " \
               "rate {:.2f}% \n" \
               "and number of years is {} as of date {}.\nThe " \
               "Monthly payment  is: $ {:,.2f}".format(Mortgage.name,
                                                       self.principle,
                                                       self.interest_rate,
                                                       self.year,
                                                       self.__date_of_calc,
                                                       self.calculate_loan())

    def get_principle(self):
        """
        The get method to get the principle
        :return: a principle
        """
        return self.principle

    def get_months(self):
        """
        Gets the months of the mortgage
        :return: returns the months. months is a private months. It is accessed
        usng the getter.
        """
        return self.__months;

    def get_percent_interest(self):
        """
        Gets the percent interest
        :return:
        """
        return self.__percentage_interest

    def __calculate_monthly_interest(self):
        """
        private method to get the percentage interest per month
        :return:
        """
        return self.__percentage_interest / 12

    def calculate_loan(self):
        """
        This method calculates the monthly loan month using the formula
        principle * ( monlty interest * (1+ monlty interest)** months ) /
        (1+monthy interest)** months -1

        :return:
        """
        # calc private method to calculate monthly interest
        monthly_interest = self.__calculate_monthly_interest()
        print(self.__months)
        print(self.principle)
        print(monthly_interest)
        # calc monthly payment.
        monthly_payment = self.principle * (monthly_interest *
                                            (
                        1 + monthly_interest) ** self.__months) / (
                                  (1 + monthly_interest) ** self.__months - 1)
        return monthly_payment

    def get_balance(self, payments):
        """
        This method get the balance using the payment parameter
        :param payments:  the payment of the months to year
        :return: a balance for the year
        """
        # calc monthly interest
        monthly_interest = self.__calculate_monthly_interest()
        m = 1 + monthly_interest

        # calculate balance
        balance = self.principle * (
                ((m ** self.__months) - (m ** payments)) / (
                (m ** self.__months) - 1))
        return balance

    def __add__(self, other):
        """
        Magic function to just used in the junit. this is used to add the
        two mortgage loans
        :param other: this ia another mortgage object to add
        :return: a added of the object.
        """
        add_mortgage = Mortgage(self.principle + other.principle,
                                self.interest_rate + other.interest_rate,
                                self.year + self.year)
        return add_mortgage

    def mortgage_detail_summary(self):
        """
        This method generate the detail summary of the mortgage loan. it will
        calculate the balance per year.
        :return: a dict of the detail summary
        """
        monthly = self.calculate_loan()
        report_dic = {'Year': [], 'Balance': [], 'Payments': []}
        years = []
        balance = []
        payments = []
        # loop through the year to get the balance and add to list
        for x in range(1, self.year + 1):
            mon = x * 12
            rem = self.get_balance(mon)
            years.append(x)
            balance.append(float(rem))
            payments.append(float(monthly * mon))
        # add to the dictionary
        report_dic['Year'] = years
        report_dic['Balance'] = balance
        report_dic['Payments'] = payments

        return report_dic

    def generate_report(self):
        detail_summary = self.mortgage_detail_summary()
        # open the report .
        file = open("report.txt", 'w')
        # Write the summary to the report file
        file.write("-" * 50)
        file.write("\n")
        file.write(f'{Mortgage.name} ! \n')
        file.write("-" * 50)
        file.write("\n")
        file.write("-" * 50)
        file.write("\n")
        file.write(f'Summary of your Mortgage is:  !\n')
        file.write(self.__str__())
        file.write("\n")
        file.write("-" * 50)
        file.write("\n")

        # The detail report in the table format using the docstring and format
        result = """{year:^12s}   {balance:^12s}   {payments:^12s} \n"""
        key_list = list(detail_summary.keys())
        file.write(result.format(year=key_list[0], balance=key_list[1],
                                 payments=key_list[2]))
        file.write("{:-^12}   {:-^12}   {:-^12} \n".
                   format('--------', '---------', '---------'))

        year = detail_summary['Year']
        balance = detail_summary['Balance']
        payment = detail_summary['Payments']
        # loop through each and every list to write to the file
        for i in range(len(year)):
            file.write("{year:^12} {balance:^14,.2f}   {payments:^14,.2f} \n"
                       .format(year=year[i],
                               balance=round(balance[i], 2),
                               payments=round(payment[i], 2)))
        file.close()

    @staticmethod
    def read_disclosure():
        """
        read the disclosure file to dispolay the disclosure
        :param file_name: the file name to read the file
        :return: a content of the file
        """
        if not path.isfile(Mortgage.__disclosure_file):
            print('File not found')
            sys.exit()  # exist the program

        # open the file to read the file
        file = open(Mortgage.__disclosure_file, 'r')

        # read the data from file
        disclosure_str = file.read()
        # close the file
        file.close()
        return disclosure_str


# This is main program for class mortgage
if __name__ == '__main__':
    mortgage_test = Mortgage(100000, 2.0, 10)
    mortgage_test2 = Mortgage(1000, 2.5, 20)

    interest_percent = 2.0 / 100
    months = 10 * 12

    # Unit Test
    # validation of the principle
    assert mortgage_test.get_principle() > 0, 'The Mortgage amount is Zero'

    # Unit test validation for the Mortgage name
    assert mortgage_test.name == 'My Mortgage Calculator', \
        'In correct Mortgage name '
    # Unit test validation for interest rate
    assert mortgage_test.get_percent_interest() == interest_percent, \
        'The Interest rate is not correct! '
    # Unit test validation for the year to months
    assert mortgage_test.get_months() == months, 'Invalid month calculation'

    print("ALL Unit Test Passed! ")

    print(mortgage_test)
    # show the magic function addition
    print(mortgage_test + mortgage_test2)

    # generate the report
    mortgage_test.generate_report()

    # eval implementation
    eval_result = eval(
        "principle * (monthly_interest * (1+ monthly_interest)**months)/"
        "((1+monthly_interest)**months - 1)",
        {"principle": 100000, "monthly_interest": 0.0016666666666666668,
         "months": months})
    print('eval', eval_result)
