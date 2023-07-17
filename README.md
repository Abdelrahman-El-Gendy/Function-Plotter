# Function Plotter

This is a Python GUI program that plots an arbitrary user-entered function.

## Requirements

* Python 3.6+
* Pyside2
* Matplotlib

## Usage

1. Save the code as a Python file.
2. Run the code from the command line.
3. Enter a function and the min and max values of x in the GUI.
4. Click the "Plot" button.

## Examples

Working example:

```python
function = "5*x^3 + 2*x"
min_x = -10
max_x = 10

fig = plot_function(function, min_x, max_x)
plt.show()

```
## Wrong Example

```python
function = "5*x^3 + 2*s"
min_x = -10
max_x = 10

fig = plot_function(function, min_x, max_x)
plt.show()

```
This will raise a SyntaxError exception because the variable `s` is not defined.

