# Hold tank

"Hold tank" is a dynamic simulation problem.

The system is a perfectly mixed hold tank with an inflow and outflow (CSTR). It is installed in an aqueous effluent-treatment process to floctuations in concentration of the effluent stream. Normally the effluent stream containts maximum 100 ppm acetone, and the maximum allowable concentration of acetone in the effluent discharge is 200 ppm. 

Due to a spill in the process plant, the acetone concentration in the feed suddenly rises to 1000 ppm for 30 min. Will the acetone concentration in the effluent stream exceed 200 ppm?

The tank has a constant volume of 500 m3. The feed stream and effulent stream are at constant volume flow 45 m3/h.

![Image of flow chart](hold-tank-flow-chart.png)

Mole balance of acetone:
<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{dt}(V\cdot c) = q_{in} c_{in} - q c">,
where *V* is the volume of the tank, *c* is the concentration in the effulent stream and in the tank, <img src="https://render.githubusercontent.com/render/math?math=\ c_{in}"> is the feed concentration, *q* is the volume flow of the effulent stream and <img src="https://render.githubusercontent.com/render/math?math=\ q_{in} "> is the volume flow of the feed stream.

Assuming constant volume V and equal volume flows in and out of the tank <img src="https://render.githubusercontent.com/render/math?math=\ q_{in} = q ">, the mole balance simplifies to:

<img src="https://render.githubusercontent.com/render/math?math=\V\frac{dc}{dt} = q_{in}(c_{in} - c)">

Introducing residence time: <img src="https://render.githubusercontent.com/render/math?math=\tau=\frac{V}{q_{in}}"> simplifies the mole balance:

<img src="https://render.githubusercontent.com/render/math?math=\tau\frac{dc}{dt} = c_{in} - c">.

This is a differential equation we can solve. However, we have concentrations given in *ppm*, so the mole balance must be converted from concentration *c* to mole fraction *x*:

<img src="https://render.githubusercontent.com/render/math?math=c = c_T \cdot x">, where <img src="https://render.githubusercontent.com/render/math?math=c_T"> is the total concentration in the tank. 

This gives: <img src="https://render.githubusercontent.com/render/math?math=\tau\frac{d}{dt}(c_T \cdot x) = c_T x_{in} - c_T x">, which can be simplified to

<img src="https://render.githubusercontent.com/render/math?math=\tau\frac{dx}{dt} = x_{in} - x">. This is an ordinary differential equation which can be solved using the initial condition <img src="https://render.githubusercontent.com/render/math?math=x(t=0)=100 ppm"> and inlet mole fraction <img src="https://render.githubusercontent.com/render/math?math=x_{in}= 1000 ppm">


Using odeint from scipy.integrate, we get that when t = 0.5 hour, x = 139.6 ppm, which is is below the maximum allowable concentration. 



