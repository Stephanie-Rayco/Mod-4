'''Module 2: Individual Programming Assignment 1
Useful Business Calculations
This assignment covers your basic proficiency with Python.
'''

def savings(gross_pay, tax_rate, expenses):
    '''Savings.
    2 points.
    This function calculates the money remaining
        for an employee after taxes and expenses.
    
    To get the take-home pay of an employee, we will
        follow the following process:
        1. Apply the tax rate to the gross pay of the employee; round down
        2. Subtract the expenses from the after-tax pay of the employee
    Parameters
    ----------
    gross_pay: int
        the gross pay of an employee for a certain time period, expressed in centavos
    tax_rate: float
        the tax rate for a certain time period, expressed as a number between 0 and 1 (e.g., 0.12)
    expenses: int
        the expenses of an employee for a certain time period, expressed in centavos
    Returns
    -------
    int
        the number of centavos remaining from an employee's pay after taxes and expenses
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    gross_pay = int(input("Gross Pay:"))
    tax_rate = float(input("Tax Rate (a number between 0 and 1):"))
    expenses = int(input("Expenses:"))

    def savings(gross_pay, tax_rate, expenses):
        take_home_pay = (int((gross_pay * 100) - (gross_pay * tax_rate)) - expenses * 100)
        return take_home_pay
    
    print("The employee has", savings(gross_pay, tax_rate, expenses), "centavos remaining from his/her gross pay after taxes and expenses")

    
def material_waste(total_material, material_units, num_jobs, job_consumption):
    '''Material Waste.
    2 points.
    This function calculates how much material input will be wasted
        after running a certain number of jobs that consume
        a set amount of material.
    To get the waste of a set of jobs:
        1. Multiply the number of jobs by the material consumption per job.
        2. Subtract the total material consumed from the total material available.
    The users of this function also want you to format the output as a string, annotated with the
        units in which the material is expressed. Do not add a space between the number and the unit.
    Parameters
    ----------
    total_material: int
        the total material available
    material_units: str
        the units used to express a quantity of the material (e.g., "kg", "L", etc.)
    num_jobs: int
        the number of jobs to run
    job_consumption: int
        the amount of material consumed per job
    Returns
    -------
    str
        the amount of remaining material expressed with its unit (e.g., "10kg").
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    total_material = int(input("Total materials available: "))
    material_units = str(input("Material unit available: "))
    num_jobs = int(input("Number of jobs to run: "))
    job_consumption = int(input("Amount of materials consumed per job here:"))
    
    def material_waste(total_material, material_units, num_jobs, job_consumption):
        materials_used = (num_jobs * job_consumption)
        materials_available = (total_material - materials_used)
    
        return materials_available

    print("The amount of remaining material is ",material_waste(total_material, material_units, num_jobs, job_consumption),material_units,sep='')



def interest(principal, rate, periods):
    '''Interest.
    3 points.
    This function calculates the final value of an investment after
        gaining simple interest over a number of periods.
    To calculate simple interest, simply multiply the principal to the quantity (rate * time). 
        Add this amount to the principal to get the final value.
    Round down the final amount.
    Parameters
    ----------
    principal: int
        the principal (i.e., starting) amount invested, expressed in centavos
    rate: float
        the interest rate per period, expressed as a decimal representation of a percentage (e.g., 3% is 0.03)
    periods: int
        the number of periods invested
    Returns
    -------
    int
        the final value of the investment
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    principal = int(input("Amount invested in Pesos: "))
    rate = float(input("Interest rate per period, expressed as a decimal representation of a percentage: "))
    periods = int(input("Number of periods invested in Pesos: "))
    
    def interest(principal, rate, periods):
        sim_interest = (principal * 100 * rate * periods)
        new_principle = (sim_interest + principal)
    
        return new_principle

    print("The final value of the investment is ", int(interest(principal, rate, periods)),"centavos", sep ='')


def body_mass_index(weight, height):
    '''Body Mass Index.
    3 points.
    This function calculates the body mass index (BMI) of a person
        given their weight and height.
    The formula for BMI is: kg / (m ^ 2)
        (i.e., kilograms over meters squared)
    Unfortunately, the users of this function use the imperial system.
        You will need to first convert their arguments to the metric system.
    
    Parameters
    ----------
    weight: float
        the weight of the person, in pounds
    height: list
        the height of the person, expressed as a list of two integers.
        the first integer is the foot component of their height.
        the second integer is the inches component of their height.
        for example, 5'10" would be passed as [5, 10].
    Returns
    -------
    float
        the BMI of the person.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer
    your_weight = float(input("Weight in pounds: "))
    your_height = input("Height: ")
    digits_only = ""

    def body_mass_index(weight, height):
        weight_kg = weight / 2.205
        height_m = (float(height[0]) * 0.3048) + float(float(height[1:]) * 0.0254)
        bmi = weight_kg / (height_m ** 2)
    
        return bmi

    for i in your_height:
        if i.isdigit():
        digits_only += i

    height=(digits_only)

    print("Your BMI is", body_mass_index(your_weight, your_height))

