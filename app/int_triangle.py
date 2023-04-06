class IntTriangle:
    def __init__(self, a: int, b: int, c: int) -> None:
        self.__input_validation(a, b, c)

        self.side_a = a
        self.side_b = b
        self.side_c = c

    def __input_validation(self, a: int, b: int, c: int) -> None:
        if not self.__input_is_positive(a, b, c):
            raise ValueError("Input must be positive")
        if not self.__input_is_integer(a, b, c):
            raise ValueError("Input must be integer")
        if not self.__input_meets_triangle_condition(a, b, c):
            raise ValueError("Input must meet triangle condition")

    def __input_is_positive(self, *args) -> bool:
        return all(arg > 0 for arg in args)

    def __input_is_integer(self, *args) -> bool:
        return all(isinstance(arg, int) for arg in args)

    def __input_meets_triangle_condition(self, a: int, b: int, c: int) -> bool:
        return a + b > c and b + c > a and c + a > b

    def perimeter(self) -> int:
        return self.side_a + self.side_b + self.side_c

    def area(self) -> float:
        area = self.__calculate_triangle_area()
        return round(area, 1)

    def __calculate_triangle_area(self) -> float:
        semi_perimeter = self.perimeter() / 2.0
        return (
            semi_perimeter
            * (semi_perimeter - self.side_a)
            * (semi_perimeter - self.side_b)
            * (semi_perimeter - self.side_c)
        ) ** 0.5
