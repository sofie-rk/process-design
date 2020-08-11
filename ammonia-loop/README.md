# Ammonia loop

This code computes flow composition in an ammonia loop. It looks at how the split flow ratio changes the inert concentration in the reactor's inlet stream.

A gas phase reaction between nitrogen (N2) and hydrogen (H2) produces NH3. The chemical reaction is: N2 + 3H2 = 2NH3.

A recycle is introduced because not all N2 and H2 are converted to NH3.

A purge is introduced because inert Ar is in the make up stream (stream 0), which will clump up in the system if not taken out through a purge.

A flow chart of the process is presented below.

![Image of flow chart](flow_chart_ammonia.jpg)

## Makeup-stream (stream 0):
N2: 240 kmol/h

H2: 750 kmol/h

NH3: 0

Ar: 10 kmol/h

## Mixer
Combines stream 0 and stream 4 to stream 1.

<img src="https://render.githubusercontent.com/render/math?math=\underline{F_1} = \underline{F_0} %2B \underline{F_4}">

## Reactor
30% of all N2 in stream 1 is converted to ammonia:

<img src="https://render.githubusercontent.com/render/math?math=X_{N2}=0.30">,

Stoichiometry matrix:

<img src="https://render.githubusercontent.com/render/math?math=\underline{\underline{N}} =\begin{bmatrix} -1 \\ -3 \\ 2 \\ 0 \end{bmatrix}">,

Conversion matrix:
<img src="https://render.githubusercontent.com/render/math?math=\underline{\underline{X}} = [X_{N2}, 0, 0, 0]">,

Mole balance reactor:

<img src="https://render.githubusercontent.com/render/math?math=\underline{F_2} = \underline{F_1} + \underline{\underline{N}}\underline{\underline{X}}\underline{F_1} = (\underline{\underline{I}} %2B \underline{\underline{N}}\underline{\underline{X}} )\underline{F_1}">.

## Separator
Assuming all Argon ends up in the gas phase and all ammonia ends up in the liquid phase.

99% of all H2 and 98% of all N2 goes to the gas phase. 

Separator factors: <img src="https://render.githubusercontent.com/render/math?math=a_k=(0.98, 0.99, 0, 1)">,

<img src="https://render.githubusercontent.com/render/math?math=\underline{\underline{A}} = diag(a_k)">,

<img src="https://render.githubusercontent.com/render/math?math=\underline{F_3} = \underline{\underline{A}} \underline{F_2}">,

<img src="https://render.githubusercontent.com/render/math?math=\underline{F_5} = (\underline{\underline{I}} - \underline{\underline{A}} ) \underline{F_2}">



## Split
5% of stream 3 goes to purge. 95% is recycled.

Split flow ratio: <img src="https://render.githubusercontent.com/render/math?math=\alpha = 0.95">.

<img src="https://render.githubusercontent.com/render/math?math=\underline{F_4} = \alpha \underline{F_3}">,


<img src="https://render.githubusercontent.com/render/math?math=\underline{F_6} = (1-\alpha) \underline{F_3}">.

## Loop

<img src="https://render.githubusercontent.com/render/math?math=\underline{F_4} = \alpha\underline{\underline{A}}  (\underline{\underline{I}} %2B \underline{\underline{N}}\underline{\underline{X}} )\cdot (\underline{F_0} %2B \underline{F_4})">,

Let <img src="https://render.githubusercontent.com/render/math?math=\underline{\underline{M}} = \alpha\underline{\underline{A}}  (\underline{\underline{I}} %2B \underline{\underline{N}}\underline{\underline{X}})">,


<img src="https://render.githubusercontent.com/render/math?math=(\underline{\underline{I}} - \underline{\underline{M}})\underline{F_4} = \underline{\underline{M}}\underline{F_0}">

By solving this equation using scipy.linalg, F4 will be known. From F4, all other flows can be calculated.


## Recycle ratio
Recycle ratio is the ratio between the the recycle stream (stream 4) and the make up stream (stream 0).

<img src="https://render.githubusercontent.com/render/math?math=\text{recycle ratio} = \frac{F_4}{F_0}">

## Split flow ratio and inert concentration
By changing the split flow ratio from 0.9 to 0.99, the inert concentration in stream 1 will increase. A plot is presented below.

![Image of inert concentration](inert_conc_alpha.png)

When no flow is let out through the purge, the inert will continue to circulate in the process as well as added through the make up stream. Thus, the inert concentration in the process increase. This is the reason why the purge is installed.











