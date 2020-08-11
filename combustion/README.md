# Combustion of natural gas

Simulation of combustion of natural gas in with air.

Natural gas consist of 80% methane, 10% ethane, 5% propane and 5% butane.

Assuming air consists of 21% O2 and 79% N2. Air is added in 20% excess O2.


The reactions are given below. Assuming complete combustion.

![Image of chemical equations](chemical_equations_combustion.png)


A flow chart of the process is presented below.
![Image of flow chart](flow_chart_combustion.png)

Mole balances of methane (C1), ethane (C2), propane (C3), butane (C4), CO2, H2O, O2 and N2 are given below, where <img src="https://render.githubusercontent.com/render/math?math=\zeta_i"> is the reaction extent of reaction *i*.

![Image of mole balances](mole_balances_combustion.png)

This can be formulated in vector notation, and this is the equation used in the python-code.

![Image of vector notation](vector_notation_combustion.png)
