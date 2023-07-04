def gradient_descent(w, learning_rate, gradients):
    new_w = []
    for i in range(len(w)):
        new_w.append(w[i] - learning_rate * gradients[i])
    return new_w

weights = [0.5, 0.3, 0.2]
gradients = [-0.8, 0.4, -0.6]                                      #wi,j(new) = wi,j(old) - α * ∂E/∂wi,j
learning_rate = 0.1
new_weights = gradient_descent(weights, learning_rate, gradients)
print("New weights:", new_weights)
