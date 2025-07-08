"""
Task 3: AI-Powered Code Review

This file demonstrates how AI can review and improve a simple Python function.
The original function calculates the average of a list of numbers.
AI suggestions include:
- Using built-in functions for clarity
- Adding error handling
- Including a docstring

Summary:
I used an AI tool to review a basic Python function that calculates the average of a list. 
The AI suggested replacing the manual loop with Python’s built-in sum() function for better readability and performance. 
It also recommended adding error handling for empty lists to avoid division by zero, and including a docstring to improve documentation. 
These suggestions made the code cleaner, safer, and more maintainable. 
AI-powered code reviews are helpful because they provide instant feedback, catch common mistakes, and promote best practices. 
They’re especially useful for beginners learning to write clean code, or for experienced developers who want a second pair of eyes. 
While AI can’t replace human judgment in complex scenarios, it’s a powerful tool for improving code quality quickly and consistently.
"""

# 🔴 Original Code (Before AI Review)

def calc_tax():
    try:
        salary = float(input("Enter Monthly Salary"))
        if salary >= 50000:
            tax = salary * 0.25
            
        else:
            tax = salary * 0.10
        Gross_salary = salary  - tax     
        print(f"Your tax is :{tax:.2f}")   
        print(f"Net salary:{Gross_salary:.2f}")
    except ValueError:
        print("Please enter a valid number.")      
           
calc_tax()

# ✅ AI-Improved Code with chat gpt
def calculate_tax():
    """
    Calculates tax and net salary based on monthly income.
    Applies:
    - 25% tax for salaries >= 50,000
    - 10% tax for salaries < 50,000
    """
    try:
        salary = float(input("Enter your monthly salary: "))
        
        tax_rate = 0.25 if salary >= 50000 else 0.10
        tax = salary * tax_rate
        net_salary = salary - tax

        print(f"💰 Salary: KES {salary:,.2f}")
        print(f"🧾 Tax Rate: {int(tax_rate * 100)}%")
        print(f"📉 Tax Amount: KES {tax:,.2f}")
        print(f"✅ Net Salary After Tax: KES {net_salary:,.2f}")

    except ValueError:
        print("❌ Invalid input. Please enter a numeric salary amount.")

# Run the function
calculate_tax()


# 🔍 Example usage
if __name__ == "__main__":
    data = [10, 20, 30, 40]
    print("Original code:", calc_tax())
    print("Improved code:", calculate_tax())
    #print("Empty list average:", average([]))
