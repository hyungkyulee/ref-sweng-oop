# ref-sweng-oop

## C#
### Abstract Class and Interface
 : When you need a list of capabilities and data that are classes-agnostic, use an interface. When you need a certain object type to share characteristics, use an abstract class.
 
- Abstract Class (inheritent relation, same parent concept)
  - never intended to be instantiated directly
  - single-inheritence
  - must contain at least one abstract method (marked with the keyword or modifier 'abstract')
  - used to define a base class in the class hierarchy.
  - can have a non-abstract methods and interit to the base calss

- Interface Class (binding relation, abstract of abstract class)
  - all method must abstract methods
  - multi-inheritence
  - can have methods, properties, events, and indexers as its members
  - contain only the declaration of the members
  - an implementation given by the class who implements the interface implicitly or explicitly.

- Common Characteristics
  - declaration only, no implementation
  - no instantiated directly (new X)

### Delegates
 : How does C# handles the callback functions or event handler? The answer is - delegate.
 : Declare a delegate -> Set a target method -> Invoke a delegate
 
- use the 'delegate' keyword in front of return type
- can be declared outside of the class or inside the class
- way to use: 1) set the target method, 2) assign a method directly without creating an object of delegate, or 2) a lambda expression
- example
``` c#
public delegate void MyDelegate(string msg); // declare a delegate

// set target method
MyDelegate del = new MyDelegate(MethodA);
// or 
MyDelegate del = MethodA; 
// or set lambda expression 
MyDelegate del = (string msg) =>  Console.WriteLine(msg);

// target method
static void MethodA(string message)
{
    Console.WriteLine(message);
}
```
