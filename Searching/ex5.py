def display_coordinate_and_distance(x0, y0, points):
    if points == []:
        return
    else:
        temp = {}
        distances = []
        for i in points:
            point = [float(x) for x in i.split()]
            x1,y1 = point[0], point[1]
            dx = abs(x0-x1)
            dy = abs(y0-y1)
            distance = pow(pow(dx,2)+pow(dy,2),1/2)
            if distance == 0.0:
                continue
            distances.append(distance)
            temp[distance] = i
        if distances == []:
            return
        new_points = list(temp.values())
        next_start = [float(x) for x in temp[min(distances)].split()]
        print(f"[{x0}, {y0}] -> {next_start} | The distance is {min(distances):.4f}")
        display_coordinate_and_distance(next_start[0], next_start[1], new_points)

inp = input("Enter a list of points: ").split('/')
points = inp[0].split(',')
start = [float(x) for x in inp[1].split()]
x0,y0 = start[0], start[1]

show_points = []
for i in points:
    show_points.append([float(x) for x in i.split()])

if inp[1] not in inp[0]:
    print(f"{start} is not in {show_points}")
else:
    display_coordinate_and_distance(x0, y0, points)

'''
example test cases

Enter a list of points: 1 1,2 2,3 3/1 1
[1.0, 1.0] -> [2.0, 2.0] | The distance is 1.4142
[2.0, 2.0] -> [3.0, 3.0] | The distance is 1.4142

Enter a list of points: 1 1,3 3,5.5 5.5,4 4/3 3
[3.0, 3.0] -> [4.0, 4.0] | The distance is 1.4142
[4.0, 4.0] -> [5.5, 5.5] | The distance is 2.1213
[5.5, 5.5] -> [1.0, 1.0] | The distance is 6.3640

Enter a list of points: -3 0,1 4,348 342,49 -10,-34 12/1 4
[1.0, 4.0] -> [-3.0, 0.0] | The distance is 5.6569
[-3.0, 0.0] -> [-34.0, 12.0] | The distance is 33.2415
[-34.0, 12.0] -> [49.0, -10.0] | The distance is 85.8662
[49.0, -10.0] -> [348.0, 342.0] | The distance is 461.8495

Enter a list of points: 123 456,-4627 9921,0 -716,40 32,1 738,83 0,6321 342/0 0
[0.0, 0.0] is not in [[123.0, 456.0], [-4627.0, 9921.0], [0.0, -716.0], [40.0, 32.0], [1.0, 738.0], [83.0, 0.0], [6321.0, 342.0]]
'''
