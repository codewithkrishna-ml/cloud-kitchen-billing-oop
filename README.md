# Cloud Kitchen & Restaurant Billing System 🍳🧾

An operations-driven billing and workflow orchestration engine built in Python using core **Object-Oriented Programming (OOP)** patterns. This application models a full-scale commercial cloud kitchen, managing food menus, stateful passenger/customer ordering pipelines, cross-departmental operations (Billing Manager to Kitchen Processing), automated GST application, and live tracking of daily revenues.

---

## 🌟 About the Developer

*   **Age/Class:** 16 Years Old (Class 10th) 🎯
*   **Future Goal:** B.Tech in Artificial Intelligence and Machine Learning (AI-ML) -> **Aspiring ML Engineer at Google / Microsoft** 🤖⚡
*   **Milestone:** Successfully completed the **100 Days of Code** challenge!
*   **Current Focus:** Mastering Data Structures & Algorithms (DSA) and building data science frameworks with **NumPy** and **Pandas**.

---

## ✨ Key Features

*   **Dynamic Menu Cataloging:** Seamlessly expand your cloud kitchen catalog by adding dishes under distinct classifications (`Veg`, `Non-Veg`, `Beverage`) backed by unique item ID keys.
*   **Stateful Order Tracking Pipeline:** Monitors food orders interactively through real-time state changes as they transition across operations:
    *   `Received`: Order initialized at checkout.
    *   `Cooking`: Dispatched to the kitchen nodes.
    *   `Ready for Pickup/Delivery`: Marked cooked by kitchen operators.
    *   `Billed`: Payment processed successfully.
*   **Automated Commercial Billing Engine:** Instantly evaluates subtotal figures, appends standard financial fractions (`5% GST`), applies conditional percentage discount parameters, and outputs formatted receipts.
*   **Central Financial Dashboard:** Records cumulative income variables across billing cycles to showcase total real-time operational revenue status instantly.

---

## 🛠️ OOP Concepts & Architecture Demonstrated

This enterprise commercial simulation isolates different kitchen departments to enforce data integrity:
*   **Classes & System Abstraction:** Structured modularly around independent operational blueprints: `MenuItem` (dish properties), `Order` (transaction cart), `Kitchen` (cooking loop queue manager), and `BillingManager` (the main master control array database).
*   **Relational Aggregation & Composition:** The master `BillingManager` hosts a direct operational instance of the independent `Kitchen` class inside its constructor (`__init__`) alongside nested operational dictionaries, perfectly demonstrating a complex multi-tier component system.
*   **Isolated Data Mutation:** Modifies sensitive status flags and aggregates transaction sums through verified, specific methods (`add_item`, `send_to_kitchen`, `generate_bill`), strictly preventing direct out-of-scope properties overrides.

---

## 🚀 How to Run the Project

1.  **Clone the repository:**
    ```bash
    git clone https://github.com
    ```
2.  **Navigate to the project folder:**
    ```bash
    cd cloud-kitchen-billing-oop
    ```
3.  **Run the interactive framework menu loop:**
    ```bash
    python main.py
    ```

---

## 📝 Prerequisites
*   **Python 3.x** installed on your machine.
*   Runs completely on pure Python core architectures without needing external third-party library installations.

