# Create 4D array
multidim <- array(1:4, dim = c(3, 4, 5, 2))

# Save number of dimensions
dimensions_n <- dim(multidim)

# Remove second element of fourth dimension
three_dim <- multidim[,,,1]

# Remove third, fourth, fifth elements of third dimension
three_dim_2 <- three_dim[,,1:2]

# Apply logarithm to last column (second dimension)
three_dim_2[,4,] <- log(three_dim_2[,4,])

# Raise first row to power of 5
three_dim_2[1,,] <- three_dim_2[1,,]^5

# Assign dimension names
dimnames(three_dim_2) <- list(
  c("Player 1", "Player 2", "Player 3"),
  c("Dexterity", "Strength", "Intelligence", "Speed"),
  c("House Stark", "House Lannister")
)

# Store Player 3's Intelligence from House Lannister
player_3_lan_int <- three_dim_2["Player 3", "Intelligence", "House Lannister"]

# Create 2x2 arrays for alpha_1 and alpha_2
alpha_1 <- array(c('A','B','C','D'), dim = c(2,2))
alpha_2 <- array(c('E','F','G','H'), dim = c(2,2))

# Combine arrays row-wise
combined_alpha <- rbind(alpha_1, alpha_2)