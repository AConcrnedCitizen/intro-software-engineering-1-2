class Employee:
    def __init__(self, name, hours, rate, withholding_rate, levy):
        self.name = name
        self.hours = hours
        self.rate = rate
        self.withholding_rate = withholding_rate
        self.levy = levy
        self.gross = self.rate*self.hours
        
    def __str__(self) -> str:
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
    
    
if __name__ == '__main__':
    a = Employee('John Smith', 10, 60.75, 0.30, 0.02)
    print(str(a))