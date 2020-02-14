
import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt



def rule_of_life(x,y):
    #计算4x4矩阵内数值求和作为周围环境的参数
    nums_neighbours = np.sum(universe[x-1:x+2,y-1:y+2])-universe[x,y]
    if universe[x,y] == 1:
        if nums_neighbours < 2 or nums_neighbours > 3:
            new_universe[x,y] = 0
    elif universe[x,y] == 0:
        if nums_neighbours == 3:
            new_universe[x,y] = 1
#遍历画布上所有点值，出现以上两种情况的，改变值，最终返回新的universe
def judgement_day():
    global universe
    row = universe.shape[0]
    col = universe.shape[1]
    for i in range(row):
        for j in range(col):
            rule_of_life(i,j)

    universe = np.copy(new_universe)


if __name__ == "__main__":
    universe = np.zeros((50, 50))
    moon = [[1, 1, 0, 1],
            [1, 1, 0, 0],
            [0, 0, 1, 1],
            [1, 0, 1, 1]]

    # earth = [[1,1,0,1],
    #         [1,1,0,0],
    #         [0,0,1,1],
    #         [1,0,1,1]]

    earth = [[1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1]]
    #初始化universe，位置10：14占位11，12，13，14，其他同理
    universe[10:14, 11:15] = moon
    universe[14:18, 15:20] = earth

    # 可视化出来
    plt.imshow(universe, cmap='binary')
    plt.show()

    new_universe = np.copy(universe)
    #制作动画
    fig = plt.figure()
    plt.axis("off")
    #动画是连续的图片，因此将图片放到frame集合里，再用ArtistAnimation连续播放
    frame = []
    for i in range(500):
        frame.append((plt.imshow(universe,cmap="Blues"),))
        #产生图片
        judgement_day()
    img_animation = animation.ArtistAnimation(fig,frame,interval=1000,repeat_delay=1000,blit=True)
    #没有show显示不出来
    plt.show()




