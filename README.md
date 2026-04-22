# SOLID Principles in Python 🧱

This project demonstrates the **SOLID design principles** using simple and practical Python examples.
Each principle is explained through two implementations:

* ❌ `bad.py` → Violates the principle
* ✅ `good.py` → Follows the principle

The goal of this repository is to help understand **why SOLID matters** and how to apply it in real-world code.

---

## 📂 Project Structure

```
solid-principles-python/
│
├── SRP/
│   ├── bad.py
│   └── good.py
│
├── OCP/
│   ├── bad.py
│   └── good.py
│
├── LSP/
│   ├── bad.py
│   └── good.py
│
├── ISP/
│   ├── bad.py
│   └── good.py
│
├── DIP/
│   ├── bad.py
│   └── good.py
│
└── README.md
```

---

## 🧠 What are SOLID Principles?

SOLID is a set of five design principles that help make software:

* Maintainable
* Scalable
* Testable
* Easy to understand

---

### 1. Single Responsibility Principle (SRP)

> A class should have only one reason to change.

* `bad.py`: One class handles multiple responsibilities
* `good.py`: Responsibilities are split into separate classes

---

### 2. Open/Closed Principle (OCP)

> Software entities should be open for extension but closed for modification.

* `bad.py`: Requires modifying existing code to add new behavior
* `good.py`: Uses abstraction to extend behavior without changing existing code

---

### 3. Liskov Substitution Principle (LSP)

> Subtypes should be replaceable with their base types without breaking functionality.

* `bad.py`: Subclass breaks expected behavior
* `good.py`: Subclasses properly extend base class behavior

---

### 4. Interface Segregation Principle (ISP)

> Clients should not be forced to depend on interfaces they do not use.

* `bad.py`: Large interface forces unnecessary implementation
* `good.py`: Smaller, specific interfaces are created

---

### 5. Dependency Inversion Principle (DIP)

> Depend on abstractions, not on concrete implementations.

* `bad.py`: High-level modules depend on low-level modules
* `good.py`: Both depend on abstractions (interfaces)

---

## 🚀 How to Run Examples

Each example is independent. You can run them directly:

```bash
python SRP/bad.py
python SRP/good.py
```

Similarly for other principles:

```bash
python OCP/bad.py
python OCP/good.py
```

---

## 🎯 Purpose of This Project

This repository is designed for:

* Developers learning system design and clean architecture
* Interview preparation (LLD / HLD)
* Understanding real-world code improvements

---

## 💡 Key Takeaway

Following SOLID principles leads to:

* Cleaner code
* Better separation of concerns
* Easier maintenance and scaling

---

## 🤝 Contributions

Asheesh Singh

---

## 📜 License

This project is open-source and available under the MIT License.