forecaster
==========

This is a probabilistic mass-radius relation. See [original repo](https://github.com/chenjj2/forecaster) for more details.

Usage
-----

The usage differs from the original due to packaging and Python 3 compatibility updates.

A simple example:

	import forecaster
 
	# predict the mass given radius mean and standard deviation (Earth units)
	rad = 3
	rad_err = 0.5
	Mmedian, Mplus, Mminus = forecaster.Rstat2M(rad, rad_err)
