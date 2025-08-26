class Pet
{
    private String name;
    private String species;
    private int age;
    private boolean isAdopted;


    public Pet(String name, String species, int age, boolean isAdopted) {
        this.name = name;
        this.species = species;
        this.age = age;
        this.isAdopted = isAdopted;
    }

    public String getName() {
        return name;
    }

    public boolean isAdopted() {
        return isAdopted;
    }

    public void adopt(){
        isAdopted = true;
    }

    public void displayInfo(){
        System.out.println("Name:" + name);
        System.out.println("Species:" + species);
        System.out.println("Age:" + age);
        System.out.println("Adopted:" + isAdopted);
    }
}