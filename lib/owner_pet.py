class Pet:
    # Define a class variable for valid pet types
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    # Define a class variable to store all Pet instances
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name

        # 1. Validate pet_type using the class variable
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Must be one of {Pet.PET_TYPES}")
        self.pet_type = pet_type

        # 2. Initialize owner attribute
        self._owner = None 
        if owner is not None:
             # If an owner is passed, ensure it's an Owner instance
            if not isinstance(owner, Owner):
                raise Exception("Owner must be an instance of the Owner class.")
            self._owner = owner
            
            owner._pets.append(self)

        # 3. Store the instance in the class variable 'all'
        Pet.all.append(self)

    # Property to manage the owner attribute
    @property
    def owner(self):
        return self._owner

    # Setter to ensure only Owner instances can be assigned
    @owner.setter
    def owner(self, new_owner):
        if new_owner is not None and not isinstance(new_owner, Owner):
            raise Exception("Owner must be an instance of the Owner class.")
        self._owner = new_owner
pass


class Owner:
    def __init__(self, name):
        self.name = name
        # Initialize an empty list to store pets specific to this owner
        self._pets = []

    # 1. Method to return a full list of the owner's pets
    def pets(self):
        return self._pets

    # 2. Method to add a pet to the owner
    def add_pet(self, pet):
        # Validate that the passed object is an instance of Pet
        if not isinstance(pet, Pet):
            raise Exception("Can only add instances of the Pet class.")

        # Check if the pet is already owned by this owner
        if pet not in self._pets:
            # Add pet to the owner's list
            self._pets.append(pet)
            # Assign this owner to the pet (establishing the one-to-many link)
            pet.owner = self

    # 3. Method to return a sorted list of pets by their names
    def get_sorted_pets(self):
        # Return a new list, sorted by the pet's 'name' attribute
        return sorted(self._pets, key=lambda pet: pet.name)
pass
