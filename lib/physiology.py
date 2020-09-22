from sympy import log, Pow


def nernst_potential(t: float, z: float, x_out: float, x_in: float):
    """
    Calculates the equilibrium potential for ion.
    R (universal gas constant) and F (Faraday's constant) are predefined.

    :param t: temperature in Kelvin.
    :param z: valence of ion (+1, +2, -1, -2, etc.).
    :param x_out: concentration of ion in extracellular fluid, in mM.
    :param x_in: concentration of ion in intracellular fluid, in mM.
    :return: equilibrium potential for given ion in milli-volts.
    """
    r = 8.314  # J.K^-1 (Joules per Kelvin per mole)
    f = 96485  # C.mol^-1 (Coulombs per mole)

    eq = ((r * t)/(z * f)) * log((x_out/x_in)) * 1000
    return eq.evalf()


def mean_arterial_pressure(systolic: int, diastolic: int):
    """
    Calculates pulse pressure and mean arterial pressure.

    :param systolic: systolic blood pressure in mm Hg.
    :param diastolic: diastolic blood pressure in mm Hg.
    :return: pulse pressure and mean arterial pressure, both in mm Hg.
    """
    pulse = systolic - diastolic
    mean_arterial = diastolic + (0.3333333 * pulse)
    return pulse, mean_arterial


def goldman_hodgkin_katz(t: float, p_k: float, p_na: float, p_cl: float,
                         k_out: float, k_in: float, na_out: float, na_in: float,
                         cl_out: float, cl_in: float):
    """
    Calculates resting membrane potential for a real cell.
    R (universal gas constant) and F (Faraday's constant) are predefined.

    :param t: temperature in Kelvin.
    :param p_k: relative membrane permeability for potassium.
    :param p_na: relative membrane permeability for sodium.
    :param p_cl: relative membrane permeability for chloride.
    :param k_out: concentration of potassium in Extra Cellular Fluid (ECF).
    :param k_in: concentration of potassium in Intra Cellular Fluid (ICF).
    :param na_out: concentration of sodium in ECF.
    :param na_in: concentration of sodium in ICF.
    :param cl_out: concentration of chloride in ECF.
    :param cl_in: concentration of chloride in ICF.
    :return: resting membrane potential in mV or Volts.
    """
    r = 8.314  # J.K^-1 (Joules per Kelvin per mole)
    f = 96485  # C.mol^-1 (Coulombs per mole)

    eq = ((r * t)/f) * log((p_k * k_out + p_na * na_out + p_cl * cl_in) /
                           (p_k * k_in + p_na * na_in + p_cl * cl_out))
    return eq.evalf()


def electrochemical_driving_force(veq: float, vm: float):
    """
    Calculates electrochemical driving force of ion across membrane.

    :param veq: equilibrium potential, calculated using Nernst equation.
    :param vm: membrane potential, calculated using Goldman-Hodgkin-Katz equation.
    :return: electrochemical driving force of ion in mV.
    """
    driving_force = vm - veq
    return driving_force


def temperature_coefficient(t_1: float, t_2: float, r_1: float, r_2: float):
    """
    Calculates temperature coefficient of reaction.

    :param t_1: temperature when r_1 measured.
    :param t_2: temperature when r_2 measured.
    :param r_1: reaction rate at t_1.
    :param r_2: reaction rate at t_2.
    :return: temperature coefficient, unit-less.
    """
    eq = Pow((r_2/r_1), (10/(t_2-t_1)))
    return eq.evalf()


def time_diffusion_distance(x: float, d: float):
    """
    Calculates time elapsed for solute to diffuse over a distance.

    :param x: mean distance traveled by diffusing solute in one direction.
    :param d: diffusion coefficient of solute in free solution.
    :return: elapsed time for solute to diffuse.
    """
    eq = (Pow(x, 2)) / (2 * d)
    return eq.evalf()


def bmi_metric(kg: float, m: float):
    """
    Calculates body mass index using metric units.

    :param kg: body mass in kilograms.
    :param m: height in meters.
    :return: body mass index in kg/m^2.
    """
    eq = (kg / Pow(m, 2))
    return eq.evalf()


def bmi_imperial(lb: float, inches: float):
    """
    Calculates body mass index using imperial units.

    :param lb: body weight in pounds.
    :param inches: height in inches.
    :return: body mass index in kg/m^2 (by multiplying 703.0704).
    """
    eq = (lb / Pow(inches, 2)) * 703.0704
    return eq.evalf()


def inches_to_millimeters(inches: float):
    """
    Converts inches to millimeters.

    :param inches: any measurement in inches.
    :return: input inches converted to millimeters.
    """
    return inches * 2.54


def body_fat_male(height: float, neck: float, waist: float):
    """
    Calculates body fat percentage in males based on US Navy formula.
    Requires measurements to be converted to millimeters.

    :param height: height in inches.
    :param neck: neck circumference in inches.
    :param waist: waist circumference in inches.
    :return: body fat percentage.
    """
    height = inches_to_millimeters(height)
    neck = inches_to_millimeters(neck)
    waist = inches_to_millimeters(waist)

    eq = (495 / (1.0324 - 0.19077 * log((waist - neck), 10) + 0.15456 * log(height, 10)) - 450)
    return eq.evalf()


def body_fat_female(height: float, neck: float, waist: float, hip: float):
    """
    Calculates body fat percentage in females based on US Navy formula.
    Requires measurements to be converted to millimeters.

    :param height: height in inches.
    :param neck: neck circumference in inches.
    :param waist: waist circumference in inches.
    :param hip: hip circumference in inches.
    :return: body fat percentage.
    """
    height = inches_to_millimeters(height)
    neck = inches_to_millimeters(neck)
    waist = inches_to_millimeters(waist)
    hip = inches_to_millimeters(hip)

    eq = (495 / (1.29579 - 0.35004 * log((waist + hip - neck), 10) + 0.22100 * log(height, 10)) - 450)
    return eq.evalf()
