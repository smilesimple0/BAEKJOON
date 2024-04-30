H,M = map(int,input().split())

if M>=45:
  print(H,M-45)
else:
  H = H - 1        # Minus yourself
  if H<0:
    H = 23
  print(H,60+M-45)
