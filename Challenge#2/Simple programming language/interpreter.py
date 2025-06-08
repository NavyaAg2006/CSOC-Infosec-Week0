# Simple mini language interpreter for beginners with variable expression support
variables = {}

def run_line(line):
    line = line.strip()
    if not line or line.startswith('#'):
        return

    try:
        if line.startswith("let"):
            if "=" not in line:
                print("Error: '=' missing in let statement")
                return
            parts = line.split("=", 1)
            var_name = parts[0].replace("let", "").strip()
            expr = parts[1].strip()
            for var in variables:
                expr = expr.replace(var, str(variables[var]))
            value = eval(expr)
            variables[var_name] = value

        elif line.startswith("print"):
            expr = line[5:].strip()
            for var in variables:
                expr = expr.replace(var, str(variables[var]))
            print(eval(expr))

        else:
            print("Error: Unknown command")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    print("Enter your code line-by-line. Type 'return' to finish.")
    user_code = []
    while True:
        line = input(">> ").strip()
        if line.lower() == 'return':
            break
        user_code.append(line)

    for line in user_code:
        run_line(line)
