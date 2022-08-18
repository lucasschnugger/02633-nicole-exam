def parasites(x0, y10, y20, k, u, beta1, beta2, v1, v2, n):
    x=x0
    y1=y10
    y2=y20
    for num in range(n):
        dx=k-u*x-x*(beta1*y1+beta2*y2)
        dy1=y1*(beta1*x-u-v1)
        dy2=y2*(beta2*x-u-v2)
        x=x+dx
        y1=y1+dy1
        y2=y2+dy2
        r=y1/(y1+y2)
    return r
print(parasites(100, 10, 1, 2, 0.01, 0.0012, 0.01, 0.02, 0.01, 2))
