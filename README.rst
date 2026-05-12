=====
Forked from NIST electrode package https://github.com/nist-ionstorage/electrode. Simplified to be used only to compute polygon potentials.
For potential optimisation, see pytrans https://github.com/tiqi-group/pytrans. 

Original author: Robert Jordens <jordens@phys.ethz.ch>

Description
===========

Electrode is a toolkit to develop and analyze RF ion traps. It can
optimize 2D surface electrode patterns to achieve desired trapping
properties and extract relevant parameters of the resulting geometry.
The software also treats precomputed 3D volumetric field and potential
data transparently.

Quick overview and tutorial:
http://nbviewer.ipython.org/github/nist-ionstorage/electrode/blob/master/examples/tutorial.ipynb

See also:

[1] Roman Schmied <roman.schmied@unibas.ch>, SurfacePattern software
package.
http://atom.physik.unibas.ch/people/romanschmied/code/SurfacePattern.php

[2] Roman Schmied: Electrostatics of gapped and finite surface
electrodes. New Journal of Physics 12:023038 (2010).
http://dx.doi.org/10.1088/1367-2630/12/2/023038

[3] Roman Schmied, Janus H. Wesenberg, and Dietrich Leibfried: Optimal
Surface-Electrode Trap Lattices for Quantum Simulation with Trapped
Ions. Physical Review Letters 102:233002 (2009).
http://dx.doi.org/10.1103/PhysRevLett.102.233002

[4] A. van Oosterom and J. Strackee: The Solid Angle of a Plane
Triangle, IEEE Transactions on Biomedical Engineering, vol. BME-30, no.
2, pp. 125-126. (1983)
http://dx.doi.org/10.1109/TBME.1983.325207

[5] Mário H. Oliveira and José A. Miranda: Biot–Savart-like law in
electrostatics. European Journal of Physics 22:31 (2001).
http://dx.doi.org/10.1088/0143-0807/22/1/304

Recommended installation is with uv.

```
uv add "surfx @ git+https://github.com/tiqi-group/surfx.git
```
