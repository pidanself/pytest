def T(n):
    if n==1:
        S=1
    else:
        S=2*T(n/3)+n
    return S
print(T(27))