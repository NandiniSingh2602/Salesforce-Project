from typing import Union


class CalculatorBackend:
    """Simple calculator backend supporting basic arithmetic operations."""

    @staticmethod
    def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:


        
        return a + b

    @staticmethod
    def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        return a - b

    @staticmethod
    def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        return a * b

    @staticmethod
    def divide(a: Union[int, float], b: Union[int, float]) -> float:
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b

    @staticmethod
    def calculate(a: Union[int, float], b: Union[int, float], operation: str) -> Union[int, float]:
        operation = operation.lower()

        if operation == "add":
            return CalculatorBackend.add(a, b)
        if operation == "subtract":
            return CalculatorBackend.subtract(a, b)
        if operation == "multiply":
            return CalculatorBackend.multiply(a, b)
        if operation == "divide":
            return CalculatorBackend.divide(a, b)

        raise ValueError(f"Unsupported operation: {operation}")


if __name__ == "__main__":
    print("Calculator Backend Demo")
    print(CalculatorBackend.add(5, 3))
    print(CalculatorBackend.subtract(10, 4))
    print(CalculatorBackend.multiply(2, 6))
    print(CalculatorBackend.divide(9, 3))
