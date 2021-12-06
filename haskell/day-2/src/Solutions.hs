module Solutions where

import System.IO

getInput = do
    contents <- lines <$> readFile "src/input.txt"
    let input = words <$> contents
    return input

parseInput :: [[String]] -> [(String, Int)]
parseInput x = zip (map head x) (castToInt (map last x))

castToInt :: [String] -> [Int]
castToInt = map read

first = do
    inp <- getInput
    let instructions = parseInput inp
    let coords = map move instructions
    let position = foldr sumCoords [0, 0] coords
    print (product position)

move :: (String, Int) -> [Int]
move (dir, dis) = case dir of
    "forward" -> [dis, 0]
    "up" -> [0, -dis]
    "down" -> [0, dis]

sumCoords x y = zipWith (+) x y

second = do
    inp <- getInput
    let instructions = parseInput inp
    let position = foldl (\x y -> updatePosition x y) [0, 0, 0] instructions
    print (position !! 0 * position !! 1)

updatePosition :: [Int] -> (String, Int) -> [Int]
updatePosition pos (dir, dis) = case dir of
    "forward" -> [pos !! 0 + dis, pos !! 1 + (dis * (pos !! 2)), pos !! 2]
    "up" -> [pos !! 0, pos !! 1, pos !! 2 - dis] 
    "down" -> [pos !! 0, pos !! 1, pos !! 2 + dis] 