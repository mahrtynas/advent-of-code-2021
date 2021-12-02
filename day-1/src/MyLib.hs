module MyLib (first, second) where

import System.IO

getInput = do
    contents <- lines <$> readFile "src/input.txt"
    let input = read <$> contents :: [Int]
    return input


first = do
    inp <- getInput
    let a = init inp
        b = tail inp
    print (sum [1 | (x, y) <- zip a b, y > x])

second = do
    inp <- getInput
    let a = init (init (init inp))
        b = tail (tail (tail inp))
    print (sum [1 | (x, y) <- zip a b, y > x])
