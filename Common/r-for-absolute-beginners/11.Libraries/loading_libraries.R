# install.packages("ggplot2")

library(ggplot2)

x_values <- seq(-5, 5, by = 0.1)
y_values <- x_values^2
data <- data.frame(x = x_values, y = y_values)

ggplot(data, aes(x = x, y = y)) +
  geom_line() +  # Use geom_line to draw a smooth curve
  labs(
    title = "Plot of y = x^2",
    x = "x",
    y = "x squared (x^2)"
  ) +
  theme_minimal()