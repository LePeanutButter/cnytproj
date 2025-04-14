# Complex Numbers
Complex numbers are an extension of real numbers and are represented in the form 𝑎+𝑏𝑖, where 𝑎 and 𝑏 are real numbers and 𝑖 is the imaginary unit that satisfies the equation 𝑖²=−1. These numbers are fundamental in quantum computing.

## Contents of the "Complex Numbers" Folder
1. **Libcplx.py**: 
This file contains a Python library with eight essential operations for working with complex numbers:
* Addition: Performs the addition of two complex numbers.
* Subtraction: Calculates the difference between two complex numbers.
* Multiplication: Multiplies two complex numbers.
* Division: Divides one complex number by another.
* Modulus: Calculates the magnitude or modulus of a complex number.
* Conjugate: Determines the conjugate of a complex number.
* Polar and Cartesian Conversion: Allows conversion between the polar and Cartesian forms of a complex number.
* Phase: Calculates the phase angle of a complex number.

2. **Testlibcpx.py**:
This file provides unit tests to verify the correct functionality of the functions implemented in Libcplx.py. The tests ensure that operations with complex numbers are performed accurately and reliably.

### Instructions
To run the Python files provided in this repository, follow these steps:  
Ensure that the Libcplx.py and Testlibcpx.py files are in the same directory so the script can find all necessary resources.  
Open a terminal or command line and navigate to the folder where the files are located.  
Then, run the Testlibcplx.py file.

# Jupyter Weekly Assignments
This folder contains the weekly workshops corresponding to the subject CNYT (Natural Sciences and Technology). The purpose of these workshops is to provide practice to improve the handling of key tools and concepts in the field of quantum computing.

## Contents of the "Jupyter Weekly Assignments" Folder
1. **ComplexIntro.ipynb**  
Purpose: Practice basic functions and operations with complex numbers. This file includes exercises to operate and plot complex numbers in the complex plane.

2. **Complex_Vector_Matrix_Operations_with_NumPy.ipynb**  
Purpose: Perform operations on matrices and column vectors using the NumPy library. Includes exercises for manipulating and calculating matrices and vectors.

3. **TallerEsp.Vect-ProdInterno-VectoPropios**  
Purpose: Calculate inner products, eigenvalues, and eigenvectors of matrices.

4. **TallerEsp.Vect-Hermitian-Unitary-Tensor-Circuits**  
Purpose: Apply the above concepts to quantum systems. Includes exercises on Hermitian matrices, unitary operations, and circuits.

### Instructions
1. Environment Setup: Make sure you have a Python 3.12.0 virtual environment configured.  
Activate the virtual environment:  
- On Windows:
```
.venv\Scripts\activate
```
- On macOS and Linux:
```
source .venv/bin/activate
```

2. Install Dependencies: Once the virtual environment is activated, install the necessary dependencies using the following command:
```
pip install numpy matplotlib ipywidgets
```

# Classic To Quantum
Classical discrete systems are characterized by having a finite number of possible states, allowing the use of statistical tools to predict outcomes. In contrast, the double-slit experiment reveals the probabilistic nature of particles.

## Contents of the "Classic To Quantum" Folder
**TallerClasicToQuantum.ipynb**  
Purpose: Implement discrete systems in a probabilistic double-slit problem and calculate the probabilities of each state.

### Instructions
1. Environment Setup: Make sure you have a Python 3.12.0 virtual environment configured.  
Activate the virtual environment:  
- On Windows:
```
.venv\Scripts\activate
```
- On macOS and Linux:
```
source .venv/bin/activate
```

2. Install Dependencies: Once the virtual environment is activated, install the necessary dependencies using the following command:
```
pip install numpy matplotlib
```

# Basic Quantum Theory, Observables and Measurements
Observables are physical quantities that can be measured due to their probabilistic nature, definition of states, and interaction with the environment.

## Contents of the "Basic Quantum Theory, Observables and Measurements" Folder
**Quantum.ipynb**  
Purpose: Implement concepts from quantum theory focusing on the calculation of observables and the analysis of the impact of measurements on quantum states.

### Exercise 4.5.2
Write down the generic state vector for the system of two particles with spin. Generalize it to a system with n particles (this is important: it will be the physical realization for quantum registers!).

The basic states of a particle with spin are:
- $$\ | \uparrow \rangle \$$
- $$\ | \downarrow \rangle \$$

Assembling a quantum system of two particles results in the tensor product between each state:
- $$\ | \uparrow \rangle \otimes | \uparrow \rangle \$$
- $$\ | \uparrow \rangle \otimes | \downarrow \rangle \$$
- $$\ | \downarrow \rangle \otimes | \uparrow \rangle \$$
- $$\ | \downarrow \rangle \otimes | \downarrow \rangle \$$

These states can be expressed as a linear combination with their coefficients:

$$\| \Psi \rangle = a_{11} | \uparrow \uparrow \rangle + a_{12} | \uparrow \downarrow \rangle + a_{21} | \downarrow \uparrow \rangle + a_{22} | \downarrow \downarrow \rangle\$$

Analyzing this equation, it can be inferred that it fits the form $$\ 2^n \$$, where $$\ n \$$ is the number of particles in the system.

### Exercise 4.5.3
Assume the same scenario as in Example 4.5.2 and let  
$$\| \Phi \rangle = |x_{0} \rangle \otimes |y_{1} \rangle + |x_1 \rangle \otimes |y_1 \rangle\$$  
Is this state separable?

A state is separable if it can be written in the form:  
$$\| \phi\rangle = |A\rangle \otimes |B\rangle \$$

The tensor product respects addition in $$\ \mathbb{V} \$$ and in $$\ \mathbb{V}' \$$, which means the formula can be expressed as:  
$$\ |\phi\rangle = |y_1\rangle \otimes (|x_0\rangle + |x_1\rangle) \$$

This means that this state is separable in a non-trivial system of two particles.

### Instructions
1. Environment Setup: Make sure you have a Python 3.12.0 virtual environment configured.  
Activate the virtual environment:  
- On Windows:
```
.venv\Scripts\activate
```
- On macOS and Linux:
```
source .venv/bin/activate
```

2. Install Dependencies: Once the virtual environment is activated, install the necessary dependencies using the following command:
```
pip install numpy matplotlib
```

# Authors
**Santiago Botero** - [LePeanutButter](https://github.com/LePeanutButter)
