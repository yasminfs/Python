# Import libraries
import numpy as np
import matplotlib.pyplot as plt

# Parameters
# Constants - water
rho_w = 1.0 		# water density [kg/m^3]
c_w = 1.0		#specific heat [J/KgK]
h_w = 1.0			#heat transfer convection coefficient [W/m^2K]
flow_rate = 1.0	#flow rate water [m^3/s]
T_start_w = 30 		# [K]

# Constants - cilinder
e_cil = 1.0					  # [W/m^3]
r_in_cil = 1.0 				  # [m]
r_out_cil = 2.0 				  # [m]
height_cil = 1.0 				  # [m]
rho_cil = 1.0					  # [kg/m^3]
c_cil = 1.0					  # [J/KgK]
k_cil = 1.0					  # [W/mK]
epsilon_cil = 1.0				  # [1]
sigma = 5.6697 * ( 10  ** - 8) # Stefan-Boltzman constant [W/m^2*K^4]
T_start_cil = 1.0				  # [K]

# Constants - air
h_air = 1.0 # heat transfer convection coefficient [W/m^2*K]
T_start_air = 1.0			  # [K]

# Simulation parameters
M = 10 						  # nodes on radial direction
N = 20 						  # nodes on axial direction
it_max = 10
error_max = 10 ** - 4		  # [K]
delta_t = 1.0 				  # [s]
t_total = 10 * 3600			  # [s]


#Processing
it_total = int(np.rint(((t_total) / delta_t))) + 1
# Creating matrix
T_matrix = np.full((N,M),T_start_cil, dtype=float)
T_matrix_time = []

# assigning initial values
T_matrix[:, 0] = T_start_w
time_vector = np.linspace(0, t_total, it_total)
# creating radii vector
radii_vec = np.zeros(M)
radii_vec[1:] = np.linspace(r_in_cil, r_out_cil, M-1)
#creating height vector
delta_z = height_cil / N
height_vec = np.full(N, delta_z)
height_vec[0] = delta_z / 2 
height_vec[-1] = delta_z / 2

# equations

def water_in(T_s, T_before): # 1
	conv = h_w * 2 * np.pi * r_in_cil * (delta_z / 2 ) 
	advc = rho_w * c_w * (flow_rate / 2) 
	sens = (rho_w * c_w * np.pi * r_in_cil ** 2 * (delta_z / 2)) / delta_t 
	T_w_in = (conv * T_s + advc * T_start_w + sens * T_before) / \
		(conv + advc + sens)	
	return T_w_in

def water_out(T_s, T_above, T_before): # 2
	conv = h_w * 2 * np.pi * r_in_cil * (delta_z / 2 ) 
	advc = rho_w * c_w * (flow_rate / 2) 
	sens = (rho_w * c_w * np.pi * r_in_cil ** 2 * (delta_z / 2)) / delta_t 
	T_w_out = (conv * T_s + advc * T_above + sens * T_before) / \
		(conv + advc + sens)
	return T_w_out	

def water_middle(T_s, T_above, T_before): # 3
	conv = h_w * 2 * np.pi * r_in_cil * (delta_z ) 
	advc = rho_w * c_w * (flow_rate) 
	sens = (rho_w * c_w * np.pi * r_in_cil ** 2 * (delta_z)) / delta_t 
	T_w_middle = (conv * T_s + advc * T_above + sens * T_before) / \
		(conv + advc + sens)
	return T_w_middle

def water_cylinder_top(T_w, T_below, T_right, T_before):
	conv = h_w * 2 * np.pi * r_in_cil * (delta_z / 2)
	cond_r = (2 * np.pi * (delta_z / 2) * k_cil) / \
		np.log(radii_vec[2] / radii_vec[1])
	cond_a = k_cil * np.pi * (radii_vec[2] ** 2 - radii_vec[1] ** 2) \
		/ delta_z
	delta_v = np.pi * (radii_vec[2] ** 2 - radii_vec[1] ** 2) * (delta_z / 2)
	sens = (rho_cil * c_cil * delta_v) / delta_t
	ger = e_cil * delta_v
	T_w_cyl_top = (conv * T_w + cond_r * T_right + cond_a * T_below + ger + \
		sens * T_before) / (conv  + cond_r  + cond_a  + ger + sens)
	return T_w_cyl_top

