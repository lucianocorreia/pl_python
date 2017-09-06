student = {
    "name": "Luciano",
    "student_id": 15163,
    "feedback": None
}

student["last_name"] = "Correia"

try:
    last_name = student["last_name"]
    numbered_last_name = 3 + last_name
except KeyError:
    print("Error finding last_name")

print("This code executed!")