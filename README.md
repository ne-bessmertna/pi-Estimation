# Monte Carlo π Estimation 

## Introduction

This project estimates the value of π using a Monte Carlo simulation and allows user to compare estimations to evaluate 
accuracy and consistency. It uses parallel computing with Python's `multiprocessing` module to speed up the computation.

## How It Works
### Background

If a quarter of a unit circle (i.e. radius equals 1) is placed into a unit square (i.e. side equals 1), a randomly chosen 
point inside the square may lay also inside the quarter of the circle. By taking a large amount of random points, 
the relation between the number of points inside the quarter circle to a total number of points represents approximated 
area of the qurter circle. Since area of a whole circle is given by  
$A = πr^2$,  
where A is area and r is radius, the area of qurter circle of radius 1 can be written as  
$A = ^π/_4$.  

Thus, estimated value of π can be calculated based on formula:  

$π ≈ 4 * \frac{\text{Number of points inside a quater circle}}{\text{Total number of points}}$

### Code

The program simulates random points inside a unit square and count the amount of points, falling inside a unit quarter 
circle. Then the estimation of π is conducted based on the formula above. 
Since random sampling introduces variation, running the estimation multiple times with large number of random points `n`
leads to better accuracy.

## Features

* Interactive CLI: Choose to either eatimate π, compare previous results, ot quit.
* Input validation: Ensure the number of points `n` is at least 1000 and a multiple of 10.
* Parallel computation: Split work across 10 CPU cores for faster execution.
* Results storage: Keeps track of all your estimations.
* Comparison tool:
  * Displayes a boxplot of estimated π values.
  * Calculates mean estimated π and persemtage error relative to `math.pi`.
  * Provides quick analysis on your `n` sufficiency.

## Project Structure
```bash
.
├── Initialization.py   # Main entry point; handles user interaction and workflow
├── Estimation.py       # Contains logic for Monte Carlo π estimation
├── Comparison.py       # Handles statistical analysis and visualization of results
└── README.md           # Project documentation (this file)
```

## Usage
1. Run the program:  
```bash
python Initialization.py
```
2. Follow the prompts:
  1. Estimate π - enter number of points `n` and get an estimation.
  2. Compare π values - vies statistics and boxplot of your previous estimations.
  3. Quit - exit the program.

## Dependencies
* Python 3.11
* matplotlib (for ploting)
* multiprocessing (biult-in)
* statistics (built-in)
* math (built-in)

Install dependencies:
```bash
pip install matplotlib
```

## Known Limitations
* The number of CPU cores is fixed on 10 and may not match the actual number of cores on your machine.
* Estimations are stored during the curent seccion only.
* The program must be run interactively.
* The results will vary even with the same input since the points are chosen randomly.
