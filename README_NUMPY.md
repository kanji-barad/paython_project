Numpy Notes


Chapter 1: Introduction to NumPy

Q1. What is NumPy? Explain its purpose in Python. (⭐⭐⭐)
Definition:NumPy is a Python library used for numerical calculations.
Purpose:
* Works with numbers, arrays, and matrices
* Used in data science, AI, ML, and scientific work
Example:Used to store marks of students and calculate average quickly.

Q2. Why is NumPy faster than Python lists? (⭐⭐⭐)
Reason:
* Written in C language
* Uses vectorized operations
* Stores data in continuous memory
Example:Adding 1 to 1 million numbers is faster in NumPy than list.

Q3. Define ndarray in NumPy. (⭐⭐⭐)
Definition:ndarray means n-dimensional array.
Points:
* Can be 1D, 2D, 3D
* Stores same type of data
Example:

import numpy as np
arr = np.array([1,2,3])

Q4. List important features of NumPy. (⭐⭐)
* Fast performance
* Multidimensional arrays
* Mathematical functions
* Less memory usage
* Vectorization

Q5. Explain vectorization in NumPy. (⭐⭐⭐)
Definition:Doing operations on entire array at once.
Example:

arr = np.array([1,2,3])
print(arr * 2)
Output:

[2 4 6]
No loop needed.

Q6. What is mean by homogeneous data in NumPy arrays? (⭐⭐)
Meaning:All elements are of same data type.
Example:[1, 2, 3] → all integers[1, "a"] → not allowed

Q7. Explain interoperability of NumPy with other libraries. (⭐)
Meaning:NumPy works easily with:
* Pandas
* Matplotlib
* TensorFlow
Used together in data science.

Chapter 2: NumPy Arrays vs Python Lists

Q1. Compare NumPy arrays and Python lists. (⭐⭐⭐)
NumPy Array	Python List
Faster	Slower
Same data type	Different types
Less memory	More memory
Vectorized	Loop needed
Q2. Why NumPy arrays use less memory? (⭐⭐)
* Fixed data type
* No extra object storage

Q3. Explain contiguous memory allocation. (⭐⭐)
Meaning:Data stored one after another in memory.
Benefit:Fast access and speed.

Q4. Why vectorized operations are faster? (⭐⭐⭐)
* No Python loop
* Uses C-level speed



Chapter 3: Creating NumPy Arrays

Q1. How do you create NumPy arrays from Python lists? (⭐⭐⭐)

import numpy as np
arr = np.array([1,2,3])
print(arr)

Q2. Create a 1D NumPy array. (⭐⭐)

arr = np.array([10,20,30])

Q3. Create a 2D NumPy array. (⭐⭐⭐)

arr = np.array([[1,2],[3,4]])

Q4. What happens if different data types are used? (⭐⭐)
NumPy converts all to one common type.

Q5. Explain built-in array creation functions. (⭐⭐)

np.zeros((2,2))    # all 0
np.ones((2,2))     # all 1
np.full((2,2),5)   # all 5
np.eye(3)          # identity matrix

Q6. Difference between np.arange() and np.linspace(). (⭐⭐⭐)
arange	linspace
Step based	Count based
May skip end	Includes end
Chapter 4: Array Properties

Q1. Explain shape attribute. (⭐⭐⭐)
Definition:Shows rows and columns.

arr.shape

Q2. What does size represent? (⭐⭐⭐)
Total number of elements.

Q3. Define ndim. (⭐⭐)
Number of dimensions.

Q4. What is dtype? (⭐⭐⭐)
Shows data type of array.

Q5. Explain itemsize. (⭐⭐)
Size of each element in bytes.

Q6. Why arrays are homogeneous? (⭐⭐)
For speed and memory efficiency.

Chapter 5: Data Types

Q1. What is dtype in NumPy? (⭐⭐⭐)
Defines type of data stored.

Q2. List common NumPy data types. (⭐⭐)
* int
* float
* bool
* complex
* string

Q3. Difference between int32 and int64. (⭐⭐)
int32	int64
4 bytes	8 bytes
Less memory	More memory
Q4. Unicode vs byte strings. (⭐⭐)
Unicode (U)	Byte (S)
Any language	English only
Q5. How to change dtype using astype()? (⭐⭐⭐)

arr = arr.astype(float)

Q6. Why dtype matters? (⭐⭐⭐)
* Memory saving
* Faster speed
* Compatibility

Q7. Explain downcasting. (⭐⭐⭐)
Meaning:Converting large type → smaller type.
Example:Age stored as int8 instead of int64.

