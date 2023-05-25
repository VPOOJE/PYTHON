
'''The below picture includes five geometrical shapes.
You have to write Python code that includes five different functions:
sphere(), cylinder(), cone(), rectangular_prism(), and triangular_prism().
You should get the respective values in the formula for the shapes,
and they should be passed to the function as a parameter.
If any of the shapes include "π” (pi), then pi value should be passed
as the default argument, and functions should return the SURFACE AREA AND
VOLUME of the respective geometrical shapes. 
Formula for calculating surface area and volume of the shapes were given
in the picture. '''
def geometrical_shapes(r=3,h=10,w=2,b=2,l=12,pi=3.14,s=6):
    SA_sphere=4*pi*r*r
    V_sphere=4/3*pi*r*r*r
    SA_cylinder=2*pi*r*r+2*pi*r*h
    V_cylinder=pi*r*r*h
    SA_cone=pi*r*s+pi*r*r
    V_cone=1/3*pi*r*r*h
    SA_rp=2*(l*w+l*h+w*h)
    V_rp=l*w*h
    SA_tp=b*h+2*l*s+l*b
    V_tp=1/2*(b*l)*h
    return(SA_sphere,V_sphere,SA_cylinder,V_cylinder,SA_cone,SA_rp,V_rp,SA_tp,V_tp)
SA_sphere,V_sphere,SA_cylinder,V_cylinder,SA_cone,SA_rp,V_rp,SA_tp,V_tp=geometrical_shapes(r=3,h=10,w=2,b=2,l=12,pi=3.14,s=6)
print("the surface area and volume is",SA_sphere,V_sphere,SA_cylinder,V_cylinder,SA_cone,SA_rp,V_rp,SA_tp,V_tp)
