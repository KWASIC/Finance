# Yearly revenue
Yearly_revenue = {
    'Year_one': 20,
    'Year_two': 55,
    'Year_three': 32,
    'Year_four': 70,
    'Year_five': 70,
    'Year_six': 90,
    'Year_seven': 80,
}

# Function to evaluate financial performance based on difference between two chosen years
def evaluate_profitability(initial_year, final_year):
    if initial_year not in Yearly_revenue.keys() or final_year not in Yearly_revenue.keys():
        print("Invalid years. Please choose years from the provided options.")
        return
    
    profit_initial_year = Yearly_revenue[initial_year]
    profit_final_year = Yearly_revenue[final_year]

    difference = profit_final_year - profit_initial_year

    if difference > 0:
        print("Company is in profit")
    elif difference < 0:
        print("Company running at a loss.")
    else:
        print("Stable profit.")

#Compare difference between two different yearly revenues
initial_year = input("Choose initial year: ")
final_year = input("Choose final year: ")
evaluate_profitability(initial_year, final_year)