Chapter 6: Array Operations

Q1. What is reshaping? (⭐⭐⭐)
Changing array shape without changing data.

Q2. Convert 1D to 2D. (⭐⭐⭐)

arr.reshape(2,3)

Q3. Difference between reshape and flatten. (⭐⭐⭐)
reshape	flatten
Change shape	Convert to 1D
Q4. Explain indexing. (⭐⭐⭐)
Access elements using index.

Q5. What is fancy indexing? (⭐⭐⭐)
Using list of indexes.

Q6. What is boolean indexing? (⭐⭐⭐)
Using conditions.

Chapter 7: Slicing & Copy vs View

Q1. Explain slicing. (⭐⭐⭐)
Extract part of array.

Q2. Difference between list slicing and array slicing. (⭐⭐⭐)
List	NumPy
Copy	View
Q3. What is view? (⭐⭐⭐)
Shares same data.

Q4. What is copy? (⭐⭐⭐)
New data created.

Q5. How to create copy? (⭐⭐)

arr.copy()

Q6. Why NumPy uses view? (⭐⭐)
For speed and memory.

Chapter 8: Multi-Dimensional Arrays

Q1. Define multi-dimensional arrays. (⭐⭐⭐)
Arrays with more than one dimension.

Q2. Explain axes. (⭐⭐⭐)
* axis 0 → rows
* axis 1 → columns

Q3. 2D vs 3D arrays. (⭐⭐)
2D	3D
Rows & columns	Layers + rows + columns
Q4. Grayscale image storage. (⭐⭐⭐)
2D array.

Q5. RGB image storage. (⭐⭐⭐)
3D array (height, width, color).

Q6. Practical use. (⭐⭐)
Images, ML data, sensors.

Chapter 9: Operations Along Axes

Q1. What is axis? (⭐⭐⭐)
Direction of operation.

Q2. axis=0 vs axis=1. (⭐⭐⭐)
axis=0	axis=1
Column wise	Row wise
Q3. Row-wise sum. (⭐⭐)

np.sum(arr, axis=1)

Q4. Column-wise sum. (⭐⭐)

np.sum(arr, axis=0)

Q5. Slicing 2D array. (⭐⭐)

arr[0:2, 1:3]

Q6. Modify 3D array. (⭐⭐⭐)

arr3D[:,0,:] = 99

Chapter 10: Vectorization & Broadcasting

Q1. What is vectorization? (⭐⭐⭐)
Array operation without loop.

Q2. Why faster than loops? (⭐⭐⭐)
Uses C-level execution.

Q3. What is broadcasting? (⭐⭐⭐)
Automatic size matching.

Q4. Broadcasting rules. (⭐⭐⭐)
* Same size
* Size 1
* Missing dimension

Q5. When broadcasting fails? (⭐⭐)
Incompatible shapes.

Q6. Vectorization vs Broadcasting. (⭐⭐)
Vectorization	Broadcasting
Operation	Shape matching
Q7. Scalar broadcasting. (⭐⭐)

arr * 10

Q8. Vector broadcasting. (⭐⭐)

arr1D + arr2D

Chapter 11: Normalization

Q1. What is normalization? (⭐⭐⭐)
Scaling data to same range.

Q2. Formula. (⭐⭐⭐)
(x − mean) / std

Q3. Why important in ML? (⭐⭐⭐)
Improves model performance.

Q4. Row vs Column normalization. (⭐⭐)
Row	Column
axis=1	axis=0
Q5. Column normalization code. (⭐⭐)

(arr - mean) / std

Chapter 12: Aggregation Functions

Q1. What are aggregation functions? (⭐⭐⭐)
Reduce array to single value.

Functions Explanation (⭐⭐ / ⭐⭐⭐)
* sum → total
* prod → multiplication
* min / max → smallest / largest
* argmin / argmax → index
* mean → average
* median → middle
* std → spread
* var → variance

Chapter 13: Mathematical & Utility Functions

Q1. square vs pow. (⭐⭐)
square	pow
x²	xⁿ
Q2. Square root. (⭐⭐)

np.sqrt(arr)

Q3. log functions difference. (⭐⭐⭐)
log	log10	log2
ln	base10	base2
Q4. exp function. (⭐⭐)
Returns eˣ.

Q5. Rounding functions. (⭐⭐⭐)
round	ceil	floor	trunc
nearest	up	down	remove decimal
Q6. abs function. (⭐⭐)
Returns positive value.

Q7. sort vs unique. (⭐⭐⭐)
sort	unique
Arrange	Remove duplicates
