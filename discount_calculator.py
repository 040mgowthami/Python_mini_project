price = float(input("Enter Product Price: "))
discount = float(input("Enter Discount Percentage: "))
discount_amount = (price * discount) / 100
final_price = price - discount_amount
print("Discount Amount =", discount_amount)
print("Final Price =", final_price)
