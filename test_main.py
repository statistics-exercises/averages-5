import scipy.stats as st
import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_first_moment(self) : 
        fighand=plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        self.assertTrue( len(this_x)==200, "your graph has the wrong number of coordinates" )
        for i in range( len(this_x) ) :
             self.assertTrue( np.abs(i + 1 - this_x[i])<1e-7, "the x-coordinates in your plot are incorrect" )
             bar = np.sqrt(1/12/(i+1))*scipy.stats.norm.ppf( (0.99 + 1) / 2 )
             self.assertTrue( np.fabs( this_y[i] - 0.5 )<bar, "the values you have computed for the first moment appear to be incorrect" )
   
    def test_second_moment(self)
        fighand=plt.gca()
        figdat = fighand.get_lines()[2].get_xydata()
        this_x, this_y = zip(*figdat)
        samples = np.zeros(100)
        for j in range(100) :
          for k in range(len(this_y)) : 
             myvar = np.random.uniform(0,1) 
             samples[j] = samples[j] + myvar*myvar
          samples[j] = samples[j] / len(this_y)
        self.assertTrue( this_y[-1]>np.percentile(samples,1) and this_y[-1]<np.percentile(samples,99), "the values you have computed for the second moment appear to be incorrect"  )
            
    def test_second_moment(self)
        fighand=plt.gca()
        figdat = fighand.get_lines()[3].get_xydata()
        this_x, this_y = zip(*figdat)
        samples = np.zeros(100)
        for j in range(100) :
          for k in range(len(this_y)) : 
             myvar = np.random.uniform(0,1) 
             samples[j] = samples[j] + myvar*myvar*myvar
          samples[j] = samples[j] / len(this_y)
        self.assertTrue( this_y[-1]>np.percentile(samples,1) and this_y[-1]<np.percentile(samples,99), "the values you have computed for the third moment appear to be incorrect"  )
                         
   
