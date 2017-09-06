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
except TypeError as error:
    print("I cant add these two together!")
    print(error)
except Exception:
    print("Unknown error!")

print("This code executes!")