def water_cylinder_botton(T_w, T_above, T_right, T_before):
	conv = h_w * 2 * np.pi * r_in_cil * (delta_z / 2)
	cond_r = (2 * np.pi * (delta_z / 2) * k_cil) / \
		np.log(radii_vec[2] / radii_vec[1])
	cond_a = k_cil * np.pi * (radii_vec[2] ** 2 - radii_vec[1] ** 2) \
		/ delta_z
	delta_v = np.pi * (radii_vec[2] ** 2 - radii_vec[1] ** 2) * (delta_z / 2)
	sens = (rho_cil * c_cil * delta_v) / delta_t
	ger = e_cil * delta_v
	T_w_cyl_top = (conv * T_w + cond_r * T_right + cond_a * T_above + ger + \
		sens * T_before) / (conv  + cond_r  + cond_a  + ger + sens)
	return T_w_cyl_top

def water_cylinder_middle(T_w, T_above, T_below, T_right, T_before):
	conv = h_w * 2 * np.pi * r_in_cil * delta_z 
	cond_r = (2 * np.pi * delta_z  * k_cil) / \
		np.log(radii_vec[2] / radii_vec[1])
	cond_a = k_cil * np.pi * (radii_vec[2] ** 2 - radii_vec[1] ** 2) \
		/ delta_z
	delta_v = np.pi * (radii_vec[2] ** 2 - radii_vec[1] ** 2) * delta_z
	sens = (rho_cil * c_cil * delta_v) / delta_t
	ger = e_cil * delta_v
	T_w_cyl_middle = (conv * T_w + cond_r * T_right + cond_a * T_above + cond_a * \
		T_below + ger + \
		sens * T_before) / (conv  + cond_r  + 2 * cond_a + sens)
	return T_w_cyl_middle


# iterating over time
for t in time_vector:
	it = 0 # iteration
	error = 10000
	T_matrix_before = T_matrix.copy()
	while it < it_max and error > error_max: # Gauss-Seidel
		# Equation 1 - water in
		T_matrix[0,0] = water_in(T_matrix[0, 1], T_matrix_before[0, 0])
		# Equation 2 - water out
		T_matrix[N-1,0] = water_out(T_matrix[N-1, 1],
									T_matrix[N-2, 0],
									T_matrix[N-1, 0] )
		# Equation 4 - water-cylinder top
		T_matrix[0, 1] = water_cylinder_top(T_matrix[0, 0], 
											T_matrix[1,1],
											T_matrix[0, 2], 
											T_matrix_before[0, 1])
		# Equation 5 - cylinder-air bottom
		T_matrix[N-1, 1] = water_cylinder_botton(T_matrix[N-1, 0], 
											T_matrix[N-2,1],
											T_matrix[N-1, 2], 
											T_matrix_before[N-1, 1]) 
		# Equation 10 - cylinder-air top
		T_matrix[0,M-1] = 10
		# Equation 11 - water-cylinder bottom
		T_matrix[N-1, M-1] = 11
		for row in range(1, N-1): 				# axial nodes
			for column in range(2,M-1):		# radial nodes
					# Equation 7 - cynlinder-insulating  top 
					T_matrix[0, column] = 7
					# Equation 8 - cylinder0insulatiog bottom 
					T_matrix[(N-1), column] = 8
					# Equation 3 - water middle (column=0)
					T_matrix[row,0] = water_middle(T_matrix[row, 1],
									T_matrix[row - 1, 0],
									T_matrix_before[row, 0])
					# Equation 6 - water-cylinder middle
					T_matrix[row, 1] = water_cylinder_middle(T_matrix[row, 0],
															T_matrix[row - 1, 1], 
															T_matrix[row  + 1, 1],
															T_matrix[row, 2],
															T_matrix_before[row, 1])
					# Equation 9 - cylinder0insulatiog middle
					T_matrix[row, column] = 9
					# Equation 12 - cylinder-air middle
					T_matrix[row,(M-1)] = 12
					# it +=1
		errorr = 0.00000001		
		it += 1
		T_matrix_before = T_matrix





# Results
