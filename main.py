def are_tuples_equal(tuple1, tuple2):
    return sorted(tuple1) == sorted(tuple2)


a = (1, 2, 3, 4, 8)
b = (4, 3, 2, 1)
c = (1, 2, 3, 4)

result_ab = are_tuples_equal(a, b)
result_bc = are_tuples_equal(b, c)
result_ac = are_tuples_equal(a, c)

print(f"Чи рівні a та b: {result_ab}")
print(f"Чи рівні b та c: {result_bc}")
print(f"Чи рівні a та c: {result_ac}")
