from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import numpy as np

def trigon(x, y, r):
    """Алгоритм тригонометрической формулы"""
    img = Image.new('RGB', (800, 500), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    for i in range(360):
        angle = i * np.pi / 180
        px = x + r * np.cos(angle)
        py = y + r * np.sin(angle)
        draw.point((int(px), int(py)), fill=(255, 0, 0))
    return np.array(img)

def bresenham(x, y, r):
    """Алгоритм Брезенхема"""
    img = Image.new('RGB', (800, 500), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    d = 3 - 2 * r
    px, py = 0, r
    while px <= py:
        draw.point((x + px, y + py), fill=(0, 255, 0))
        draw.point((x + py, y + px), fill=(0, 255, 0))
        draw.point((x - px, y + py), fill=(0, 255, 0))
        draw.point((x - py, y + px), fill=(0, 255, 0))
        draw.point((x + px, y - py), fill=(0, 255, 0))
        draw.point((x + py, y - px), fill=(0, 255, 0))
        draw.point((x - px, y - py), fill=(0, 255, 0))
        draw.point((x - py, y - px), fill=(0, 255, 0))
        if d < 0:
            d += 4 * px + 6
        else:
            d += 4 * (px - py) + 10
            py -= 1
        px += 1
    return np.array(img)

def round_formula(x, y, r):
    """Алгоритм формулы круга"""
    img = Image.new('RGB', (800, 500), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    for i in range(-r*10, r*10+1):
        for j in range(-r*10, r*10+1):
            if abs(i**2/100 + j**2/100 - r**2) <= 1:
                draw.point((x + i//10, y + j//10), fill=(0, 0, 255))
    return np.array(img)

class AlgorithmPlot:
    def __init__(self, x, y, r):
        self.x, self.y, self.r = x, y, r
        self.fig, self.ax = plt.subplots()
        self.ax.set_title("Алгоритмы")
        self.ax.set_axis_off()
        self.buttons = [
            plt.Button(plt.axes([0.1, 0.05, 0.2, 0.075]), 'Тригонометрия'),
            plt.Button(plt.axes([0.4, 0.05, 0.2, 0.075]), 'Брезенхем'),
            plt.Button(plt.axes([0.7, 0.05, 0.2, 0.075]), 'Формула круга')
        ]
        self.buttons[0].on_clicked(self.plot_trigon)
        self.buttons[1].on_clicked(self.plot_brezenhem)
        self.buttons[2].on_clicked(self.plot_round_formula)

    def plot_trigon(self, event):
        self.ax.clear()
        plt.show(block=False)
        self.ax.imshow(trigon(self.x, self.y, self.r))
        plt.subplots_adjust(top=1.0, bottom=0.2, left=0.1, right=0.9)
        self.ax.set_title("Алгоритм тригонометрии")

    def plot_brezenhem(self, event):
        self.ax.clear()
        plt.show(block=False)
        self.ax.imshow(bresenham(self.x, self.y, self.r))
        plt.subplots_adjust(top=1.0, bottom=0.2, left=0.1, right=0.9)
        self.ax.set_title("Алгоритм Брезенхема")

    def plot_round_formula(self, event):
        self.ax.clear()
        plt.show(block=False)
        self.ax.imshow(round_formula(self.x, self.y, self.r))
        plt.subplots_adjust(top=1.0, bottom=0.2, left=0.1, right=0.9)
        self.ax.set_title("Алгоритм формулы круга")

def main():
    x, y = map(int, input("Введите координаты центра окружности (x y): ").split())
    r = int(input("Введите радиус окружности: "))
    plot = AlgorithmPlot(x, y, r)
    plt.show()

if __name__ == "__main__":
    main()