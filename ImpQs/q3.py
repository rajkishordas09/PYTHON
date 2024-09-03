def paragraph_stats(paragraph):
  """
  Calculates line count, character count, and unique character count in a paragraph.

  Args:
      paragraph: A string representing the paragraph.

  Returns:
      A tuple containing the number of lines, total characters, and unique characters.
  """

  # Split the paragraph into lines
  lines = paragraph.splitlines()

  # Count total characters
  total_chars = len(paragraph)

  # Count unique characters using a set
  unique_chars = len(set(paragraph))

  return len(lines), total_chars, unique_chars

# Example usage
paragraph = "This is a sample paragraph. It has multiple lines and contains various characters."

lines, total_chars, unique_chars = paragraph_stats(paragraph)

print(f"Lines: {lines}")
print(f"Total characters: {total_chars}")
print(f"Unique characters: {unique_chars}")
