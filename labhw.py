circleNum = int(input())
circles = []
intersectedCircles = []


def main():
    makelist() 
    checkConnected()
    out()


def makelist():
    for i in range(circleNum):
        circle = input()
        x = circle.split()
        circles.append(x)



def findXpoints(circle1, circle2):
    points = []
    points.append(int(circle1[0]) - int(circle1[2]))
    points.append(int(circle1[0]) + int(circle1[2]))
    points.append(int(circle2[0]) - int(circle2[2]))
    points.append(int(circle2[0]) + int(circle2[2]))
    return abs(min(points) - max(points))

def findYpoints(circle1, circle2):
    points = []
    points.append(int(circle1[1]) - int(circle1[2]))
    points.append(int(circle1[1]) + int(circle1[2]))
    points.append(int(circle2[1]) - int(circle2[2]))
    points.append(int(circle2[1]) + int(circle2[2]))
    return abs(min(points) - max(points))

def checkConnected():
    for i in range(circleNum):
        for x in range(i, circleNum):
            if i != x:
                dis = ((int(circles[i][0]) - int(circles[x][0])) ** 2 + (int(circles[i][1]) - int(circles[x][1]))**2) ** (1/2)
                if dis < int(circles[i][2]) + int(circles[x][2]):
                    intersectedCircles.extend((i, x))


def areaOfNonIntersect():
    sum = 0
    for i in range(circleNum):
        if i not in intersectedCircles:
            sum += (int(circles[i][2]) * 2)**2
    return sum
            

def areaOfIntersect():
    sum = 0
    divideIntersects = [intersectedCircles[i:i + 2] for i in range(0, len(intersectedCircles), 2)]
    for i in range(len(divideIntersects)):
        x = findXpoints(circles[divideIntersects[i][0]], circles[divideIntersects[i][1]])
        y = findYpoints(circles[divideIntersects[i][0]], circles[divideIntersects[i][1]])
        sum += x * y
    return sum

def out():
    for i in range(len(circles)):
        print("( {0} {1} ) rad: {2}".format(circles[i][0], circles[i][1], circles[i][2]))
    print("Total rect area:", areaOfNonIntersect() + areaOfIntersect())

main()