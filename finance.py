Year_one = 20,
Year_two = 55,
Year_three = 32,
Year_four = 70,
Year_four = 70,
Year_five = 90,
Year_six = 80,


# Yearly revenue
Yearly_revenue = {
'1':Year_one,
'2':Year_two,
'3':Year_three,
'4':Year_four,
'5':Year_five,
'6':Year_six,
}


#def yearly_revenue():
  #  print(f"1.Year_one =: {Year_one} ")
  #  print(f"2.Year_two =: {Year_two} ")
   # print(f"3.Year_three =: {Year_three} ")
   # print(f"4.Year_four =: {Year_four} ")
   # print(f"5.Year_five =: {Year_five} ")
   # print(f"6.Year_six = : {Year_six} ")
initial_year = ("choose initial year: ")
final_year = ("choose final year")
for n in Yearly_revenue.keys():
        print(n)
        if initial_year > final_year:
             print("Companny is in profit")
        elif initial_year < final_year:
             print("Company running at a loss")
        else:
             print("Stable profit")
     
    



 
       
       
    
   
