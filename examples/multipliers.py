def create_multiplier(x):
    def mul(y):
        return x * y
    return mul

multipliers = []
for x in range(1, 4):
    multipliers.append(create_multiplier(x))


print(f"{multipliers[0](10)} {multipliers[1](10)} {multipliers[2](10)}")
