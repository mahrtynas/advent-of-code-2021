module MyLib (first, second) where


getInput = do
    contents <- words <$> readFile "src/input.txt"
    let input = read <$> contents :: [[Int]]
    return contents

toInt :: String -> [Int]
toInt = map (\x -> read (x:[]) :: Int)

transpose:: [[a]]->[[a]]
transpose ([]:_) = []
transpose x = (map head x) : transpose (map tail x)

dominant :: [Int] -> Int
dominant arr = if sum arr * 2 >= length arr
    then 1
    else 0

invert :: Int -> Int
invert x = if x == 0 then 1 else 0

binToDec :: [Int] -> Int
binToDec arr = sum [x * 2 ^ y | (y, x) <- zip [0..] (reverse arr)]

first = do
    inp <- getInput
    let bits = transpose (map toInt inp)
    let gamma = map dominant bits
        epsilon = map invert gamma
    print $ (binToDec gamma * binToDec epsilon)

filterArray :: [[Int]] -> Int -> Int -> [[Int]]
filterArray arr p v = [a | a <- arr, a !! p == v]

oxygenRating arr p = do
    let v = dominant [x !! p | x <- arr]
        subarr = filterArray arr p v
        nextp = succ p
    if length subarr == 1
        then subarr !! 0
        else oxygenRating subarr nextp

co2Rating arr p = do
    let v = invert $ dominant [x !! p | x <- arr]
        subarr = filterArray arr p v
        nextp = succ p
    if length subarr == 1
        then subarr !! 0
        else co2Rating subarr nextp


second = do
    inp <- getInput
    let bits = map toInt inp
        oxy = oxygenRating bits 0
        co2 = co2Rating bits 0
    print $ (binToDec oxy * binToDec co2)
    