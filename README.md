# 🔢 Sudoku Solver

A fast and efficient Python-based Sudoku solver that can crack any **valid** puzzle in **under half a second**.  
Whether you're testing logic or automating your puzzles, this tool handles it all with speed and precision.

---

## 💡 How It Works

Simply provide your Sudoku puzzle as a `9x9` grid, where:
- Each row is a list of integers
- Empty cells are represented by `0`

**Example input:**
```python
[
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
```

## 📱 Mobile App — *Coming Soon*

We're working on a mobile application that:

- 📷 Scans **live camera footage** to detect Sudoku puzzles  
- 🔢 Recognizes digits using **custom-trained computer vision models**  
- 🧩 **Overlays** the solution directly on the screen

### 🔧 Two Possible Approaches

**1. On-Device Processing**  
- Lightweight custom CV models optimized for mobile performance.

**2. Server-Side Processing**  
- Stream video to a server, process the puzzle, and return results — minimizing device load.

> Stay tuned for updates and beta releases!

---

## 📸 Vision for the Future

- Real-time puzzle detection from camera input  
- OCR for digit recognition  
- Augmented overlay of the solution  
- Native Android app with a clean UI

---

## 🤝 Feedback & Contributions

We’re open to:

- Feedback on features and performance  
- Ideas for the mobile version  
- Pull requests and code suggestions

Feel free to reach out or open an issue!

---

## 📄 License

**MIT License** — feel free to use and adapt with attribution.
