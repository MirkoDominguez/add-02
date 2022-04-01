from machine import ADC
import utime
res = 0

val1 = 0
s1 = ADC(27)
convert = 3.3 / (65535)
  
while 1:
  val1 = s1.read_u16() * convert
  res = val1 / 0.01
  resformateado = "{:.2f}".format(res)
  print ("La temperatura es: ()" .format(resformateado))
  utime.sleep(1)
  
  