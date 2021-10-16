from termproject.Mortgage import Mortgage


def get_input(input_data):
    """
    The method get the input for the Mortagage calculator
    :param input_data:  a input dic object
    :return: a dict object
    """
    invalid_input = True
    while invalid_input:
        # get the inpout and add to key of the dictionary
        if input_data['principle'] is None:
            principle_str = input(
                'Enter the mortgage amount in dollars(ex: 100000): ').strip()
            try:
                input_data['principle'] = float(principle_str)
            except ValueError as ve:
                print(f"Invalid input mortgage amount {principle_str} \n"
                      f"Please re-enter the mortgage amount in the number "
                      f"format!")
                invalid_input = True
                continue
        # get the interest rate
        if input_data['interest_rate'] is None:
            interest_rate_str = input(
                'Enter the interest rate in percentage(ex 5 for 5%): ').strip()
            try:
                input_data['interest_rate'] = float(interest_rate_str)
            except ValueError as ve:
                print(f"Invalid input interest rate {interest_rate_str}. \n"
                      f"Please re-enter the interest rate in the number format")
                invalid_input = True
                continue
        # get the number of years
        if input_data['years'] is None:
            years_str = input('Enter the number of years in numbers'
                              '(ex:10 for 10 years) :').strip()
            try:
                input_data['years'] = int(years_str)
            except ValueError as ve:
                print(f"Invalid input years {years_str}.\n"
                      f"Please re-enter the years in the number format! ")
                invalid_input = True
                continue
        # change to invalid to false to stop the while loopo
        invalid_input = False


def display_report(dic):
    """
    The display report method used to display the report to user
    :param dic: a input dict alue to print the report
    :return: None
    """
    # format the result string to disply
    result = """{year:^12s}   {balance:^12s}   {payments:^12s} """
    key_list = list(dic.keys())
    print(result.format(year=key_list[0], balance=key_list[1],
                        payments=key_list[2]))
    print("{:-^12}   {:-^12}   {:-^12}  ".
          format('--------', '---------', '---------'))

    # Get the key value
    year = dic['Year']
    bal = dic['Balance']
    payment = dic['Payments']
    # display the values to detail the report
    for i in range(len(year)):
        print("{year:^12} {balance:^14,.2f}   {payments:^14,.2f}"
              .format(year=year[i],
                      balance=round(bal[i], 2),
                      payments=round(payment[i], 2)))


def display_summary(mortgage):
    """
    The display the summary of the mortagage calculator
    :param mortgage:  a mortgage object
    :return: None
    """
    print("-" * 50)
    print(f'{Mortgage.name} ! ')
    print("-" * 50)
    print('The Mortgage Principle Amount is $ {:,.2f} '
          .format(mortgage.principle))
    print('The interest rate of the mortgage loan in percentage is {:.2f}% '
          .format(mortgage.interest_rate))
    print('The annual interest rate of the mortgage loan is {:.2f}  '
          .format(mortgage.get_percent_interest()))
    print('The duration of this loan, that is the Loan Term (in months) '
          'is: {} '.format(mortgage.get_months()))
    print('The monthly payment for the loan term is {:,.2f} '
          .format(mortgage.calculate_loan(), 2))
    print("-" * 50)
    print(f'Summary of your Mortgage is:  ! ')
    print("-" * 50)
    print(mortgage)
    print("-" * 50)


# this is a main method for mortgage calculation
if __name__ == '__main__':

    EXIST_NOTE = """
    Thank you for using My Mortgage Calculator !! 
    Hope you enjoyed the Mortgage Calculator. 
    see you soon!! 
                 """
    EXIST_NOTE_CALC = """
       Thank you for using My Mortgage Calculator !! 
       Hope you got the idea of the mortgage calculator. 
       see you soon!! 
                    """
    # tuple to have the constant string to display
    note_tuple = (EXIST_NOTE, EXIST_NOTE_CALC)
    # input data dictionary to get the values
    input_data = {'principle': None, 'interest_rate': None, 'years': None}
    # read the file and display the disclosure
    print(Mortgage.read_disclosure())
    disclosure = input("To agree the disclosure Enter Y or any key to "
                       "exist : ")
    # condition check for the disclosure
    if disclosure == 'Y':
        get_input(input_data)
        mortgage = Mortgage(input_data['principle'],
                            input_data['interest_rate'],
                            input_data['years'])
        # call the summary method to display summary
        display_summary(mortgage)
        # get the input value to generate report
        generate_report = input(
            'Do you want the report of the Mortgage Calculation \n'
            'Enter Y for generating report or any key to '
            'exit! ')
        # condition check to generate the roeprt
        if generate_report == 'Y':
            # generate the report
            mortgage.generate_report()
            # get the detail report
            report_dic = mortgage.mortgage_detail_summary()
            # display summary and report
            display_summary(mortgage)
            display_report(report_dic)

        else:
            print(EXIST_NOTE[1])
    else:
        print(note_tuple[0])
