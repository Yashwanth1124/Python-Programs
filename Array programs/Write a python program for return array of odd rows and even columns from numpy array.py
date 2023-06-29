mport numpy
samplearray = numpy.array([[3,6,9,12],[15,18,21,24]])
newarray = samplearray[::2,1::2]
print(newarray)