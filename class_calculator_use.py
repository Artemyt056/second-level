from class_calculator import Calculator
import json


class CalculatorProgram:
    def __init__(self):
        self.calculator = Calculator()
        self.calc_history = {}

    def perform_operation(self, operation, x, y=None):
        if y is None:
            result = getattr(self.calculator, operation)(x)
            self.calc_history[f"{operation}({x})"] = result
            return result
        else:
            result = getattr(self.calculator, operation)(x, y)
            self.calc_history[f"{x}{operation}{y}"] = result
            return result

    def save_history_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.calc_history, file)

    def load_history_from_file(self, filename):
        with open(filename, 'r') as file:
            self.calc_history = json.load(file)

    def sum_first_5_results(self):
        results = list(self.calc_history.values())[:5]
        return sum(results)


calc_program = CalculatorProgram()
calc_program.perform_operation("add", 4, 17)
calc_program.perform_operation("subtract", 25, 10)
calc_program.perform_operation("multiply", 5, 6)
calc_program.perform_operation("divide", 20, 4)
calc_program.perform_operation("power", 2, 3)
calc_program.perform_operation("square_root", 25)

calc_program.save_history_to_file("calc_history.json")

calc_program = CalculatorProgram()
calc_program.load_history_from_file("calc_history.json")

print("Історія дій калькулятора:")
for operation, result in calc_program.calc_history.items():
    print(f"{operation} = {result}")

print("Сума перших 5 результатів:", calc_program.sum_first_5_results())
