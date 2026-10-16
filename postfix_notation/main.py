import sys


def eval_postfix(expression: str):
    tokens = expression.split()
    if not tokens:
        print("Передано пустое выражение, пожалуйста, повторите запуск и введите выражение:)")
        return None

    stack = []
    for token in tokens:
        if token in {"+", "-", "*", "/", "~"}:
            if len(stack) < 2:
                print(f"Для операции '{token}' не хватает операндов в стеке {stack}!")
                return None

            b = stack.pop()
            a = stack.pop()

            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                if b == 0:
                    print("Деление на ноль невозможно, извините, таковы правила(")
                    return None
                res = a / b
                stack.append(int(res) if res.is_integer() else res)
            elif token == "~":
                if a != 0 and b != 0:
                    stack.append(abs(a - b))
                else:
                    stack = [(sum(stack) + a + b) ** 2]
        else:
            try:
                val = float(token) if "." in token else int(token)
                stack.append(val)
            except ValueError:
                print(f"Неизвестный сиmвол '{token}'!")
                return None

        print(f"Токен: {token:>2} | Стек: {stack}")

    if len(stack) != 1:
        print(f"В стеке осталось несколько значений {stack}!")
        return None

    res = stack[0]
    return int(res) if isinstance(res, float) and res.is_integer() else res


def main():
    if len(sys.argv) > 1:
        expr = " ".join(sys.argv[1:])
    else:
        expr = input("Введите постфиксное выражение: ")

    result = eval_postfix(expr)
    if result is not None:
        print(f"{expr} = {result}")


if __name__ == "__main__":
    main()

