import argparse

# Set up the parser
p = argparse.ArgumentParser(description="Feature-rich CLI Calculator")

# Positional arguments
p.add_argument("a", type=float, help="First number")
p.add_argument("b", type=float, help="Second number")

# Optional arguments
p.add_argument("--opp", choices=["add", "sub", "mul", "div"], default="add", help="Operation to perform")
p.add_argument("--verbose", "-v", action="store_true", help="Print operation details")
p.add_argument("--round", type=int, help="Round result to N decimal places")

# Parse arguments
args = p.parse_args()

try:
    if args.opp == "add":
        result = args.a + args.b
        op_text = "Adding"
    elif args.opp == "sub":
        result = args.a - args.b
        op_text = "Subtracting"
    elif args.opp == "mul":
        result = args.a * args.b
        op_text = "Multiplying"
    elif args.opp == "div":
        if args.b == 0:
            raise ZeroDivisionError("You can't divide by zero.")
        result = args.a / args.b
        op_text = "Dividing"

    if args.round is not None:
        result = round(result, args.round)

    if args.verbose:
        print(f"{op_text} {args.a} and {args.b}")
    print("Result:", result)

except Exception as e:
    print("Error:", e)
