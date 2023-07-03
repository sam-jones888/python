def calculate_error(targets, outputs):
    squared_errors = [(t - o) ** 2 for t, o in zip(targets, outputs)]
    error = 0.5 * sum(squared_errors)
    return error

targets = [1, 2, 3]                       #E({wi,j}) = 1/2 Σ (tk - ok)^2
outputs = [0.8, 1.5, 2.7]

error = calculate_error(targets, outputs)
print("Error:", error)
