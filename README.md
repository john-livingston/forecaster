forecaster
==========

Forecaster is a probabilistic mass-radius relation. See the [original](https://github.com/chenjj2/forecaster) code for more details.

Usage
-----

The usage differs from the original due to packaging and Python 3 compatibility updates.

A simple example:

	import forecaster
	
	# predict the mean and std of mass given radius measurements
	Mmedian, Mplus, Mminus = forecaster.Rstat2M(3, 0.5)
