# ⭐ Pyramid Star Pattern in Python

## 📌 Output

```text
    *
   ***
  *****
 *******
*********
```

---

# 📘 Pyramid Star Pattern – Theory

The Pyramid Star Pattern is a popular Python pattern program used to understand nested loops, spacing logic, and pattern design.

In this pattern, stars are printed in the shape of a centered pyramid. The number of stars increases in every row while spaces decrease to maintain alignment.

---

## 🔹 Concepts Used

### ✅ Outer Loop
Controls the number of rows in the pyramid.

### ✅ Space Loop
Prints spaces before stars to align the pyramid at the center.

### ✅ Star Loop
Prints stars in odd-numbered sequence:
- 1
- 3
- 5
- 7
- 9

### ✅ Pattern Alignment
Spaces decrease while stars increase in each row.

---

## 🔄 Working Explanation

- The first row contains maximum spaces and 1 star.
- Each next row decreases spaces by 1.
- The number of stars increases by 2 in every row.
- This creates a symmetric pyramid structure.

---

## 🧠 Time Complexity

```text
O(n²)
```

The time complexity is `O(n²)` because nested loops are used for spaces and stars.

---

## 🎯 Learning Outcome

By practicing this pattern, beginners learn:

- Nested loops
- Space and alignment handling
- Pattern-building logic
- Row and column traversal

Pyramid patterns are important for improving logical thinking and loop understanding in programming.
