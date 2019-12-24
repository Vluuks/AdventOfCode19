
def calc_fuel(m):
    return (m//3)-2

total = 0
with open("input1.txt") as f:
    lines = f.read()
    # print(lines)
    lineseroni = lines.split('\n')
    for line in lineseroni:

        if line != '':
            mass = int(line.strip())
            init_fuel = calc_fuel(mass)

            rf = init_fuel
            total += init_fuel
            while True:
                rf = calc_fuel(rf)
                
                if rf <= 0:
                    break
                
                total += rf

f.close()
print(total)