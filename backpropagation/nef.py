def calculate_h(z, z_star):
    n = len(z)  
    squared_diff_sum = 0
    
    for t in range(n):
        squared_diff = (z[t] - z_star[t]) ** 2
        squared_diff_sum += squared_diff            #h = 1/2 Σ (Z(t)-Z*(t))^2
       #1/2#
    h = 0.5 * squared_diff_sum                      #[1, 2, 3, 4]
    return h                                        #[2, 3, 4, 5]

z = [1, 2, 3, 4] 
z_star = [2, 3, 4, 5]                               #(1-2)**2 == 1
                                                    #(2-3)**2 == 1           #4 * 0.5 == 2.0
result = calculate_h(z, z_star)                     #(3-4)**2 == 1
print(result)                                       #(4-5)**2 == 1
