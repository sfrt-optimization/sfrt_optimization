import csv

a_square_points = [[-140, -10, -5.0], [-140, 50, -5.0], [-140, 20, -2.5], [-170, 10, 2.5], [-170, -20, 7.5], [-140, -40, 7.5], [-170, 40, 12.5], [-110, 60, 17.5], [-120, 0, 20.0], [-110, -30, 20.0], [-150, 0, 25.0], [-140, 60, 25.0], [-140, 30, 27.5], [-160, -40, 30.0], [-80, 50, 35.0], [-180, 10, 37.5], [-110, 40, 40.0], [-180, -20, 42.5], [-170, 50, 42.5], [-130, -50, 45.0], [-140, -20, 47.5], [-110, 10, 47.5], [-100, 70, 47.5], [-110, -20, 50.0], [-140, 10, 55.0], [-140, 40, 62.5], [-90, 30, 62.5], [-70, 60, 62.5], [-170, 30, 67.5], [-170, 0, 70.0], [-160, -30, 70.0], [-150, 70, 70.0], [-130, -30, 75.0], [-90, 80, 75.0], [-120, 0, 77.5], [-120, 70, 82.5], [-120, 30, 85.0], [-90, 50, 85.0], [-150, 20, 90.0], [-150, -10, 92.5], [-140, 50, 97.5], [-100, 30, 107.5], [-80, 70, 107.5], [-130, 20, 112.5], [-110, 60, 112.5]]
with open('../csv_outputs/A_square_points.csv','w', newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerows(a_square_points)

b_square_points =[[-40, -20, -110.0], [-30, -50, -102.5], [-60, -50, -95.0], [-60, -20, -87.5], [-20, -20, -87.5], [-40, -80, -80.0], [-10, -60, -80.0], [-80, -40, -72.5], [-70, -70, -72.5], [-40, -40, -72.5], [-60, 0, -65.0], [-30, -10, -60.0], [-10, -80, -57.5], [-10, -40, -57.5], [-80, -20, -50.0], [-50, -80, -50.0], [-80, -60, -45.0], [-50, -50, -45.0], [-30, -30, -32.5], [-10, -60, -32.5], [-60, -10, -25.0], [-70, -40, -22.5], [-60, -70, -22.5], [-40, -50, -10.0]]
with open('../csv_outputs/B_square_points.csv','w', newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerows(b_square_points)

a_triangular_points = [[-142.634850253404, -5.0, -7.5], [-168.6156123669372, 10, 0.0], [-168.6156123669372, -20, 5.0], [-142.634850253404, -35.0, 5.0], [-133.97459621555961, 60, 7.5], [-133.97459621555961, 20, 10.0], [-116.65408813987085, -10, 10.0], [-168.6156123669372, 40, 12.5], [-116.65408813987085, -40, 20.0], [-107.99383410202647, 55.0, 22.5], [-177.2758664047816, -5.0, 30.0], [-159.9553583290928, -35.0, 30.0], [-151.2951042912484, 10, 32.5], [-133.97459621555961, 40, 32.5], [-133.97459621555961, -20, 35.0], [-107.99383410202647, 25.0, 35.0], [-177.2758664047816, 25.0, 37.5], [-159.9553583290928, 55.0, 37.5], [-82.01307198849332, 50, 37.5], [-133.97459621555961, -50, 42.5], [-107.99383410202647, -5.0, 42.5], [-116.65408813987085, 70, 50.0], [-177.2758664047816, -25.0, 55.0], [-151.2951042912484, 30, 55.0], [-151.2951042912484, -10, 57.5], [-125.31434217771523, 15.0, 57.5], [-177.2758664047816, 5.0, 60.0], [-116.65408813987085, -30, 60.0], [-73.35281795064894, 65.0, 62.5], [-151.2951042912484, -40, 65.0], [-99.33358006418209, 50, 65.0], [-159.9553583290928, 55.0, 70.0], [-99.33358006418209, 80, 72.5], [-133.97459621555961, 70, 75.0], [-99.33358006418209, 20, 75.0], [-125.31434217771523, -5.0, 80.0], [-125.31434217771523, 35.0, 80.0], [-151.2951042912484, -20, 87.5], [-82.01307198849332, 50, 90.0], [-151.2951042912484, 10, 92.5], [-151.2951042912484, 40, 95.0], [-107.99383410202647, 65.0, 97.5], [-99.33358006418209, 30, 107.5], [-125.31434217771523, 15.0, 110.0], [-125.31434217771523, 45.0, 112.5], [-82.01307198849332, 70, 112.5]]
with open('../csv_outputs/A_triangular_points.csv','w', newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerows(a_triangular_points)

b_triangular_points = [[-47.37205583711578, -20, -110.0], [-47.37205583711578, -50, -102.5], [-21.391293723582613, -35.0, -100.0], [-30.051547761427003, -70, -87.5], [-64.69256391280456, -20, -85.0], [-30.051547761427003, -10, -85.0], [-64.69256391280456, -70, -80.0], [-4.070785647893839, -55.0, -75.0], [-38.71180179927139, -45.0, -72.5], [-82.01307198849332, -40, -70.0], [-56.03230987496017, 5.0, -70.0], [-12.731039685738226, -80, -60.0], [-12.731039685738226, -30, -60.0], [-47.37205583711578, -80, -57.5], [-73.35281795064894, -15.0, -55.0], [-38.71180179927139, -15.0, -55.0], [-73.35281795064894, -65.0, -50.0], [-47.37205583711578, -50, -42.5], [-4.070785647893839, -55.0, -42.5], [-56.03230987496017, -15.0, -30.0], [-56.03230987496017, -75.0, -27.5], [-30.051547761427003, -30, -27.5], [-64.69256391280456, -40, -15.0], [-38.71180179927139, -55.0, -10.0]]

with open('../csv_outputs/B_triangular_points.csv','w', newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerows(b_triangular_points)
