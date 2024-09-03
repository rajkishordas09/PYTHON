def paragraph_stats(paragraph):
  lines = paragraph.splitlines()

  # Count total characters
  total_chars = len(paragraph)

  # Count unique characters using a set
  unique_chars = len(set(paragraph))

  return lines, total_chars, unique_chars

# Example usage
paragraph = '''This is a sample paragraph.
 It has multiple lines and
  contains various characters.'''

lines, total_chars, unique_chars = paragraph_stats(paragraph)

print(f"Lines: {lines}")
print(f"Lines: {len(lines)}")
print(f"Total characters: {total_chars}")
print(f"Unique characters: {unique_chars}")
