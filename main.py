#TharinduRamanayake

bill = input("What was the total bill:")
bill_int = float(bill)

tip = input("What percentage tip would you like to give ? 10%, 12% or 15%: ")
tip_int = int(tip)

split = input("How many people to split the bill: ")
split_int = int(split)

each_person_bill = (bill_int/split_int)

each_person_tip = (tip_int/100)
each_person_tip = (each_person_bill *each_person_tip)

each_person_pay = each_person_bill + each_person_tip

# each_person_pay = "{:.2f}".format(each_person_pay) <-- Also use for round 2 decimal places

each_person_pay = round(each_person_pay,2)
print (f"each person should pay ${each_person_pay}")
