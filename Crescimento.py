import cv2, queue, math

dx = [1, -1, 0, 0, 1, -1, -1, 1];
dy = [0, 0, 1, -1, 1, -1, 1, -1];

# LER IMAGEM
#cv2.imshow("Original", imagem)

#print(imagem[0][0])

imagem = cv2.imread("sonic.png")

print("Altura (height): %d pixels" % (imagem.shape[0]))
print("Largura (width): %d pixels" % (imagem.shape[1]))
print("Canais (channels): %d"      % (imagem.shape[2]))


def inGrid(l, c, hl, hc):
    if(l >= 0 and c >= 0 and l < hl and c < hc):
        return 1
    else:
        return 0

# imagem[130][100]

height = imagem.shape[0]
width  = imagem.shape[1]

visitado = [[-1] * height] * width

def bfs(i, j):

    visitado[j][i] = 1
    fila1 = queue.Queue(maxsize=height * width)
    fila2 = queue.Queue(maxsize=height * width)

    fila1.put(i)
    fila2.put(j)

    while(fila1.empty() != True):
        x = fila1.get()
        y = fila2.get()
        
        #print('>> %d %d' %(x, y))

        for pos in range(0, 8):
            a = x + dx[pos]
            b = y + dy[pos]

            #print('\t >> %d %d' %(a, b))

            if(inGrid(a, b, height, width) == 1 and
                (imagem[a][b][0] >= 100 and imagem[a][b][0] <= 255) and
                (imagem[a][b][1] >= 50  and imagem[a][b][1] <= 200) and
                (imagem[a][b][2] >= 0   and imagem[a][b][2] <= 100)):

                '''print('%d: %d %d' %(pos, a, b), end = '')
                print(imagem[a][b])'''
                visitado[b][a] = 1

                fila1.put(a)
                fila2.put(b)

                imagem[a][b][2] = 0   # R
                imagem[a][b][1] = 0   # G
                imagem[a][b][0] = 0 # B

        imagem[x][y][2] = 255   # R
        imagem[x][y][1] = 0   # G
        imagem[x][y][0] = 0 # B

bfs(70, 130)
bfs(280, 120)
bfs(190, 106)
bfs(189, 156)

# ESCREVER NOVA IMAGEM
cv2.imwrite("newCrescimento.png", imagem)

# MOSTRA A IMAGEM
cv2.imshow("New Iagem", imagem)
cv2.waitKey(0)