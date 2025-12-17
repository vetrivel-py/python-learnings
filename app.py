def get_user_input():
    try:
        name=input("Enter the name: ")
        if not name:
            raise ValueError("Name cannot be empty.")
        
        age=int(input("Enter the age: "))
        if age <= 0:
            raise ValueError("Age must be a positive")
    

        return name , age 
    
    except ValueError as s:
         print("Input error:", s)
         return None,None
    
    except Exception as e:
        print("An unexpected error occurred:", e)
        return None, None


def save_to_file(text):
    with open("data.txt", "a") as file:
        file.write(text + "\n")

def main():

    name, age = get_user_input()

    if name is None:
        print("Failed to get valid user input.")
        return
    
    future_age=age+5
    message = f"Hello {name}, your age after 5 years will be {future_age}"

    print(message)
    save_to_file(message)
    print("Saved successfully")

if __name__== "__main__":
   main()


