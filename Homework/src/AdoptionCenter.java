//https://www.w3schools.com/java/ref_arraylist_add.asp
//https://www.w3schools.com/java/java_user_input.asp
//https://www.w3schools.com/java/java_ref_arraylist.asp
//https://www.w3schools.com/java/ref_string_equals.asp

import java.util.ArrayList;

public class AdoptionCenter {
    private ArrayList<Pet> pets;

    public AdoptionCenter() {
        pets = new ArrayList<>();
    }

    public void addPet(Pet pet) {
        pets.add(pet);
        System.out.println(pet.getName() + " is now within the adoption center");
    }

    public void displayAvailablePets() {
        boolean found = false;
        int i = 0;
        while (i < pets.size()) {
            Pet pet = pets.get(i);
            if (pet.isAdopted() == false) {
                pet.displayInfo();
                found = true;
            }
            i++;
        }
        if (found == false) {
            System.out.println("All pets are currently adopted");
        }
    }

    public void adoptPet(String name) {
        int i = 0;
        boolean found = false;
        while (i < pets.size()) {
            Pet pet = pets.get(i);
            if (pet.getName().equals(name) && pet.isAdopted() == false) {
                pet.adopt();
                System.out.println(name + " has been adopted");
                found = true;
                break;
            }
            i++;
        }
        if (found == false) {
            System.out.println("Pet not found or already adopted");
        }
    }

    public void displayAllPets() {
        if (pets.isEmpty()) {
            System.out.println("No pets in the adoption center.");
            return;
        }

        int i = 0;
        while (i < pets.size()) {
            Pet pet = pets.get(i);
            pet.displayInfo();
            i++;
        }
    }
}
