courses = ["ECE", "CSE", "EEE", "CIVIL", "MECH"]
duration = ["4.5 years", "4.7 years", "4.3 years", "4.4 years", "4.1 years"]
fees = [70000, 80000, 70000, 70000, 85000]
for (c, d, f) in zip(courses, duration, fees) :
    
    print(c , d, f);
