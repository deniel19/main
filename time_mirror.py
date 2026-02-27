# Online Python - IDE, Editor, Compiler, Interpreter
# Display all palindrome times in a day (24h format)


for ora in range(24):
    for minut in range(60):
        timp = f"{ora:02d}:{minut:02d}"
        # verificăm palindromul fără caracterul :
        if timp.replace(":", "") == timp.replace(":", "")[::-1]:
            print(timp)