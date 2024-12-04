def find_word(grid, word):
    def search_from(x, y, dx, dy):
        for i in range(len(word)):
            nx, ny = x + i * dx, y + i * dy
            if not (0 <= nx < len(grid) and 0 <= ny < len(grid[0])):
                return False
            if grid[nx][ny] != word[i]:
                return False
        return True

    directions = [
        (0, 1), (1, 0), (0, -1), (-1, 0),  # horizontal and vertical
        (1, 1), (-1, -1), (1, -1), (-1, 1)   # diagonal
    ]

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == word[0]:
                for dx, dy in directions:
                    if search_from(i, j, dx, dy):
                        count += 1

    return count

def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
    
    # Remove any leading/trailing whitespace and filter out empty lines
    word_search = [line.strip() for line in lines if line.strip()]
    
    word = "XMAS"
    count = find_word(word_search, word)
    print(f"The word '{word}' appears {count} times in the word search.")

if __name__ == "__main__":
    main()
