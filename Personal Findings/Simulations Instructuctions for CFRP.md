Perform structural simulations on a Carbon Fiber Reinforced Polymer (CFRP) rectangular specimen with the following specifications:

Geometry:
- Length: 100 mm
- Width: 50 mm
- Thickness: 0.5 mm

Material:
- Orthotropic CFRP material
- Define longitudinal (E1), transverse (E2), in-plane shear modulus (G12), Poisson’s ratio (ν12)
- Include density if required for solver stability

Assume unidirectional fiber orientation along the 100 mm length (0° direction).
Use appropriate 3D solid or layered shell elements.
Enable nonlinear analysis if failure modeling is included.

Run the following simulations:

1. Tensile Test
- Apply uniaxial displacement-controlled loading along longitudinal direction (100 mm side).
- Fix opposite edge completely.
- Extract stress–strain curve.
- Report longitudinal tensile strength, transverse tensile response, and maximum deformation.
- Apply suitable failure criteria (Maximum Stress and Tsai-Wu).

2. Compressive Test
- Apply compressive displacement along longitudinal direction.
- Constrain lateral rigid body motion.
- Include geometric nonlinearity to capture buckling.
- Extract compressive strength and buckling load factor.

3. Flexural Test (Three-Point Bending)
- Support specimen at two ends (simply supported).
- Apply central downward load.
- Use appropriate contact definitions if needed.
- Extract flexural strength, flexural modulus, and maximum mid-span deflection.

4. Shear Test (In-Plane Shear)
- Fix bottom edge.
- Apply horizontal displacement on top edge.
- Extract shear stress–strain response.
- Compute in-plane shear strength and modulus (G12).

Mesh:
- Use refined mesh through thickness (minimum 3–5 elements if using solid elements).
- Perform mesh convergence study.

Outputs Required:
- Stress distribution plots
- Strain distribution plots
- Load vs displacement curves
- Stress vs strain curves
- Failure index contour plots
- Summary table of mechanical properties

Ensure units are consistent (MPa, mm, N).
