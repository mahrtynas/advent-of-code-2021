module Main where

import MyLib (first, second)

main :: IO ()
main = do
  putStr "First solution: "
  MyLib.first
  putStr "Second solution: "
  MyLib.second
