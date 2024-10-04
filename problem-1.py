class Employee:
    # Constructor
    def __init__(self, name, hours, rate, withholding_rate, levy):
        self.name = name
        self.hours = hours
        self.rate = rate
        self.withholding_rate = withholding_rate
        self.levy = levy
        self.gross = self.rate*self.hours
        

    # Creates the pay slip as a string
    def __str__(self) -> str:
        # Splits the name and gets the last name
        # Turns the hours and the rate into floats to match the example
        # Convert the tax and levy into percentages then calculates the deductions
        return f'''
        ------- PAY SLIP ------- 
        Employee Name: {self.name.split(" ")[-1:][0]}
        Hours Worked: {float(self.hours)}
        Pay Rate: ${float(self.rate)}
        Gross Pay: ${self.gross}
        Deductions:
            ATO tax ({self.withholding_rate*100}%): %{self.gross*self.withholding_rate}
            Medicare Levy ({self.levy*100}%): ${self.gross*self.levy}
            Total Deductions: ${(self.gross*self.withholding_rate) + (self.gross*self.levy)}
        Net Pay: ${self.gross - (self.gross*self.withholding_rate + self.gross*self.levy)}
        ------- END -------
    '''


# Creates an employee object
a = Employee(input("Enter your name: "), float(input("Enter the hours worked: ")), 
             float(input("Enter the pay rate: ")), float(input("Enter the withholding rate: ")), float(input("Enter the levy: ")))
# Prints the pay slip
print(str(a))