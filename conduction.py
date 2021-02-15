# Import libraries
import numpy as np
import matplotlib.pyplot as plt

# Parameters
# Constants - water
rho_w = 1 		# water density [kg/m^3]
c_w = 1 		#specific heat [J/KgK]
h_w = 1			#heat transfer convection coefficient [W/m^2K]
flow_rate = 1	#flow rate water [m^3/s]
T_start_w = 1 		# [K]

# Constants - cilinder
e_cli = 1					  # [W/m^3]
r_in_cill = 1 				  # [m]
r_out_cil = 2 				  # [m]
height_cil = 1 				  # [m]
rho_cil = 1					  # [kg/m^3]
c_cil = 1					  # [J/KgK]
k_cil = 1					  # [W/mK]
epsilon_cil = 1				  # [1]
sigma = 5.6697 * ( 10  ** - 8) # Stefan-Boltzman constant [W/m^2*K^4]
T_start_cil = 1				  # [K]

# Constants - air
h_air = 1 # heat transfer convection coefficient [W/m^2*K]
T_start_air = 1 			  # [K]

# Simulation parameters
M = 10 						  # nodes on radial direction
N = 20 						  # nodes on axial direction
it_max = 10
error_max = 10 ** - 4		  # [K]
delta_t = 1 				  # [s]
t_total = 10 * 3600			  # [s]


#Processing
it_total = int(np.rint(((t_total) / delta_t))) + 1
# Creating matrix
T_matrix = np.full((N,M),T_start_cil)
T_matrix_time = []

# assigning initial values
T_matrix[:, 0] = T_start_w
time_vector = np.linspace(0, t_total, it_total)

# iterating over time
for t in time_vector:
	it = 0 # iteration
	error = 10000
	while it < it_max and error > error_max: # Gauss-Seidel
		# Equation 1 - water in
		T_matrix[0,0] = 1
		# Equation 2 - water out
		T_matrix[N-1,0] = 2
		# Equation 4 - water-cilinder top
		T_matrix[0,1] = 4
		# Equation 5 - cilinder-air bottom
		T_matrix[N-1, 1] = 5 
		# Equation 10 - cilinder-air top
		T_matrix[0,M-1] = 10
		# Equation 11 - water-cilinder bottom
		T_matrix[N-1, M-1] = 11
		for row in range(1, N-1): 				# axial nodes
			for column in range(2,M-1):		# radial nodes
					# Equation 7 - cinlinder-insulating  top 
					T_matrix[0, column] = 7
					# Equation 8 - cilinder0insulatiog bottom 
					T_matrix[(N-1), column] = 8
					# Equation 3 - water middle (column=0)
					T_matrix[row,0] = 3
					# Equation 6 - water-cilinder middle
					T_matrix[row,0] = 6
					# Equation 9 - cilinder0insulatiog middle
					T_matrix[row, column] = 9
					# Equation 12 - cilinder-air middle
					T_matrix[row,(M-1)] = 12
					# it +=1
		errorr = 0.00000001		
		it += 1
		





# Results
