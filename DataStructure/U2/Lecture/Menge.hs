data M = Le | Ei Int M | Lö Int M deriving Show

ie x Le = False
ie x (Ei y m)
 | x==y      = True
 | otherwise = ie x m

ie x (Lö y m)
 | x==y = False
 | otherwise = ie x m

ei = Ei
lö = Lö

