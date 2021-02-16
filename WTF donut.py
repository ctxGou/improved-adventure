from math import *
import os

theta_spacing = 0.07
phi_spacing = 0.02

screen_width = 40
screen_height = 40
R1 = 1
R2 = 2
K2 = 5
K1 = screen_width * K2 * 3 / (8 * (R1 + R2))


def update(A, B):
    cosA = cos(A)
    sinA = sin(A)
    cosB = cos(B)
    sinB = sin(B)

    output = []
    zbuffer = []
    for a in range(screen_height):
        output.append([])
        zbuffer.append([])
        for b in range(screen_width):
            output[a].append(' ')
            zbuffer[a].append(0)

    theta = float(0.07)  # 二维圆的角
    phi = float(0.02)  # 二维圆旋转称三维环的角

    while theta < 2 * pi:
        costheta = cos(theta)
        sintheta = sin(theta)
        while phi < 2 * pi:
            cosphi = cos(phi)
            sinphi = sin(phi)
            phi += phi_spacing

            circlex = R2 + R1 * costheta
            circley = R1 * sintheta  # 圆的坐标
            x = circlex * (cosB * cosphi + sinA * sinB * sinphi) - circley * cosA * sinB
            y = circlex * (cosphi * sinB - cosB * sinA * sinphi) + circley * cosA * cosB
            z = K2 + cosA * circlex * sinphi + circley * sinA
            z_ = 1 / z
            xp = int(screen_width / 2 + K1 * z_ * x)
            yp = int(screen_height / 2 - K1 * z_ * y)
            L = cosphi * costheta * sinB - cosA * costheta * sinphi - sinA * sintheta + cosB * (
                    cosA * sintheta - costheta *
                    sinA * sinphi)
            if L > 0:
                if z_ > zbuffer[xp][yp]:
                    zbuffer[xp][yp] = z_
                    luminance_index = int(L * 8)
                    output[xp][yp] = ".,-~:;=!*#$@"[luminance_index]

        phi = 0
        theta += theta_spacing

    text = ''
    for a in output:
        for b in a:
            text += b + ' '
        text += '\n'

    return text


x = 0
y = 0
while x < 2 * pi and y < 2 * pi:
    os.system('cls')
    print(update(x, y))
    y += 0.03
    x += 0.03
    if x >= 2 * pi:
        x = 0
    if y >= 2 * pi:
        y = 0
