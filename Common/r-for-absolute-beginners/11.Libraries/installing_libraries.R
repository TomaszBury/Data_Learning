# install.packages("ggplot2")
# install.packages("xlsx")

# Make sure you have ggplot2 installed (you only need to do this once)
# install.packages("ggplot2")

# Load the ggplot2 library
library(ggplot2)

# Create some sample data
data <- data.frame(
  x = 1:5,
  y = c(2, 5, 3, 6, 4)
)

# Create a basic scatter plot
ggplot(data, aes(x = x, y = y)) +
  geom_point() +
  labs(title = "Tiny ggplot Showcase", x = "X-axis", y = "Y-axis")
