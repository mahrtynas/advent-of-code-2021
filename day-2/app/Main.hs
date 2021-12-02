module Main where

import Solutions(first, second)

main :: IO ()
main = do
  putStr "First solution: "
  Solutions.first
  putStr "Second solution: "
  Solutions.second
