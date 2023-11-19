def even_number_generator():
    last = 0
    def generate():
        nonlocal last
        result = last
        last += 2
        return result
    return generate

gen = even_number_generator()

for i in range(10):
    print(gen())
