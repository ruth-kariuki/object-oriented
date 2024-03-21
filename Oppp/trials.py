class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I am {self.gender}.")

# Example usage
if __name__ == "__main__":
    person1 = Person("Antony", 35, "male")
    person1.introduce()

    person2 = Person("Ruth", 30, "Female")
    person2.introduce()

    person2 = Person("Mercy", 20, "Female")
    person2.introduce()


