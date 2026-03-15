#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.cm as cm

class enhanced_washing_machine:
    def __init__(self):
        # Input variables
        self.laundry_weight = ctrl.Antecedent(np.arange(0.0, 8.5, 0.5), 'laundry_weight')
        self.dirt_level = ctrl.Antecedent(np.arange(1.0, 10.5, 0.5), 'dirt_level')
        self.fabric_type = ctrl.Antecedent(np.arange(1, 5.1, 0.1), 'fabric_type')
        self.water_hardness = ctrl.Antecedent(np.arange(1, 10.1, 0.5), 'water_hardness')
        
        # Output variables
        self.powder_required = ctrl.Consequent(np.arange(0, 61, 1), 'powder_required')
        self.wash_time = ctrl.Consequent(np.arange(20, 121, 1), 'wash_time')
        self.water_temperature = ctrl.Consequent(np.arange(20, 91, 1), 'water_temperature')
        
        # Customize membership functions for laundry weight
        self.laundry_weight['very_light'] = fuzz.trimf(self.laundry_weight.universe, [0, 0, 2])
        self.laundry_weight['light'] = fuzz.trimf(self.laundry_weight.universe, [0, 2, 4])
        self.laundry_weight['medium'] = fuzz.trimf(self.laundry_weight.universe, [2, 4, 6])
        self.laundry_weight['heavy'] = fuzz.trimf(self.laundry_weight.universe, [4, 6, 8])
        self.laundry_weight['very_heavy'] = fuzz.trimf(self.laundry_weight.universe, [6, 8, 8])
        
        # Customize membership functions for dirt level
        self.dirt_level['slightly_dirty'] = fuzz.trimf(self.dirt_level.universe, [1, 1, 4])
        self.dirt_level['moderately_dirty'] = fuzz.trimf(self.dirt_level.universe, [2, 5, 8])
        self.dirt_level['very_dirty'] = fuzz.trimf(self.dirt_level.universe, [6, 10, 10])
        
        # Define membership functions for fabric type
        # 1: Delicate, 2: Wool, 3: Cotton, 4: Synthetic, 5: Heavy Duty
        self.fabric_type['delicate'] = fuzz.trimf(self.fabric_type.universe, [1, 1, 2])
        self.fabric_type['wool'] = fuzz.trimf(self.fabric_type.universe, [1.5, 2, 2.5])
        self.fabric_type['cotton'] = fuzz.trimf(self.fabric_type.universe, [2, 3, 4])
        self.fabric_type['synthetic'] = fuzz.trimf(self.fabric_type.universe, [3, 4, 5])
        self.fabric_type['heavy_duty'] = fuzz.trimf(self.fabric_type.universe, [4, 5, 5])
        
        # Define membership functions for water hardness
        self.water_hardness['soft'] = fuzz.trimf(self.water_hardness.universe, [1, 1, 4])
        self.water_hardness['medium'] = fuzz.trimf(self.water_hardness.universe, [3, 5, 7])
        self.water_hardness['hard'] = fuzz.trimf(self.water_hardness.universe, [6, 10, 10])
        
        # Define membership functions for powder required
        self.powder_required['very_low'] = fuzz.trimf(self.powder_required.universe, [0, 5, 15])
        self.powder_required['low'] = fuzz.trimf(self.powder_required.universe, [10, 20, 30])
        self.powder_required['medium'] = fuzz.trimf(self.powder_required.universe, [25, 35, 45])
        self.powder_required['high'] = fuzz.trimf(self.powder_required.universe, [40, 50, 60])
        self.powder_required['very_high'] = fuzz.trimf(self.powder_required.universe, [55, 60, 60])
        
        # Define membership functions for wash time
        self.wash_time['very_short'] = fuzz.trimf(self.wash_time.universe, [20, 20, 40])
        self.wash_time['short'] = fuzz.trimf(self.wash_time.universe, [30, 50, 70])
        self.wash_time['medium'] = fuzz.trimf(self.wash_time.universe, [60, 75, 90])
        self.wash_time['long'] = fuzz.trimf(self.wash_time.universe, [80, 100, 120])
        self.wash_time['very_long'] = fuzz.trimf(self.wash_time.universe, [100, 120, 120])
        
        # Define membership functions for water temperature
        self.water_temperature['cold'] = fuzz.trimf(self.water_temperature.universe, [20, 20, 35])
        self.water_temperature['warm'] = fuzz.trimf(self.water_temperature.universe, [30, 45, 60])
        self.water_temperature['hot'] = fuzz.trimf(self.water_temperature.universe, [50, 70, 90])
        self.water_temperature['very_hot'] = fuzz.trimf(self.water_temperature.universe, [70, 90, 90])
        
        # Define fuzzy rules for powder required
        rule1 = ctrl.Rule(self.laundry_weight['very_light'] & self.dirt_level['slightly_dirty'], self.powder_required['very_low'])
        rule2 = ctrl.Rule(self.laundry_weight['light'] & self.dirt_level['slightly_dirty'], self.powder_required['low'])
        rule3 = ctrl.Rule(self.laundry_weight['medium'] & self.dirt_level['slightly_dirty'], self.powder_required['low'])
        rule4 = ctrl.Rule(self.laundry_weight['heavy'] & self.dirt_level['slightly_dirty'], self.powder_required['medium'])
        rule5 = ctrl.Rule(self.laundry_weight['very_heavy'] & self.dirt_level['slightly_dirty'], self.powder_required['medium'])
        
        rule6 = ctrl.Rule(self.laundry_weight['very_light'] & self.dirt_level['moderately_dirty'], self.powder_required['low'])
        rule7 = ctrl.Rule(self.laundry_weight['light'] & self.dirt_level['moderately_dirty'], self.powder_required['medium'])
        rule8 = ctrl.Rule(self.laundry_weight['medium'] & self.dirt_level['moderately_dirty'], self.powder_required['medium'])
        rule9 = ctrl.Rule(self.laundry_weight['heavy'] & self.dirt_level['moderately_dirty'], self.powder_required['high'])
        rule10 = ctrl.Rule(self.laundry_weight['very_heavy'] & self.dirt_level['moderately_dirty'], self.powder_required['high'])
        
        rule11 = ctrl.Rule(self.laundry_weight['very_light'] & self.dirt_level['very_dirty'], self.powder_required['medium'])
        rule12 = ctrl.Rule(self.laundry_weight['light'] & self.dirt_level['very_dirty'], self.powder_required['high'])
        rule13 = ctrl.Rule(self.laundry_weight['medium'] & self.dirt_level['very_dirty'], self.powder_required['high'])
        rule14 = ctrl.Rule(self.laundry_weight['heavy'] & self.dirt_level['very_dirty'], self.powder_required['very_high'])
        rule15 = ctrl.Rule(self.laundry_weight['very_heavy'] & self.dirt_level['very_dirty'], self.powder_required['very_high'])
        
        # Rules considering water hardness
        rule16 = ctrl.Rule(self.water_hardness['hard'], self.powder_required['high'])
        rule17 = ctrl.Rule(self.water_hardness['soft'] & self.dirt_level['slightly_dirty'], self.powder_required['very_low'])
        rule18 = ctrl.Rule(self.water_hardness['medium'], self.powder_required['medium'])  # Added default rule for medium water hardness
        
        # Rules for fabric type affecting powder amount
        rule19 = ctrl.Rule(self.fabric_type['delicate'], self.powder_required['low'])
        rule20 = ctrl.Rule(self.fabric_type['wool'], self.powder_required['low'])
        rule21 = ctrl.Rule(self.fabric_type['heavy_duty'] & self.dirt_level['very_dirty'], self.powder_required['very_high'])
        rule22 = ctrl.Rule(self.fabric_type['cotton'], self.powder_required['medium'])  # Added default rule for cotton
        rule23 = ctrl.Rule(self.fabric_type['synthetic'], self.powder_required['medium'])  # Added default rule for synthetic
        
        # Rules for wash time
        rule24 = ctrl.Rule(self.dirt_level['slightly_dirty'] & self.laundry_weight['very_light'], self.wash_time['very_short'])
        rule25 = ctrl.Rule(self.dirt_level['slightly_dirty'] & self.laundry_weight['light'], self.wash_time['short'])  # Added
        rule26 = ctrl.Rule(self.dirt_level['slightly_dirty'] & self.laundry_weight['medium'], self.wash_time['short'])
        rule27 = ctrl.Rule(self.dirt_level['slightly_dirty'] & self.laundry_weight['heavy'], self.wash_time['medium'])  # Added
        rule28 = ctrl.Rule(self.dirt_level['slightly_dirty'] & self.laundry_weight['very_heavy'], self.wash_time['medium'])  # Added
        
        rule29 = ctrl.Rule(self.dirt_level['moderately_dirty'] & self.laundry_weight['very_light'], self.wash_time['short'])  # Added
        rule30 = ctrl.Rule(self.dirt_level['moderately_dirty'] & self.laundry_weight['light'], self.wash_time['short'])  # Added
        rule31 = ctrl.Rule(self.dirt_level['moderately_dirty'] & self.laundry_weight['medium'], self.wash_time['medium'])
        rule32 = ctrl.Rule(self.dirt_level['moderately_dirty'] & self.laundry_weight['heavy'], self.wash_time['long'])  # Added
        rule33 = ctrl.Rule(self.dirt_level['moderately_dirty'] & self.laundry_weight['very_heavy'], self.wash_time['long'])  # Added
        
        rule34 = ctrl.Rule(self.dirt_level['very_dirty'] & self.laundry_weight['very_light'], self.wash_time['medium'])  # Added
        rule35 = ctrl.Rule(self.dirt_level['very_dirty'] & self.laundry_weight['light'], self.wash_time['medium'])  # Added
        rule36 = ctrl.Rule(self.dirt_level['very_dirty'] & self.laundry_weight['medium'], self.wash_time['long'])  # Added
        rule37 = ctrl.Rule(self.dirt_level['very_dirty'] & self.laundry_weight['heavy'], self.wash_time['long'])
        rule38 = ctrl.Rule(self.dirt_level['very_dirty'] & self.laundry_weight['very_heavy'], self.wash_time['very_long'])
        
        # Rules for fabric type affecting wash time
        rule39 = ctrl.Rule(self.fabric_type['delicate'], self.wash_time['short'])
        rule40 = ctrl.Rule(self.fabric_type['wool'], self.wash_time['short'])
        rule41 = ctrl.Rule(self.fabric_type['cotton'] & self.dirt_level['very_dirty'], self.wash_time['long'])
        rule42 = ctrl.Rule(self.fabric_type['heavy_duty'] & self.dirt_level['very_dirty'], self.wash_time['very_long'])
        rule43 = ctrl.Rule(self.fabric_type['cotton'] & self.dirt_level['slightly_dirty'], self.wash_time['medium'])  # Added
        rule44 = ctrl.Rule(self.fabric_type['cotton'] & self.dirt_level['moderately_dirty'], self.wash_time['medium'])  # Added
        rule45 = ctrl.Rule(self.fabric_type['synthetic'] & self.dirt_level['slightly_dirty'], self.wash_time['short'])  # Added
        rule46 = ctrl.Rule(self.fabric_type['synthetic'] & self.dirt_level['moderately_dirty'], self.wash_time['medium'])  # Added
        rule47 = ctrl.Rule(self.fabric_type['synthetic'] & self.dirt_level['very_dirty'], self.wash_time['long'])  # Added
        rule48 = ctrl.Rule(self.fabric_type['heavy_duty'] & self.dirt_level['slightly_dirty'], self.wash_time['medium'])  # Added
        rule49 = ctrl.Rule(self.fabric_type['heavy_duty'] & self.dirt_level['moderately_dirty'], self.wash_time['long'])  # Added
        
        # Rules for water temperature
        rule50 = ctrl.Rule(self.fabric_type['delicate'], self.water_temperature['cold'])
        rule51 = ctrl.Rule(self.fabric_type['wool'], self.water_temperature['cold'])
        rule52 = ctrl.Rule(self.fabric_type['cotton'] & self.dirt_level['slightly_dirty'], self.water_temperature['warm'])
        rule53 = ctrl.Rule(self.fabric_type['cotton'] & self.dirt_level['moderately_dirty'], self.water_temperature['warm'])  # Added
        rule54 = ctrl.Rule(self.fabric_type['cotton'] & self.dirt_level['very_dirty'], self.water_temperature['hot'])
        rule55 = ctrl.Rule(self.fabric_type['synthetic'] & self.dirt_level['slightly_dirty'], self.water_temperature['cold'])  # Added
        rule56 = ctrl.Rule(self.fabric_type['synthetic'] & self.dirt_level['moderately_dirty'], self.water_temperature['warm'])
        rule57 = ctrl.Rule(self.fabric_type['synthetic'] & self.dirt_level['very_dirty'], self.water_temperature['hot'])  # Added
        rule58 = ctrl.Rule(self.fabric_type['heavy_duty'] & self.dirt_level['slightly_dirty'], self.water_temperature['warm'])  # Added
        rule59 = ctrl.Rule(self.fabric_type['heavy_duty'] & self.dirt_level['moderately_dirty'], self.water_temperature['hot'])  # Added
        rule60 = ctrl.Rule(self.fabric_type['heavy_duty'] & self.dirt_level['very_dirty'], self.water_temperature['very_hot'])
        
        # Default rules for edge cases - these are crucial
        rule61 = ctrl.Rule(self.laundry_weight['very_light'], self.powder_required['low'])  # Default for very light
        rule62 = ctrl.Rule(self.dirt_level['slightly_dirty'], self.wash_time['short'])  # Default for slightly dirty
        rule63 = ctrl.Rule(self.dirt_level['very_dirty'], self.water_temperature['hot'])  # Default for very dirty
        
        # Create control system
        self.washing_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10,rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20,rule21, rule22, rule23, rule24, rule25, rule26, rule27, rule28, rule29, rule30,
            rule31, rule32, rule33, rule34, rule35, rule36, rule37, rule38, rule39, rule40,
            rule41, rule42, rule43, rule44, rule45, rule46, rule47, rule48, rule49, rule50,
            rule51, rule52, rule53, rule54, rule55, rule56, rule57, rule58, rule59, rule60,
            rule61, rule62, rule63
        ])
        
        # Initialize the control system simulation
        self.washing = ctrl.ControlSystemSimulation(self.washing_ctrl)

    def fuzzify_laundry(self, laundry_weight, dirt_level, fabric_type=3, water_hardness=5):
        """
        Calculate washing parameters based on input variables
        
        Parameters:
        laundry_weight (float): Weight of laundry in kg (0-8)
        dirt_level (float): Level of dirt (1-10)
        fabric_type (float): Type of fabric (1: Delicate, 2: Wool, 3: Cotton, 4: Synthetic, 5: Heavy Duty)
        water_hardness (float): Water hardness level (1-10)
        
        Returns:
        dict: Dictionary containing the output values
        """
        # Ensure we're using proper bounds to prevent errors
        laundry_weight = max(0.0, min(8.0, laundry_weight))
        dirt_level = max(1.0, min(10.0, dirt_level))
        fabric_type = max(1.0, min(5.0, fabric_type))
        water_hardness = max(1.0, min(10.0, water_hardness))
        
        # Input values to the control system
        self.washing.input['laundry_weight'] = laundry_weight
        self.washing.input['dirt_level'] = dirt_level
        self.washing.input['fabric_type'] = fabric_type
        self.washing.input['water_hardness'] = water_hardness
        
        try:
            # Compute the result
            self.washing.compute()
            
            # Get the outputs
            results = {
                'powder_required': self.washing.output['powder_required'],
                'wash_time': self.washing.output['wash_time'],
                'water_temperature': self.washing.output['water_temperature']
            }
            
            return results
        except Exception as e:
            print(f"Warning: Error during fuzzy computation: {e}")
            # Provide default values based on input parameters when fuzzy computation fails
            return self.calculate_fallback_values(laundry_weight, dirt_level, fabric_type, water_hardness)

    def calculate_fallback_values(self, laundry_weight, dirt_level, fabric_type, water_hardness):
        """
        Calculate fallback values when fuzzy computation fails
        Uses linear formulas based on input ranges
        """
        # Default/fallback calculations
        # These are simplified linear relationships that can work when fuzzy logic fails
        
        # Powder calculation based on all parameters
        powder_required = (
            5 +  # Base amount
            (laundry_weight / 8.0) * 30 +  # Weight component (0-30g)
            (dirt_level / 10.0) * 15 +  # Dirt component (0-15g)
            (water_hardness / 10.0) * 10  # Water hardness component (0-10g)
        )
        
        # Wash time calculation
        wash_time = (
            30 +  # Base time
            (laundry_weight / 8.0) * 40 +  # Weight component (0-40 min)
            (dirt_level / 10.0) * 50  # Dirt component (0-50 min)
        )
        
        # Adjust wash time based on fabric type
        if fabric_type < 2:  # Delicate
            wash_time = max(30, min(60, wash_time * 0.7))  # Reduce time for delicate
        elif fabric_type < 3:  # Wool
            wash_time = max(30, min(60, wash_time * 0.8))  # Slightly reduce time for wool
        elif fabric_type > 4:  # Heavy duty
            wash_time = min(120, wash_time * 1.2)  # Increase time for heavy duty
        
        # Water temperature calculation
        water_temperature = 20  # Start with cold
        
        # Adjust temperature based on fabric type
        if fabric_type < 2:  # Delicate
            water_temperature = 25  # Cold for delicate
        elif fabric_type < 3:  # Wool
            water_temperature = 30  # Cool for wool
        elif fabric_type < 4:  # Cotton
            water_temperature = 40 + (dirt_level / 10.0) * 30  # Warm to hot based on dirt
        elif fabric_type < 5:  # Synthetic
            water_temperature = 40 + (dirt_level / 10.0) * 20  # Warm to medium-hot
        else:  # Heavy duty
            water_temperature = 50 + (dirt_level / 10.0) * 40  # Hot to very hot based on dirt
        
        results = {
            'powder_required': round(powder_required, 2),
            'wash_time': round(wash_time, 2),
            'water_temperature': round(water_temperature, 2)
        }
        
        print("Using fallback calculation method")
        return results

    def compute_washing_parameters(self, laundry_weight, dirt_level, fabric_type=3, water_hardness=5):
        """
        Validate inputs and compute washing parameters
        """
        # Input validation with clamping instead of raising exceptions
        if laundry_weight < 0.0 or laundry_weight > 8.0:
            print(f"Warning: Laundry weight {laundry_weight} out of range, clamping to 0-8 kg")
            laundry_weight = max(0.0, min(8.0, laundry_weight))
            
        if dirt_level < 1.0 or dirt_level > 10.0:
            print(f"Warning: Dirt level {dirt_level} out of range, clamping to 1-10")
            dirt_level = max(1.0, min(10.0, dirt_level))
            
        if fabric_type < 1.0 or fabric_type > 5.0:
            print(f"Warning: Fabric type {fabric_type} out of range, clamping to 1-5")
            fabric_type = max(1.0, min(5.0, fabric_type))
            
        if water_hardness < 1.0 or water_hardness > 10.0:
            print(f"Warning: Water hardness {water_hardness} out of range, clamping to 1-10")
            water_hardness = max(1.0, min(10.0, water_hardness))
        
        results = self.fuzzify_laundry(laundry_weight, dirt_level, fabric_type, water_hardness)
        
        print("\nWashing Machine Parameters:")
        print(f"Powder Required: {results['powder_required']:.2f} grams")
        print(f"Wash Time: {results['wash_time']:.2f} minutes")
        print(f"Water Temperature: {results['water_temperature']:.2f}°C")
        
        return results
    
    def plot_membership_functions_3d(self):
        """
        Create a 3D plot of membership functions for each input variable
        """
        fig = plt.figure(figsize=(15, 10))
        
        # Plot for laundry weight membership functions
        ax1 = fig.add_subplot(221, projection='3d')
        x = np.linspace(0, 8, 100)
        y = np.arange(5)  # Number of membership functions
        X, Y = np.meshgrid(x, y)
        Z = np.zeros_like(X)
        
        # Get membership values for each point
        mf_names = ['very_light', 'light', 'medium', 'heavy', 'very_heavy']
        for i, name in enumerate(mf_names):
            for j, x_val in enumerate(x):
                Z[i, j] = fuzz.interp_membership(self.laundry_weight.universe, 
                                                self.laundry_weight[name].mf, 
                                                x_val)
        
        ax1.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
        ax1.set_xlabel('Laundry Weight (kg)')
        ax1.set_ylabel('Membership Functions')
        ax1.set_zlabel('Membership Value')
        ax1.set_yticks(np.arange(5))
        ax1.set_yticklabels(mf_names)
        ax1.set_title('Laundry Weight Membership Functions')
        
        # Plot for dirt level membership functions
        ax2 = fig.add_subplot(222, projection='3d')
        x = np.linspace(1, 10, 100)
        y = np.arange(3)  # Number of membership functions
        X, Y = np.meshgrid(x, y)
        Z = np.zeros_like(X)
        
        # Get membership values for each point
        mf_names = ['slightly_dirty', 'moderately_dirty', 'very_dirty']
        for i, name in enumerate(mf_names):
            for j, x_val in enumerate(x):
                Z[i, j] = fuzz.interp_membership(self.dirt_level.universe, 
                                                self.dirt_level[name].mf, 
                                                x_val)
        
        ax2.plot_surface(X, Y, Z, cmap='plasma', alpha=0.8)
        ax2.set_xlabel('Dirt Level')
        ax2.set_ylabel('Membership Functions')
        ax2.set_zlabel('Membership Value')
        ax2.set_yticks(np.arange(3))
        ax2.set_yticklabels(mf_names)
        ax2.set_title('Dirt Level Membership Functions')
        
        # Plot for fabric type membership functions
        ax3 = fig.add_subplot(223, projection='3d')
        x = np.linspace(1, 5, 100)
        y = np.arange(5)  # Number of membership functions
        X, Y = np.meshgrid(x, y)
        Z = np.zeros_like(X)
        
        # Get membership values for each point
        mf_names = ['delicate', 'wool', 'cotton', 'synthetic', 'heavy_duty']
        for i, name in enumerate(mf_names):
            for j, x_val in enumerate(x):
                Z[i, j] = fuzz.interp_membership(self.fabric_type.universe, 
                                                self.fabric_type[name].mf, 
                                                x_val)
        
        ax3.plot_surface(X, Y, Z, cmap='magma', alpha=0.8)
        ax3.set_xlabel('Fabric Type')
        ax3.set_ylabel('Membership Functions')
        ax3.set_zlabel('Membership Value')
        ax3.set_yticks(np.arange(5))
        ax3.set_yticklabels(mf_names)
        ax3.set_title('Fabric Type Membership Functions')
        
        # Plot for water hardness membership functions
        ax4 = fig.add_subplot(224, projection='3d')
        x = np.linspace(1, 10, 100)
        y = np.arange(3)  # Number of membership functions
        X, Y = np.meshgrid(x, y)
        Z = np.zeros_like(X)
        
        # Get membership values for each point
        mf_names = ['soft', 'medium', 'hard']
        for i, name in enumerate(mf_names):
            for j, x_val in enumerate(x):
                Z[i, j] = fuzz.interp_membership(self.water_hardness.universe, self.water_hardness[name].mf, x_val)
        
        ax4.plot_surface(X, Y, Z, cmap='cividis', alpha=0.8)
        ax4.set_xlabel('Water Hardness')
        ax4.set_ylabel('Membership Functions')
        ax4.set_zlabel('Membership Value')
        ax4.set_yticks(np.arange(3))
        ax4.set_yticklabels(mf_names)
        ax4.set_title('Water Hardness Membership Functions')
        
        plt.tight_layout()
        plt.show()
    
    def plot_output_surfaces(self, output_var='powder_required', fixed_inputs=None):
        """
        Create a 3D surface plot for an output variable based on two input variables,
        with other inputs fixed at specified values
        
        Parameters:
        output_var (str): The output variable to visualize ('powder_required', 'wash_time', or 'water_temperature')
        fixed_inputs (dict): Dictionary with fixed values for the non-plotted input variables
                            Example: {'fabric_type': 3, 'water_hardness': 5}
        """
        if fixed_inputs is None:
            # Default values for non-plotted variables
            fixed_inputs = {'fabric_type': 3, 'water_hardness': 5}  # Default to cotton and medium water hardness
        
        # Create a meshgrid for laundry weight and dirt level
        laundry_range = np.linspace(0, 8, 25)
        dirt_range = np.linspace(1, 10, 25)
        laundry_grid, dirt_grid = np.meshgrid(laundry_range, dirt_range)
        
        # Initialize output grid
        output_grid = np.zeros_like(laundry_grid)
        
        # Calculate output values for each point in the grid
        for i in range(len(dirt_range)):
            for j in range(len(laundry_range)):
                try:
                    # Set inputs to the control system
                    self.washing.input['laundry_weight'] = laundry_grid[i, j]
                    self.washing.input['dirt_level'] = dirt_grid[i, j]
                    self.washing.input['fabric_type'] = fixed_inputs.get('fabric_type', 3)
                    self.washing.input['water_hardness'] = fixed_inputs.get('water_hardness', 5)
                    
                    # Compute the result
                    self.washing.compute()
                    
                    # Get the output
                    output_grid[i, j] = self.washing.output[output_var]
                except:
                    # Fallback values if computation fails
                    result = self.calculate_fallback_values(
                        laundry_grid[i, j], 
                        dirt_grid[i, j],
                        fixed_inputs.get('fabric_type', 3),
                        fixed_inputs.get('water_hardness', 5)
                    )
                    output_grid[i, j] = result[output_grid[i, j]] = result[output_var]
        
        # Create 3D plot
        fig = plt.figure(figsize=(12, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        # Plot the surface
        surf = ax.plot_surface(laundry_grid, dirt_grid, output_grid, cmap=cm.viridis, alpha=0.8,
                              linewidth=0, antialiased=True)
        
        # Add labels and title
        output_labels = {
            'powder_required': 'Powder Amount (grams)',
            'wash_time': 'Wash Time (minutes)',
            'water_temperature': 'Water Temperature (°C)'
        }
        
        ax.set_xlabel('Laundry Weight (kg)')
        ax.set_ylabel('Dirt Level')
        ax.set_zlabel(output_labels.get(output_var, output_var))
        
        # Set title with fixed input info
        fixed_inputs_str = ', '.join([f"{k.replace('_', ' ').title()}: {v}" for k, v in fixed_inputs.items()])
        ax.set_title(f"{output_var.replace('_', ' ').title()} vs Laundry Weight and Dirt Level\n(Fixed: {fixed_inputs_str})")
        
        # Add a color bar
        fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5, label=output_labels.get(output_var, output_var))
        
        plt.tight_layout()
        plt.show()
    
    def plot_3d_comparison(self, fixed_inputs=None):
        """
        Create a 3D plot comparison of all three output variables based on laundry weight and dirt level,
        with other inputs fixed at specified values
        
        Parameters:
        fixed_inputs (dict): Dictionary with fixed values for the non-plotted input variables
                            Example: {'fabric_type': 3, 'water_hardness': 5}
        """
        if fixed_inputs is None:
            # Default values for non-plotted variables
            fixed_inputs = {'fabric_type': 3, 'water_hardness': 5}  # Default to cotton and medium water hardness
        
        # Create a meshgrid for laundry weight and dirt level (using fewer points for speed)
        laundry_range = np.linspace(0, 8, 15)
        dirt_range = np.linspace(1, 10, 15)
        laundry_grid, dirt_grid = np.meshgrid(laundry_range, dirt_range)
        
        # Initialize output grids
        powder_grid = np.zeros_like(laundry_grid)
        time_grid = np.zeros_like(laundry_grid)
        temp_grid = np.zeros_like(laundry_grid)
        
        # Calculate output values for each point in the grid
        for i in range(len(dirt_range)):
            for j in range(len(laundry_range)):
                try:
                    # Set inputs to the control system
                    self.washing.input['laundry_weight'] = laundry_grid[i, j]
                    self.washing.input['dirt_level'] = dirt_grid[i, j]
                    self.washing.input['fabric_type'] = fixed_inputs.get('fabric_type', 3)
                    self.washing.input['water_hardness'] = fixed_inputs.get('water_hardness', 5)
                    
                    # Compute the result
                    self.washing.compute()
                    
                    # Get the outputs
                    powder_grid[i, j] = self.washing.output['powder_required']
                    time_grid[i, j] = self.washing.output['wash_time']
                    temp_grid[i, j] = self.washing.output['water_temperature']
                except:
                    # Fallback values if computation fails
                    result = self.calculate_fallback_values(
                        laundry_grid[i, j], 
                        dirt_grid[i, j],
                        fixed_inputs.get('fabric_type', 3),
                        fixed_inputs.get('water_hardness', 5)
                    )
                    powder_grid[i, j] = result['powder_required']
                    time_grid[i, j] = result['wash_time']
                    temp_grid[i, j] = result['water_temperature']
        
        # Create plot
        fig = plt.figure(figsize=(18, 6))
        
        # Normalize output values to a common scale (0-1) for visualization
        powder_norm = (powder_grid - np.min(powder_grid)) / (np.max(powder_grid) - np.min(powder_grid))
        time_norm = (time_grid - np.min(time_grid)) / (np.max(time_grid) - np.min(time_grid))
        temp_norm = (temp_grid - np.min(temp_grid)) / (np.max(temp_grid) - np.min(temp_grid))
        
        # Plot powder required
        ax1 = fig.add_subplot(131, projection='3d')
        surf1 = ax1.plot_surface(laundry_grid, dirt_grid, powder_grid, cmap=cm.viridis, alpha=0.8)
        ax1.set_xlabel('Laundry Weight (kg)')
        ax1.set_ylabel('Dirt Level')
        ax1.set_zlabel('Powder Amount (g)')
        ax1.set_title('Powder Required')
        fig.colorbar(surf1, ax=ax1, shrink=0.5, aspect=5)
        
        # Plot wash time
        ax2 = fig.add_subplot(132, projection='3d')
        surf2 = ax2.plot_surface(laundry_grid, dirt_grid, time_grid, cmap=cm.plasma, alpha=0.8)
        ax2.set_xlabel('Laundry Weight (kg)')
        ax2.set_ylabel('Dirt Level')
        ax2.set_zlabel('Wash Time (min)')
        ax2.set_title('Wash Time')
        fig.colorbar(surf2, ax=ax2, shrink=0.5, aspect=5)
        
        # Plot water temperature
        ax3 = fig.add_subplot(133, projection='3d')
        surf3 = ax3.plot_surface(laundry_grid, dirt_grid, temp_grid, cmap=cm.magma, alpha=0.8)
        ax3.set_xlabel('Laundry Weight (kg)')
        ax3.set_ylabel('Dirt Level')
        ax3.set_zlabel('Temperature (°C)')
        ax3.set_title('Water Temperature')
        fig.colorbar(surf3, ax=ax3, shrink=0.5, aspect=5)
        
        # Add common title
        fixed_inputs_str = ', '.join([f"{k.replace('_', ' ').title()}: {v}" for k, v in fixed_inputs.items()])
        plt.suptitle(f"Output Variables vs Laundry Weight and Dirt Level\n(Fixed: {fixed_inputs_str})", fontsize=16)
        
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Adjust layout to make room for the suptitle
        plt.show()


def main():
    print("Enhanced Washing Machine Fuzzy Logic System")
    print("------------------------------------------")
    
    # Initialize the fuzzy control system
    try:
        washing_machine = enhanced_washing_machine()
    except Exception as e:
        print(f"Error initializing fuzzy system: {e}")
        return
    
    while True:
        print("\nOptions:")
        print("1. Calculate washing parameters")
        print("2. View 3D membership functions")
        print("3. View 3D surface for powder required")
        print("4. View 3D surface for wash time")
        print("5. View 3D surface for water temperature")
        print("6. View 3D comparison of all outputs")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            try:
                laundry_weight = float(input("Enter laundry weight (0-8 kg): "))
                dirt_level = float(input("Enter dirt level (1-10): "))
                
                fabric_type_info = """
Fabric Type Options:
1: Delicate
2: Wool
3: Cotton
4: Synthetic
5: Heavy Duty
                """
                print(fabric_type_info)
                fabric_type = float(input("Enter fabric type (1-5): "))
                water_hardness = float(input("Enter water hardness level (1-10): "))
                
                results = washing_machine.compute_washing_parameters(laundry_weight, dirt_level, fabric_type, water_hardness)
            except Exception as e:
                print(f"Error: {e}")
                print("Please try again.")
        
        elif choice == '2':
            try:
                washing_machine.plot_membership_functions_3d()
            except Exception as e:
                print(f"Error displaying 3D membership functions: {e}")
        
        elif choice == '3':
            try:
                print("\nFixing other variables for the 3D visualization...")
                fabric_type = float(input("Enter fixed fabric type (1-5, default=3): ") or "3")
                water_hardness = float(input("Enter fixed water hardness (1-10, default=5): ") or "5")
                
                washing_machine.plot_output_surfaces(
                    output_var='powder_required',
                    fixed_inputs={'fabric_type': fabric_type, 'water_hardness': water_hardness}
                )
            except Exception as e:
                print(f"Error displaying 3D surface: {e}")
        
        elif choice == '4':
            try:
                print("\nFixing other variables for the 3D visualization...")
                fabric_type = float(input("Enter fixed fabric type (1-5, default=3): ") or "3")
                water_hardness = float(input("Enter fixed water hardness (1-10, default=5): ") or "5")
                
                washing_machine.plot_output_surfaces(
                    output_var='wash_time',
                    fixed_inputs={'fabric_type': fabric_type, 'water_hardness': water_hardness}
                )
            except Exception as e:
                print(f"Error displaying 3D surface: {e}")
        
        elif choice == '5':
            try:
                print("\nFixing other variables for the 3D visualization...")
                fabric_type = float(input("Enter fixed fabric type (1-5, default=3): ") or "3")
                water_hardness = float(input("Enter fixed water hardness (1-10, default=5): ") or "5")
                
                washing_machine.plot_output_surfaces(
                    output_var='water_temperature',
                    fixed_inputs={'fabric_type': fabric_type, 'water_hardness': water_hardness}
                )
            except Exception as e:
                print(f"Error displaying 3D surface: {e}")
        
        elif choice == '6':
            try:
                print("\nFixing other variables for the 3D visualization...")
                fabric_type = float(input("Enter fixed fabric type (1-5, default=3): ") or "3")
                water_hardness = float(input("Enter fixed water hardness (1-10, default=5): ") or "5")
                
                washing_machine.plot_3d_comparison(
                    fixed_inputs={'fabric_type': fabric_type, 'water_hardness': water_hardness}
                )
            except Exception as e:
                print(f"Error displaying 3D comparison: {e}")
        
        elif choice == '7':
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")
    
    print("Thank you for using the Enhanced Washing Machine System!")

if __name__ == "__main__":
    main()


# In[ ]:




