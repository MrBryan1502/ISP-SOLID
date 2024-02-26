# Principio de Segregación de Interfaces 👨‍👦

## Practica Aplicano el ISP 💥

[❎] Utilizando el ejemplo que dejamos más abajo, o cualquier otro con el que te gustaría practicar, realiza los cambios que consideres necesarios para ue se respete este principio.

```Java
public interface Animal {
    void fly();
    void run();
    void bark();
}

public class Dog implements Animal {
    @Override
    public void fly() { }

    @Override
    public void run() {
        System.out.print("Dog is running");
    }

    @Override
    public void bark() {
        System.out.print("Dog is barking");
    }
}

public class Bird implements Animal {
    public void bark() { }
    public void run() {
        System.out.print("Bird is running");
    }
    public void fly() {
        System.out.print("Bird is flying");
    }
}
```