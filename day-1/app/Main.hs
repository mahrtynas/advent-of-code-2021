module Main where

import MyLib (first, second)

main = do
  putStr "First solution: "
  MyLib.first
  putStr "Second solution: "
  MyLib.second
