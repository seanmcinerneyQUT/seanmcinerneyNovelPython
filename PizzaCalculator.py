totalSlices = int(input("How many slices of pizza did you start with?"))
eatenSlices = int(input("How many slices have you eaten?"))
remainingSlices = totalSlices - eatenSlices
if remainingSlices < 0.5*totalSlices:
    print("Wooooah! Ease up. You only have "+str(remainingSlices)+"/"+str(totalSlices)+" slices left.")
else:
    print("Nice! You still have "+str(remainingSlices)+"/"+str(totalSlices)+" slices left.")
   