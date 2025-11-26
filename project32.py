class dog:
    species = "canis familiaris"
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def display(self):
        print(f"name: {self.name}")
        print(f"breed: {self.breed}")
        print(f"species: {dog.species}")
dog1 = dog("fon", "retriever")
dog2 = dog("leo", "golden retriever")
dog1.display()
dog2.display()