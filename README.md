# Mobius Strip Generator and Analyzer

A Python implementation for generating, visualizing, and analyzing the mathematical properties of a Möbius strip - a fascinating topological surface with only one side and one boundary.

## 🌟 Features

- **3D Surface Generation**: Creates parametric equations for a Möbius strip
- **Surface Area Calculation**: Computes the total surface area using triangular patches
- **Edge Length Computation**: Calculates the length of the single boundary edge
- **Interactive 3D Visualization**: Renders the strip using matplotlib with customizable viewing
- **Configurable Parameters**: Adjustable radius, width, and resolution

## 🔧 Requirements

```bash
pip install numpy matplotlib
```

## 🚀 Usage

### Command Line Interface

```bash
python mobius_strip.py <R> <w> <n>
```

**Parameters:**
- `R`: Major radius of the strip (distance from center to middle of the strip)
- `w`: Width of the strip
- `n`: Number of grid points for resolution (higher = more detailed)

**Example:**
```bash
python mobius_strip.py 3.0 1.0 50
```

### Python Import

```python
from mobius_strip import MobiusStrip

# Create a Möbius strip
strip = MobiusStrip(R=3.0, w=1.0, n=50)

# Calculate properties
surface_area = strip.compute_surface_area()
edge_length = strip.compute_edge_length()

# Visualize
strip.plot()

print(f"Surface Area: {surface_area:.2f}")
print(f"Edge Length: {edge_length:.2f}")
```

## 📊 Output

The program provides:
1. **Surface Area**: Total area of the one-sided surface
2. **Edge Length**: Length of the single continuous boundary
3. **3D Visualization**: Interactive plot showing the strip's unique topology

## 🧮 Mathematical Background

The Möbius strip is parameterized using:
- **x(u,v) = (R + v·cos(u/2))·cos(u)**
- **y(u,v) = (R + v·cos(u/2))·sin(u)**
- **z(u,v) = v·sin(u/2)**

Where:
- `u ∈ [0, 2π]` (angle parameter)
- `v ∈ [-w/2, w/2]` (width parameter)
- The `u/2` term creates the characteristic half-twist

## 🎯 Key Properties

- **One-sided surface**: No distinct "inside" or "outside"
- **Single boundary**: One continuous edge
- **Non-orientable**: Cannot define consistent "left" and "right"
- **Genus 0**: Topologically equivalent to a disk with a twist

## 📈 Accuracy Notes

- Surface area is approximated using triangular mesh patches
- Higher `n` values provide more accurate calculations but slower performance
- Edge length computation follows the boundary at v = w/2

## 🔬 Applications

- Topology and differential geometry education
- Mathematical visualization
- Surface analysis and mesh generation studies
- Understanding non-orientable surfaces

## 📝 License

Open source - feel free to modify and extend!

## 🤝 Contributing

Contributions welcome! Areas for improvement:
- More accurate surface area calculation methods
- Additional topological property calculations
- Enhanced visualization options
- Performance optimizations
