def are_collinear(x1, y1, x2, y2, x3, y3):
  area = (x2 - x1)*(y3 - y1)-(y2 - y1)*(x3 - x1)
  return area == 0

# Example usage:
point1 = (1, 2)
point2 = (3, 4)
point3 = (5, 6)

if are_collinear(*point1, *point2, *point3):
  print("The points are collinear.")
else:
  print("The points are not collinear.")
