### import required modules
from mlxtend.evaluate import permutation_test

print ("\n...Starting p-test...")

print ("\nThe first test contains some random stuff found online")

### set treatment and control variables
treatment = [ 28.44,  29.32,  31.22,  29.58,  30.34,  28.76,  29.21,  30.4 ,
              31.12,  31.78,  27.58,  31.57,  30.73,  30.43,  30.31,  30.32,
              29.18,  29.52,  29.22,  30.56]

control = [ 33.51,  30.63,  32.38,  32.52,  29.41,  30.93,  49.78,  28.96,
            35.77,  31.42,  30.76,  30.6 ,  23.64,  30.54,  47.78,  31.98,
            34.52,  32.42,  31.32,  40.72]

print ("\nThe treatment set is:", treatment)
print ("\nThe control set is:", control)

print ("\nNow let's start our test...")

### evaluate the p_test
p_value = permutation_test(treatment, control,
               method='approximate',
               num_rounds=10000,
               seed=0)

avg_treatment = sum(treatment) / len(treatment)
avg_control = sum(control) / len(control)

print ("\n\nthe mean of the treatment is: ", avg_treatment)
print ("\n\nthe mean of the control is: ", avg_control)
print ("\n\nthe p_value of the test is: ", p_value)
print("\n\np-value is less than `.05` so the experiment wins! :D") if p_value <= .05 else print("\n\np-value is greater than `.05` so the experiment loses :(")
####################

print ("\n\n")
print ("#"*10)

treatment = [50, 55, 52, 49, 59, 50, 51, 48, 50, 55]
control = [40, 45, 42, 39, 49, 40, 41, 38, 40, 45]

print ("\n\n\nLet's move onto our second test")
print ("\n\nThe second test contains hand-curated values.")
print ("\nThe treatment contains values that are obviously much higher than the control")

print ("\nThe treatment set is:", treatment)
print ("\nThe control set is:", control)

### evaluate the p_test
p_value = permutation_test(treatment, control,
               method='approximate',
               num_rounds=10000,
               seed=0)

avg_treatment = sum(treatment) / len(treatment)
avg_control = sum(control) / len(control)

print ("\n\nthe mean of the treatment is: ", avg_treatment)
print ("\n\nthe mean of the control is: ", avg_control)
print ("\n\nthe p_value of the test is: ", p_value)
print("\n\np-value is less than `.05` so the experiment wins! :D") if p_value <= .05 else print("\n\np-value is greater than `.05` so the experiment loses :(")

treatment   = [50, 51, 51, 49, 51, 50, 51, 52, 50, 51]
control     = [50, 51, 51, 49, 51, 50, 51, 52, 50, 52]

####################
print ("\n\n")
print ("#"*10)

print ("\n\n\nLet's move onto our third test")
print ("\n\nThe third test also contains hand-curated values.")
print ("\nThe treatment and control, however, are only 1 value different")

print ("\nThe treatment set is:", treatment)
print ("\nThe control set is:", control)

### evaluate the p_test
p_value = permutation_test(treatment, control,
               method='approximate',
               num_rounds=10000,
               seed=0)

avg_treatment = sum(treatment) / len(treatment)
avg_control = sum(control) / len(control)

print ("\n\nthe mean of the treatment is: ", avg_treatment)
print ("\n\nthe mean of the control is: ", avg_control)
print ("\n\nthe p_value of the test is: ", p_value)
print("\n\np-value is less than `.05` so the experiment wins! :D") if p_value <= .05 else print("\n\np-value is greater than `.05` so the experiment loses :(")