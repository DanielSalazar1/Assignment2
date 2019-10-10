def c_to_f(celsius):
    #Formula = (c + 9/5) + 32
    f = (c * 9/5) + 32
    return f

c = 100.0
f = c_to_f(c)

def c_to_k(celsius):
    #Formula = K = °C + 273.15
    #Took from https://www.softschools.com/formulas/physics/kelvin_to_celsius_formula/47/
    k = c + 273.15
    return k

def f_to_c(Fahrenheit):
    #Formula = (32 °F − 32) × 5 / 9
    #https://www.google.com/search?sxsrf=ACYBGNTcnBxSPeT_c73q8f_jn1O0NkRh3A%3A1568156230358&source=hp&ei=Rip4XcH4E-bB_QbnsJagAg&q=formula+from+fahrenheit+to+celsius&oq=formula+from+fah&gs_l=psy-ab.1.0.0i203l2j0i22i10i30j0i22i30l7.58.4066..12804...0.0..0.140.1953.2j14......0....1..gws-wiz.......35i39i19j35i39j0i67j0.wdfp0Bzf_M4
    c = (f - 32) * 5 / 9
    return c

def f_to_k(Fahrenheit):
    #Formula = (0 °F − 32) × 5 / 9 + 273,15
    #Took from https://www.google.com/search?sxsrf=ACYBGNQ1lXuZy2lJINt1OYvQBpI3Cpf2uQ%3A1568156244000&ei=Uyp4XcDOPPCm_QbywYWYDA&q=formula+from+fahrenheit+to+kelvin&oq=formula+from+fahrenheit+to+kelvin&gs_l=psy-ab.3..0i203j0i22i10i30j0i22i30l6.496385.496975..497230...0.2..0.190.1061.0j6......0....1..gws-wiz.......0i71j0i19j0i22i10i30i19j0i22i30i19.5qfca7p3ClI&ved=0ahUKEwiAxICfrcfkAhVwU98KHfJgAcMQ4dUDCAs&uact=5
    k = (f - 32) * 5 / 9 + 273.15
    return k

def k_to_c(kelvin):
    #Formula = K = °C + 273.15
    #Took from https://www.softschools.com/formulas/physics/kelvin_to_celsius_formula/47/
    c = k - 273.15
    return c
