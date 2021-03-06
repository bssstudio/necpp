#nec_norm_rx_pattern.py

#header generated by SWIG

import _PyNEC

def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "this"):
        if isinstance(value, class_type):
            self.__dict__[name] = value.this
            if hasattr(value,"thisown"): self.__dict__["thisown"] = value.thisown
            del value.thisown
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name) or (name == "thisown"):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types

#end of the header generated by SWIG



from numpy.numarray import *

#some utility functions

def _get_mag(arg0): 
	"""
	Returns the array of receiving gain not yet normalized.
	"""
    	n_theta = _get_n_theta(arg0)
	n_phi = _get_n_phi(arg0)
	ar = numarray.reshape(_PyNEC.nec_norm_rx_pattern_get_mag(arg0),(n_theta, n_phi))
	ar.transpose()
	return ar


def _get_n_theta(arg0):
	"""
	Returns the number of theta angles.
	"""
	return _PyNEC.nec_norm_rx_pattern_get_n_theta(arg0)


def _get_n_phi(arg0):
	"""
	Returns the number of phi angles.
	"""
	return _PyNEC.nec_norm_rx_pattern_get_n_phi(arg0)


def _get_theta_start(arg0):
	"""
	Returns the first value of theta in degrees.
	"""
	return _PyNEC.nec_norm_rx_pattern_get_theta_start(arg0)


def _get_phi_start(arg0):
	"""
	Returns the first value of phi angles in degrees.
	"""
	return _PyNEC.nec_norm_rx_pattern_get_phi_start(arg0)


def _get_delta_theta(arg0):
	"""
	Returns the increment for theta in degrees.
	"""
	return _PyNEC.nec_norm_rx_pattern_get_delta_theta(arg0)


def _get_delta_phi(arg0):
	"""
	Returns the increment for phi in degrees.
	"""
	return _PyNEC.nec_norm_rx_pattern_get_delta_phi(arg0)



#class "nec_norm_rx_pattern"

class nec_norm_rx_pattern(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, nec_norm_rx_pattern, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, nec_norm_rx_pattern, name)
    def __init__(self): raise RuntimeError, "No constructor defined"
    def __repr__(self):
        return "<%s.%s; proxy of C++ nec_norm_rx_pattern instance at %s>" % (self.__class__.__module__, self.__class__.__name__, self.this,)
    
    
    def get_frequency(*args):
    	"""
	Returns the frequency in Hertz.
	"""
    	return _PyNEC.nec_norm_rx_pattern_get_frequency(*args)
    
    
    def get_eta(*args):
    	"""
	Returns the value of eta in degrees.
	"""
	return _PyNEC.nec_norm_rx_pattern_get_eta(*args)
	
	
    def get_axial_ratio(*args):
    	"""
	Returns the axial ratio (no units).
	"""
	return _PyNEC.nec_norm_rx_pattern_get_axial_ratio(*args)
	
	
    def get_segment_number(*args):
    	"""
	Returns the segment number.
	"""
	return _PyNEC.nec_norm_rx_pattern_get_segment_number(*args)
	
	
    def get_polarization_type(*args):
    	"""
	Return the polarization type.
	"""
	return _PyNEC.nec_norm_rx_pattern_get_type(*args)
	
	
    def get_norm_factor(*args):
    	"""
	Returns the normalization factor in Amperes.
	"""
	return _PyNEC.nec_norm_rx_pattern_get_norm_factor(*args)
	
	
    def get_coordinates(*args):
    	"""
	Returns the array of coordinates of the elements of the other arrays :
		an array of tuples (theta, phi)  - in (degrees, degrees).
	""" 
    	n_theta=_get_n_theta(*args)
        n_phi=_get_n_phi(*args)
	theta_start = _get_theta_start(*args)
	delta_theta = _get_delta_theta(*args)
	phi_start = _get_phi_start(*args)
	delta_phi = _get_delta_phi(*args)
	l=[]
	
	for i in range(n_phi) :
			for j in range(n_theta) :
				l.append((theta_start+j*delta_theta, phi_start+i*delta_phi))
	
	ar = numarray.array(l);
	ar = numarray.reshape(ar, (n_phi,n_theta,2))
	return ar 

	    
    def get_magnitude(*args):
    	"""
	Returns the array of magnitude of the normalized receiving gain (no units).
	"""
    	norm_factor = nec_norm_rx_pattern.get_norm_factor(*args)
    	return _get_mag(*args)/norm_factor
	

    def get_gain(self,*args):
    	"""
	Returns the array of normalized receiving gain in dB.
	""" 
    	mag = self.get_magnitude(*args)
	gain = 20*numarray.ma.log10(mag)
	gain.set_fill_value(-999.999)
	return gain.filled()



class nec_norm_rx_patternPtr(nec_norm_rx_pattern):
    def __init__(self, this):
        _swig_setattr(self, nec_norm_rx_pattern, 'this', this)
        if not hasattr(self,"thisown"): _swig_setattr(self, nec_norm_rx_pattern, 'thisown', 0)
        _swig_setattr(self, nec_norm_rx_pattern,self.__class__,nec_norm_rx_pattern)
_PyNEC.nec_norm_rx_pattern_swigregister(nec_norm_rx_patternPtr)
