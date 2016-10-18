pseudocode

HPS(n):
  root <- sqrt(n)    // Root the number given 
  
  floor_n <- int(root)   // Round root to a int 
  ceil_n <- floor_n + 1  // Create ceil int
  
  // Square both integers
  floor_n_square <- floor_n * floor_n
  ceil_n_square <- ceil_n * ceil_n
  
  // Calcute sqaure closest to the original
  floor_gap <- n - floor_n_square
  ceil_gap <- ceil_n_square - n
  if floor_gap < ceil_gap then
    print floor_n_squard
  else 
    print ceil_n_squard
  
  
