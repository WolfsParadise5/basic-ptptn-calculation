interest = 0.05
admin_percent_fee = 0.01

def calculate_admin_fee(due_amount):
    admin_fee = due_amount * admin_percent_fee
    return admin_fee
    
def calculate_year_topay(due_amount, if_pay):
    year = 0
    cumulative_paid = 0.00
    while due_amount > 0:
        #Print statements
        print(f'Year: {year}')
        print(f'Total Paid: {round(cumulative_paid, 2)}')
        print(f'Total left: {round(due_amount, 2)}')
        print()

        #Run calculations
        admin_fee = calculate_admin_fee(due_amount)
        paid_current_year = if_pay * 12 
        to_principal = paid_current_year - admin_fee
        if (due_amount - to_principal) > 0:
            due_amount -= to_principal
            cumulative_paid += paid_current_year
            year += 1
        else:
            month_count = 1
            while due_amount > 0:
                if if_pay > due_amount:
                    print()
                    print("Summary: ")
                    print()
                    print(f'Year: {year}')
                    print(f'Month: {month_count}')
                    print(f'Total Paid: {round(cumulative_paid, 2) + round(due_amount, 2)}')
                    print(f'Last Payment: {round(due_amount, 2)}')
                    print(f'Total left: {round(due_amount, 2) - round(due_amount, 2)}')
                    return 
                cumulative_paid += if_pay
                due_amount -= if_pay    
                print(f'Month: {month_count}')
                print(f'Total Paid: {round(cumulative_paid, 2)}')
                print(f'Total left: {round(due_amount, 2)}')
                month_count += 1
    


    

val_currentDue = float(input("Input due amount (in RM): "))
val_monthly = float(input("Enter monthly payment (in RM): "))

calculate_year_topay(val_currentDue, val_monthly)


