//https://www.w3schools.com/java/java_user_input.asp
//https://www.w3schools.com/java/ref_scanner_nextint.asp

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        AdoptionCenter adoptionCenter = new AdoptionCenter();

        adoptionCenter.addPet(new Pet("Marshmallow", "Cat", 3, false));
        adoptionCenter.addPet(new Pet("Bolt", "Dog", 2, false));
        adoptionCenter.addPet(new Pet("Peach", "Rabbit", 2, false));
        adoptionCenter.addPet(new Pet("Zigzag", "Lizard", 2, false));
        adoptionCenter.addPet(new Pet("Pebble", "Turtle", 4, false));
        adoptionCenter.addPet(new Pet("Fizz", "Bird", 9, false));
        adoptionCenter.addPet(new Pet("Waffles", "Hamster", 1, false));
        adoptionCenter.addPet(new Pet("Sushi", "Fish", 7, false));
        adoptionCenter.addPet(new Pet("Cricket", "Ferret", 3, false));
        adoptionCenter.addPet(new Pet("Tofu", "Mouse", 3, false));

        while (true) {
            System.out.println("\nPet Adoption Center Menu:");
            System.out.println("\n1. View available pets");
            System.out.println("2. Adopt a pet by name");
            System.out.println("3. Add a new pet");
            System.out.println("4. Exit the program");
            System.out.println("5. View all pets (including adopted)");
            System.out.print("\nEnter your choice: ");

            int decision = scanner.nextInt();
            scanner.nextLine();

            if (decision == 1) {
                adoptionCenter.displayAvailablePets();
            } else if (decision == 2) {
                System.out.print("Enter the name of the pet to adopt: ");
                String name = scanner.nextLine();
                adoptionCenter.adoptPet(name);
            } else if (decision == 3) {
                System.out.print("Enter pet name: ");
                String newName = scanner.nextLine();
                System.out.print("Enter species: ");
                String species = scanner.nextLine();
                System.out.print("Enter age: ");
                int age = scanner.nextInt();
                scanner.nextLine(); // Clear newline
                adoptionCenter.addPet(new Pet(newName, species, age, false));
            } else if (decision == 4) {
                System.out.println("Exiting program");
                break;
            } else if (decision == 5) {
                adoptionCenter.displayAllPets();
            } else {
                System.out.println("Invalid option. Out of bounds");
            }
        }
    }
}
