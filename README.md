# Rule Engine with Abstract Syntax Tree (AST)

## Overview

This project is a simple 3-tier rule engine application to determine user eligibility based on attributes like age, department, income, and spend. The system uses an Abstract Syntax Tree (AST) to represent conditional rules and allows dynamic creation, combination, and modification of these rules.


## Key Features

- **AST-Based Rule Representation**: Use AST for representing rules, enabling flexibility and dynamic changes to rule structures.
- **Dynamic Rule Creation and Combination**: Easily create and modify eligibility rules.
- **Efficient Evaluation**: Evaluate rules efficiently based on user attributes.
- **Error Handling and Validation**: Manage invalid inputs and unsupported operations gracefully.
  
## Preview
![Screenshot 2024-10-26 162247](https://github.com/user-attachments/assets/87a2498d-0b4b-4968-be7b-eb9364851a99)
![Screenshot 2024-10-26 162325](https://github.com/user-attachments/assets/9b43eaa2-4d9c-4864-bdb3-415282a62ec3)


## Setup Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo/rule-engine.git
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Configure the database in `config.py`.
4. Run migrations to set up the database schema.
5. Start the application:
    ```bash
    python app.py
    ```

## Data Structure for AST

The AST is represented as a binary tree using nodes with the following fields:
- **type**: `"operator"` (for `AND`, `OR`) or `"operand"` (for conditions).
- **left**: Reference to the left child node.
- **right**: Reference to the right child node (for operators).
- **value**: Value associated with operand nodes (e.g., `age > 30`).

Example of a Node structure:
```python
class Node:
    def __init__(self, type, left=None, right=None, value=None):
        self.type = type
        self.left = left
        self.right = right
        self.value = value
```

## Sample Rules

- **Rule 1**: `((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)`
- **Rule 2**: `((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)`

## Testing

1. **Test `create_rule`**: Verify that each rule string translates to an AST accurately.
2. **Test `combine_rules`**: Ensure that combining rules results in a logical AST.
3. **Test `evaluate_rule`**: Check rule evaluation against sample JSON data.

### Example Test Case
```python
# Example input data
data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}
# Expected result based on Rule 1: True
result = evaluate_rule(combined_rule_ast, data)
assert result == True
```
