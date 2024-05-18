

import math, random 

def OTPgenerator() : 
	digits_in_otp = '0123456789'
	OTP = "" 
	length = len(digits_in_otp)
	for i in range(6) : 
		OTP += digits_in_otp[math.floor(random.random() * length)] 
	return OTP 