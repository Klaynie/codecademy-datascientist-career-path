names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Add your code here

names.append("Priscilla")
insurance_costs.append(8320.0)

medical_records = list(zip(insurance_costs,names))

print(medical_records)

num_medicaL_records = len(medical_records)

print("There are " + str(num_medicaL_records) +" medical records.")

first_medical_record = medical_records[0]

print("Here is the first medical record:\n", first_medical_record)

sorted_medical_records = sorted(medical_records)

print("Here are the medical records sorted by insurance cost:\n", sorted_medical_records)

cheapest_three = sorted_medical_records[:3]

print("Here are the three cheapest insurance costs in our medical records:\n", cheapest_three)

priciest_three = sorted_medical_records[-3:]

print("Here are the three most expensive insurance costs in our medical records:\n", priciest_three)

occurrences_paul = names.count('Paul')

print("There are " + str(occurrences_paul) + " individuals with the name Paul in our medical records")