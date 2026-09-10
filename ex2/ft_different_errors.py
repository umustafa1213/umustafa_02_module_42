def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        69/0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "Hello World!" + 42
    else:
        return


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    print("Testing operation 0...")
    try:
        garden_operations(0)
    except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as e:
        print("Caught ValueError:", e)
    print("Testing operation 1...")
    try:
        garden_operations(1)
    except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as e:
        print("Caught ZeroDivisionError:", e)
    print("Testing operation 2...")
    try:
        garden_operations(2)
    except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as e:
        print("Caught FileNotFoundError:", e)
    print("Testing operation 3...")
    try:
        garden_operations(3)
    except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as e:
        print("Caught TypeError:", e)
    print("Testing operation 4...")
    try:
        garden_operations(4)
    except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError) as e:
        print("Caught error:", e)
    else:
        print("Operation completed successfully")
    print()
    print("All error types tested successfully")


if __name__ == "__main__":
    test_error_types()
